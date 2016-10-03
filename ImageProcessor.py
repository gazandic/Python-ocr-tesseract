import pytesseract
import requests
import re
from PIL import Image
from PIL import ImageFilter
from os import listdir
from os.path import isfile, join
try:
    from BytesIO import BytesIO
except ImportError:
    from io import BytesIO

class ImageProcessor(object):
    NEWIMAGESIZE = 300
    path = ""
    def __init__(self):
        self.image = 0

    def process_images_from_dir(self, mypath):
        self.path = mypath + '/'
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        return self.process_images(onlyfiles)

    # process list image to string and print it
    def process_images(self, listUrl):
        s =  {}
        for url in listUrl:
            s[url] = self.process_image(self.path+url)+"\n"
        return s

    # process the image to string with tesseract library
    # sharpen image first
    def process_image(self, url):
        image = self._get_image(url)
        image.filter(ImageFilter.SHARPEN)
        image = self._resize_image(image, 3)
        image.filter(ImageFilter.GaussianBlur(2))
        image.filter(ImageFilter.SMOOTH)
        image.filter(ImageFilter.Kernel((3,3), [1,1,1,1,0,-1,-1,-1,-1]));
        s = pytesseract.image_to_string(image)
        return self.normalize(s)

    # get the image
    def _get_image(self, url):
        if "http" in url:
            return Image.open(BytesIO(requests.get(url).content))
        return Image.open(url)

   # resize image with magnitude
    def _resize_image(self, image, magnitude):
        xDim = image.size[0] * magnitude
        yDim = image.size[1] * magnitude
        newSize = self.aspectRatio(xDim, yDim)
        return image.resize((int(newSize[0]),int(newSize[1])),Image.ANTIALIAS)

   # normalize indonesian string for small email picture
    def normalize(self, string):
        string = string.replace(" ", "")
        string = string.replace("©", "@")
        string = string.replace("®", "@")
        s = list(string)
        i = 0
        numbercount = 0
        alphacount = 0
        for c in s:
            if self.isNumber(c):
                numbercount += 1
            elif self.isVowel(c):
                alphacount += 1
            elif not self.isVowel(c):
                alphacount += 1
                if c == 'l' and i<len(s)-1 and not self.isVowel(s[i-1]) and not self.isVowel(s[i+1]):
                    s[i] = 'i'
                if c == 'c' and i >= 1 and s[i-1] == 'L' :
                    s[i-1] = 'l'
                    s.insert(i,'.')
                if c == 'c' and i >= 1 and s[i-1] == '`' or s[i-1] == "'" or s[i-1] == '‘' or s[i-1] == ',' :
                    s[i-1] = '.'
                if c == 'S' and i >= 1 and self.isNumber(s[i-1]) and self.isNumber(s[0]) :
                    s[i] = '5'
                if c == 'g' and i >= 1 and self.isNumber(s[i-1]) and self.isNumber(s[0]):
                    s[i] = '9'
                if c == 'G' and i >= 1 and self.isNumber(s[i-1]) and self.isNumber(s[0]):
                    s[i] = '6'
            i += 1
        return "".join(s)

    # check the char is vowel or not
    def isVowel(self, c):
        return c == 'a' or c == 'i' or c == 'u' or c == 'e' or c == 'o'

    # check the char is number and - or not
    def isNumber(self, c, search=re.compile(r'[^0-9.-]').search):
        return not bool(search(c))

    # calculate aspectRatio from dimension x and y
    def aspectRatio(self, xDim, yDim):
        if xDim <= self.NEWIMAGESIZE and yDim <= self.NEWIMAGESIZE: #ensures images already correct size are not enlarged.
            return(xDim, yDim)

        elif xDim > yDim:
            divider = xDim/float(self.NEWIMAGESIZE)
            xDim = float(xDim/divider)
            yDim = float(yDim/divider)
            return(xDim, yDim)

        elif yDim > xDim:
            divider = yDim/float(self.NEWIMAGESIZE)
            xDim = float(xDim/divider)
            yDim = float(yDim/divider)
            return(xDim, yDim)

        elif xDim == yDim:
            xDim = self.NEWIMAGESIZE
            yDim = self.NEWIMAGESIZE
            return(xDim, yDim)

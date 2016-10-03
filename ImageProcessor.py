import pytesseract
import requests
from PIL import Image
from PIL import ImageFilter
try:
    from BytesIO import BytesIO
except ImportError:
    from io import BytesIO


class ImageProcessor(object):
    NEWIMAGESIZE = 300
    def __init__(self):
        self.image = 0

    def process_images(listUrl):
        for url in listUrl(keys, values):
            self.process_image(url)
        # do nothing

    # process the image to string with tesseract library
    # sharpen image first
    def process_image(self, url):
        image = self._get_image(url)
        image = self._resize_image(image, 3)
        image.filter(ImageFilter.SHARPEN)
        return pytesseract.image_to_string(image)

    # get the image
    def _get_image(self, url):
        return Image.open(BytesIO(requests.get(url).content))

    def _resize_image(self, image, magnitude):
        xDim = image.size[0] * magnitude
        yDim = image.size[1] * magnitude
        newSize = self.aspectRatio(xDim, yDim)
        return image.resize((int(newSize[0]),int(newSize[1])),Image.ANTIALIAS)

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

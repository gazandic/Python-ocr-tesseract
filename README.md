# Python-ocr-tesseract
Implement tesseract at python

#Install-dependencies
```
$ sudo apt-get update
$ sudo apt-get install autoconf automake libtool
$ sudo apt-get install libpng12-dev
$ sudo apt-get install libjpeg62-dev
$ sudo apt-get install g++
$ sudo apt-get install libtiff4-dev
$ sudo apt-get install libopencv-dev libtesseract-dev
$ sudo apt-get install git
$ sudo apt-get install cmake
$ sudo apt-get install build-essential
$ sudo apt-get install libleptonica-dev
$ sudo apt-get install liblog4cplus-dev
$ sudo apt-get install libcurl3-dev
$ sudo apt-get install python2.7-dev
$ sudo apt-get install tk8.5 tcl8.5 tk8.5-dev tcl8.5-dev
$ sudo apt-get build-dep python-imaging --fix-missing
$ wget http://www.leptonica.org/source/leptonica-1.70.tar.gz
$ tar -zxvf leptonica-1.70.tar.gz
$ cd leptonica-1.70/
$ ./autobuild
$ ./configure
$ make
$ sudo make install
$ sudo ldconfig
$ sudo pip install pytesseract 
$ pip install validate_email
# for python2
$ pip install pyDNS
# for python3
$ pip install py3DNS

```
#How-to-use
```
IP = ImageProcessor()  

# process 1 image  
s = self.IP.process_image('https://realpython.com/images/blog_images/ocr/sample5.jpg')  

# process 1 directory to string and store at file  
s = self.IP.process_images_from_dir("samples_images2")  
file = open("sample222.txt", "w")  
for key, val in s.items():  
    file.write("{} = {}".format(key, val))  
file.close  

```

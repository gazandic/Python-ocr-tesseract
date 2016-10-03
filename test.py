import unittest
from ImageProcessor import ImageProcessor

class IPTestCase(unittest.TestCase):
    def setUp(self):
        self.IP = ImageProcessor()

    def testOneImage(self):
        s = self.IP.process_image('https://realpython.com/images/blog_images/ocr/sample5.jpg')
        self.assertEqual(s, "1234567890", "wrong at testcase 1")

        s = self.IP.process_image('agungsukses.png')
        self.assertEqual(s, "gemilangsukses@gmail.com", "wrong at testcase 2")

    def testOnDirectorySample(self):
        s = self.IP.process_images_from_dir("sample_images")
        file = open("sample.txt", "w")
        for key, val in s.items():
            file.write("{} = {}".format(key, val))
        file.close

    def testOnDirectorySample2(self):
        s = self.IP.process_images_from_dir("samples_images2")
        file = open("sample2.txt", "w")
        for key, val in s.items():
            file.write("{} = {}".format(key, val))
        file.close

    # def testOnDirectoryTrue(self):
    #     s = self.IP.process_images_from_dir("images")
    #     file = open("real.txt", "w")
    #     for key, val in s.items():
    #         file.write("{} = {}".format(key, val))
    #     file.close

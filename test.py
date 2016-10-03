import unittest
from ImageProcessor import ImageProcessor

class IPTestCase(unittest.TestCase):
    def setUp(self):
        self.IP = ImageProcessor()

    def testOneImage(self):
        s = self.IP.process_image('https://realpython.com/images/blog_images/ocr/sample5.jpg')
        self.assertEqual(s, "1234567890", "wrong at testcase 1")
        s = self.IP.process_image('https://lh5.googleusercontent.com/FJtlOcFPYfqFfGEeYRKIeLELkzIIoJFWJI6Im2i8gHxReMnTWJPYj2zMzcbJv49edUN6fB2pmtvbNA=w1301-h673')
        self.assertEqual(s, "gemilangsukses@gmail.com", "wrong at testcase 2")

        # s = self.IP.process_image('results2.png')
        # self.assertEqual(s, "gemilangsukses@gmail.com", "wrong at testcase 2")

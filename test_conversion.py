import unittest
from converter import *


# Test the convert function of the App class
class TestApp(unittest.TestCase):
    def test_convert(self):
        app = App()
        app.entry.insert(0, "10")
        app.convert()
        self.assertEqual(app.output_label['text'], "16.09 km")


if __name__ == "__main__":  
    unittest.main()
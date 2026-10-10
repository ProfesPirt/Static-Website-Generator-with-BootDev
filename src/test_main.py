from main import extract_title
import unittest
class TestMain(unittest.TestCase):
    def test_extract_heading(self):
        md = """
# Hello World

This is a paragraph
"""
        self.assertEqual("Hello World",extract_title(md))

if __name__ == "__main__":
    unittest.main()

import unittest

from parsing_markdown import extract_markdown_images, extract_markdown_link

class TestParsingMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        result = extract_markdown_images("![This is alt text](https://www.yourmom.com)")
        self.assertEqual("This is alt text", result[0][0])
        self.assertEqual("https://www.yourmom.com", result[0][1])
    def test_extract_markdown_links(self):
        result = extract_markdown_link("[This is a link text](https://www.yourmom.com)")
        self.assertEqual("This is a link text", result[0][0])
        self.assertEqual("https://www.yourmom.com", result[0][1])

if __name__ == "__main__":
    unittest.main()

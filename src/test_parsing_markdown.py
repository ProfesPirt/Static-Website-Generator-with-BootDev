import unittest
import textnode
from parsing_markdown import extract_markdown_images, extract_markdown_link, text_to_textnodes
class TestParsingMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        result = extract_markdown_images("![This is alt text](https://www.yourmom.com)")
        self.assertEqual("This is alt text", result[0][0])
        self.assertEqual("https://www.yourmom.com", result[0][1])
    def test_extract_markdown_links(self):
        result = extract_markdown_link("[This is a link text](https://www.yourmom.com)")
        self.assertEqual("This is a link text", result[0][0])
        self.assertEqual("https://www.yourmom.com", result[0][1])
    def test_text_to_textnodes(self):
        result = [
            textnode.TextNode("This is ", textnode.TextType.TEXT),
            textnode.TextNode("text", textnode.TextType.BOLD),
            textnode.TextNode(" with an ", textnode.TextType.TEXT),
            textnode.TextNode("italic", textnode.TextType.ITALIC),
            textnode.TextNode(" word and a ", textnode.TextType.TEXT),
            textnode.TextNode("code block", textnode.TextType.CODE),
            textnode.TextNode(" and an ", textnode.TextType.TEXT),
            textnode.TextNode("obi wan image", textnode.TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            textnode.TextNode(" and a ", textnode.TextType.TEXT),
            textnode.TextNode("link", textnode.TextType.LINK, "https://boot.dev"),
        ]
        answer = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertEqual(result[0], answer[0])
        self.assertEqual(result[1], answer[1])
        self.assertEqual(result[2], answer[2])
        self.assertListEqual(result, text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"))

if __name__ == "__main__":
    unittest.main()

import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_defaulturl(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)
    def test_text_node_to_html_node(self):
        text_node1 = TextNode("This is a text node", "Invalid texttype")
        self.assertRaises(Exception, text_node_to_html_node, text_node1)
        text_node2 = TextNode("This is a text node", TextType.IMAGE, "project/images")
        result_leaf_node1 = text_node_to_html_node(text_node2)
        self.assertEqual("img",result_leaf_node1.tag)
        self.assertEqual("", result_leaf_node1.value)
        self.assertTrue("alt" in result_leaf_node1.props 
            and "src" in result_leaf_node1.props
        )
        self.assertEqual("This is a text node", result_leaf_node1.props["alt"])
        self.assertEqual("project/images", result_leaf_node1.props["src"])
if __name__ == "__main__":
    unittest.main()

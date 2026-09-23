import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode("div")
        self.assertEqual(node.tag,"div")
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
    def test_props_to_html(self):
        node1 = HTMLNode("div")
        node2 = HTMLNode("body", "This is a body text",[node1,],{"id": "burger"})
        self.assertEqual(node1.props_to_html(),"")
        self.assertEqual(node2.props_to_html(), 'id="burger"')
    def test_to_html(self):
        node = HTMLNode("div")
        self.assertRaises(NotImplementedError, node.to_html)

if __name__ == "__main__":
    unittest.main()

import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def setUp(self):
        self.node = node = LeafNode("p", "This is a paragraph.", {"id": "up"})
    def test_init(self):
        self.assertEqual(True, hasattr(self.node,"tag"))
        self.assertEqual(True, hasattr(self.node, "value"))
        self.assertRaises(TypeError, LeafNode, "p")
        self.assertTrue(self.node.children is None)
    def test_to_html(self):
        self.assertEqual('<p id="up">This is a paragraph.</p>', self.node.to_html())
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual("<p>This is a paragraph.</p>",node.to_html())

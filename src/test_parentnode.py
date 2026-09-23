import unittest
from parentnode import ParentNode
from leafnode import LeafNode
class TestParentNode(unittest.TestCase):
    def setUp(self):
       self.node1 = ParentNode("p",[
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text")
        ], )
       self.node2 = ParentNode(None, None)
       self.node3 = ParentNode("p", None)
       self.node4 = ParentNode(None, [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text")
        ])

    def test_init(self):
        self.assertTrue(self.node1.value is None)
        self.assertTrue(hasattr(self.node1,"tag"))
        self.assertTrue(hasattr(self.node1,"children"))
    def test_to_html(self):
        self.assertRaises(ValueError, self.node2.to_html)
        self.assertRaises(ValueError, self.node3.to_html)
        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", self.node1.to_html())
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()

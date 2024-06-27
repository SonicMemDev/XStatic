import unittest

from htmlnode import HTMLNode, LeafNode, BranchNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "This is a test node", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"'
        )
    
    def test_leafnode_paragraph(self):
        node = LeafNode("p", "This is a test node")
        self.assertEqual(
            node.to_html(),
            "<p>This is a test node</p>"
        )
    
    def test_leafnode_no_tag(self):
        node = LeafNode(None, "This is a test node")
        self.assertEqual(
            node.to_html(),
            "This is a test node"
        )

    def test_leafnode_link(self):
        node = LeafNode("a", "Press here", {"href": "https://test.link"})
        self.assertEqual(
            node.to_html(),
            f'<a href="https://test.link">Press here</a>'
        )

    def test_branchnode_to_html(self):
        childnode = LeafNode("i", "This is a test node")
        branchnode = BranchNode("p", [childnode])
        self.assertEqual(
            branchnode.to_html(),
            f'<p><i>This is a test node</i></p>'
        )

    def test_branchnode_multiple_children(self):
        child1 = LeafNode("b", "NOW")
        child2 = LeafNode("p", " the fun ")
        child3 = LeafNode("i", "truly")
        child4 = LeafNode("p", " begins!")
        branchnode = BranchNode("div", [child1, child2, child3, child4])
        self.assertEqual(
            branchnode.to_html(),
            f'<div><b>NOW</b><p> the fun </p><i>truly</i><p> begins!</p></div>'
        )

if __name__ == "__main__":
    unittest.main()
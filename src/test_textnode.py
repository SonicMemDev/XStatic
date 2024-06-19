import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
)


class TestTextNode(unittest.TestCase):
    def test_eq_no_url(self):
        node1 = TextNode("Equal nodes", text_type_bold)
        node2 = TextNode("Equal nodes", text_type_bold)
        self.assertEqual(node1, node2)
    
    def test_eq_with_url(self):
        node1 = TextNode("Url nodes", text_type_italic, "https://equal.nodes")
        node2 = TextNode("Url nodes", text_type_italic, "https://equal.nodes")
        self.assertEqual(node1, node2)
    
    def test_eq_not_equal(self):
        node1 = TextNode("One node", text_type_bold)
        node2 = TextNode("Another node", text_type_italic, "https://different.node")
        self.assertNotEqual(node1, node2)
    
    def test_text_type_not_equal(self):
        node1 = TextNode("Same text", text_type_bold)
        node2 = TextNode("Same text", text_type_italic)
        self.assertNotEqual(node1, node2)

    def test_repr(self):
        node = TextNode("Some text", text_type_bold, "https://test.dev")
        input = node.__repr__()
        expected = f"TextNode({node.text}, {node.text_type}, {node.url})"
        self.assertEqual(input, expected)



if __name__ == "__main__":
    unittest.main()
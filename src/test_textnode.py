import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This has different text", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.ITALIC)
        node5 = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        node6 = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node4)
        self.assertNotEqual(node, node5)
        self.assertEqual(node5, node6)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.google.com")
        test_string = "TextNode(This is a text node, text, https://www.google.com)"

        self.assertEqual(print(node),print(test_string))

if __name__ == "__main__":
    unittest.main()

import unittest
from blocks import block_to_block_type, BlockType
class TestBlocks(unittest.TestCase):
    def test_block_to_block_type(self):
        self.assertEqual(BlockType.HEADING, block_to_block_type("# This is a heading"))
        self.assertEqual(BlockType.CODE, block_to_block_type("```\nThis is a code block with some text\n```"))
        self.assertEqual(BlockType.QUOTE, block_to_block_type("> This is one line of a quote\n> This is another line of a quote"))
        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type("- This is a unordered list line\n- This is another unordered list line"))
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type("1. This is a ordered list\n2. This is a second line of a ordered list"))
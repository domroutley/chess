import unittest
from game import draw


class DrawTest(unittest.TestCase):

    def test_input_board_type_error(self):
        """
        Test to see if passing an object NOT of the correct board_type will result in a TypeError
        """
        with self.assertRaises(TypeError):
            draw.draw("")

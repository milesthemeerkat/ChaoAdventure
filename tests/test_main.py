"""
Initial file for testing
"""

import unittest
from chao_adventure.main import main


class TestMain(unittest.TestCase):
    """
    Placeholder test case
    """

    def test_main(self):
        """
        Test that main() returns Hello, World!
        """
        self.assertEqual("Hello, World!", main())

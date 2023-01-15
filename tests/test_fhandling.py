# -*- coding: utf-8 -*-

from .context import importscript

import unittest


class successful_csv(unittest.TestCase):
    """Basic test cases."""
    def test_absolute_truth_and_meaning(self):
        self.assertTrue(True)
    
    def test_create_folder(self):
        self.assertEquals()

if __name__ == '__main__':
    unittest.main()
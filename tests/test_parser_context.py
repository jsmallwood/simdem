# -*- coding: utf-8 -*-

from .context import simdem, context

import unittest
import os.path
import configparser
import mistune

class MistletoeParserTestSuite(unittest.TestCase):
    """Advanced test cases."""

    parser = None

    def setUp(self):
        self.maxDiff = None
        config = configparser.ConfigParser()
        config.read("content/config/unit_test.ini")

        self.parser = context.ContextParser()

    def test_full(self):
        file_path = 'content/complete-features/context.md'
        res = self.parser.parse_file(file_path)
        exp_res = {
            'prerequisites': ['prereq.md', 'prereq-2.md'],
            'commands': [
                { 'command': 'echo foo' },
                { 'command': 'echo bar' },
                { 'command': 'echo baz', 'expected_result': 'baz' } ]
        }

        self.assertEqual(res, exp_res)


if __name__ == '__main__':
    unittest.main()
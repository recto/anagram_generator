"""
Test case for tail.py
"""
import sys
sys.path.append("../src")
from pytail import PyTail
import unittest

DICTIONARY_FILE = '../src/resource/word_list.txt'

class PyTailTestCase(unittest.TestCase):
    """
        Test case for pytail module.
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pytail(self):
        """
            test case for PyTrail constructor
        """
        self.tail = PyTail(DICTIONARY_FILE, 5)
        self.assertEqual(5, self.tail.nline)
        self.assertEqual(DICTIONARY_FILE, self.tail.fname)
        # IOError should be thrown if the specified file does not exist.
        with self.assertRaises(IOError):
            self.tail = PyTail('donexist.txt', 10)

    def test_read_lines(self):
        """
            test case for PyTail.read_lines().
        """
        self.tail = PyTail(DICTIONARY_FILE, 5)
        expected = ['zythem\r\n', 'Zythia\r\n', 'zythum\r\n', 'Zyzomys\r\n',
                    'Zyzzogeton\r\n']
        self.assertEqual(expected, self.tail.read_lines())

if __name__ == "__main__":
    unittest.main()


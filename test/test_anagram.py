"""
Test case for anagram.py
"""
import sys
sys.path.append("../src")
from anagram import AnagramGenerator
from collections import defaultdict
import unittest

DICTIONARY_FILE = '../src/resource/word_list.txt'

class AnagramGeneratorTestCase(unittest.TestCase):
    """
        Test case for anagram module.
    """
    def setUp(self):
        self.generator = AnagramGenerator()
        self.dic = self.generator.load_dictionary(DICTIONARY_FILE)

    def tearDown(self):
        pass

    def test_load_dictionary(self):
        """
            test case for AnagramGenerator.load_dictionary().
        """
        self.assertEqual(235886, len(self.dic))

    def test_get_permutation(self):
        """
            test case for AnagramGenerator.get_permutations().
        """
        expected = ['ear', 'aer', 'rae', 'rea', 'era']
        self.assertEqual(expected, self.generator.get_permutations('are'))
        # with self.assertRaises(OverflowError):
        #     self.generator.get_permutations('are')

    def test_get_words(self):
        """
            test case for AnagramGenerator.get_words().
        """
        expected = [['ear'], ['ea', 'r'], ['e', 'ar'], ['e', 'a', 'r']]
        self.assertEqual(expected, self.generator.get_words('ear', self.dic))

    def test_get_anagrams(self):
        """
            test case for AnagramGenerator.get_anagrams().
        """
        perms = ['ear']
        expected = defaultdict(list)
        expected[1].append(['ear'])
        expected[2].append(['ea', 'r'])
        expected[2].append(['e', 'ar'])
        self.assertEqual(expected, self.generator.get_anagrams(perms, self.dic))

if __name__ == "__main__":
    unittest.main()


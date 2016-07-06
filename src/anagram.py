"""
Anagram Generator
"""
from __future__ import print_function
from itertools import permutations
from collections import defaultdict
from argparse import ArgumentParser

class AnagramGenerator(object):
    """
    AnagramGenerator class
    """

    def load_dictionary(self):
        """
        Load dictionary from resource/word_list.txt.
        """
        dic = defaultdict(bool)
        with open('resource/word_list.txt', 'r') as dictionary:
            for word in dictionary:
                word = word.strip()
                dic[word] = True
        return dic

    def get_permutations(self, src):
        """
        get permutations for the given input string.
        :param src: input string
        :return: list of permutations
        """
        words = list(set([''.join(word) for word in permutations(src) if word != tuple(src)]))
        return words

    def get_words(self, perm, dic):
        """
        get words for the given input string.
        :param perm: the input string
        :return: list of valid words
        """
        words = []
        for index in xrange(len(perm), 0, -1):
            # single character is always valid in the given dictionary.
            # avoid checking with dict.
            if len(perm[0:index]) == 1 or dic[perm[0:index]]:
                sub_words = self.get_words(perm[index:], dic)
                if sub_words != None and len(sub_words) > 0:
                    for sub_word in sub_words:
                        word = [perm[0:index]]
                        if isinstance(sub_word, list):
                            word.extend(sub_word)
                        else:
                            word.append(sub_word)
                        words.append(word)
                else:
                    words.append(perm[0:index])

            elif index == len(perm):
                words = []
        return words

    def get_anagrams(self, perms, dic):
        """
        return valid anagrams for the given permutations
        :param perms: list of permutations
        :return: list of valid anagrams
        """
        anagrams = defaultdict(list)
        for perm in perms:
            words = self.get_words(perm, dic)
            words = [anagrams[len(word)].append(word) for word in words if len(word) < len(perm)]
        # for key, values in anagrams.iteritems():
        #     print('word cound: {0}'.format(key))
        #     print(*values, sep='\n')
        return anagrams

def main():
    """
    Anagram generator main function
    """
    parser = ArgumentParser(description='Print anagrams with two words and max word length')
    parser.add_argument('word', metavar='input', type=str, help='input string')

    args = parser.parse_args()
    generator = AnagramGenerator()
    dic = generator.load_dictionary()
    #perms = generator.get_permutations('incredible')
    #perms = generator.get_permutations('are')
    #perms = generator.get_permutations('nails')
    perms = generator.get_permutations(args.word.replace(' ', ''))
    anagrams = generator.get_anagrams(perms, dic)
    maxwc = max(anagrams)
    two_words = []
    longests = []
    if anagrams.get(2) is not None:
        two_words = [' '.join(anagram) for anagram in anagrams.get(2)]
    if maxwc >= 2:
        longests = [' '.join(anagram) for anagram in anagrams.get(maxwc)]
    print('=== Two words anagrams:\n')
    print(*two_words, sep='\n')
    print('\n=== Anagrams with max word length, {0}:\n'.format(maxwc))
    print(*longests, sep='\n')

if __name__ == "__main__":
    main()

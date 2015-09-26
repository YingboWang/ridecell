import unittest
import random
import numpy
from anagrams import *
from anagrams.getAnagrams import *

class AnagramsTest(unittest.TestCase):

    def test_subWord(self):
        word1 = "liufjoaljhdkfjAIDNF"
        word2 = "lidk"
        expectedOutput = "ADFINaffhjjjlou"

        w1 = sorted(word1)
        w2 = sorted(word2)
        joinw = ''.join(subWord(w1, w2))
        self.assertEqual(joinw, expectedOutput)


    def ttest_2(self):
        print "testing anagrams"
        wordList = getWordList("data/words.txt")
        print wordList[10]
        getAnagrams(wordList, "abacination")
        print wordList[10]
        self.assertEqual(1, 1)


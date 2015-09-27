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


    def test_2(self):
        print "testing anagrams"
        wordList = getWordList("data/words.txt")
        for i in range(15):

            x = random.randint(0, len(wordList) - 1)
            print "generating anagrams of " + wordList[x]
            getAnagrams(wordList, wordList[x])
        print "generating anagrams of imperturbableness" 
        #getAnagrams(wordList, "imperturbableness")
        print "generating anagrams of incredible" 
        getAnagrams(wordList, "incredible")
        self.assertEqual(1, 1)


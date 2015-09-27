#!/usr/bin/python

def subWord(word1, word2):
    #remove all letters in word2 from word1 and return
    if len(word1)<= len(word2):
        return []
    result = [word1[i] for i in range(len(word1))]
    for i in range(len(word2)):
        if not word2[i] in result:
            return []
        result.remove(word2[i])
    return result
	
def getTwoAna(sortDict, word):
    #find two anagrams of word
    for x in sortDict:
        y = ''.join(subWord(word, x))
        if y == x and len(sortDict[x]) >= 2:
            return sortDict[x][0] + " " + sortDict[x][1]
        elif y != x and y in sortDict:
            return sortDict[x][0] + " " + sortDict[y][0]
    return ""

def getMaxAna(sortDict, word, maxDict):
    if word in maxDict:
        return maxDict[word]
    if len(word) <= 1:
        return ""
    numWords = 0
    maxAna = ""
    for x in sortDict:
        y = ''.join(subWord(word, x))
        if len(y) > 1:
            prevWords = getMaxAna(sortDict, y, maxDict).split()
            if len(prevWords) >= numWords:
                for i, z in enumerate(sortDict[x]):
                    if not z in prevWords:
                        maxAna = z + ' ' + ' '.join(prevWords)
                        numWords = len(prevWords) + 1
                        
                        break
    maxDict[word] = maxAna
    return maxAna

def getWordList(fname):
	with open(fname) as f:
		wordList = [line.rstrip() for line in f]
	return wordList
	
def getAnagrams(wordList, word):
	if len(word) < 2 or (not word in wordList):
		print "there is no such anagrams for " + word
		return
	sortWord = ''.join(sorted(word.lower()))
	sortDict = {}
	for x in wordList:
		if len(x) > 1:
			#In the word list, ignore the single character words.
			sortX = ''.join(sorted(x.lower()))
			if subWord(sortWord, sortX) != []:
				if sortX in sortDict:
					sortDict[sortX].append(x)
				else:
					sortDict[sortX] = [x]
	twoAna = getTwoAna(sortDict, sortWord)
	print twoAna

	maxDict = {}
	print getMaxAna(sortDict, sortWord, maxDict)



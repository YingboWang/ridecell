#!/usr/bin/python

def subWord(word1, word2):
	if len(word1)<= len(word2):
		return []
	result = [word1[i] for i in range(len(word1))]
	for i in range(len(word2)):
		if not word2[i] in result:
			return []
		result.remove(word2[i])
	return result
	
def getTwoAna(sortDict, word):
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
	if len(word) == 0:
		return ""
	numWords = 0
	maxAna = []
	for x in sortDict:
		y = subWord(word, x)
		if y != "":
			tmp = [sortDict[x][0]] + getMaxAna(sortDict, word, maxDict)
			if len(tmp) > numWords:
				numWords = len(tmp)
				maxAna = tmp
	maxDict[word] = maxAna
	return maxAna

def getWordList(fname):
	with open(fname) as f:
		wordList = [line.rstrip() for line in f]
	return wordList
	
def getAnagrams(wordList, word):
	sortWord = ''.join(sorted(word))
	sortDict = {}
	for x in wordList:
		sortX = ''.join(sorted(x))
		if subWord(sortWord, sortX) != []:
			if sortX in sortDict:
				sortDict[sortX].append(x)
			else:
				sortDict[sortX] = [x]
	twoAna = getTwoAna(sortDict, sortWord)
	print twoAna
	maxDict = {}
	print getMaxAna(sortDict, sortWord, maxDict)

#word1 = "liufjoaljhdkfjAIDNF"
#word2 = "lidkX"
#w1 = sorted(word1)
#w2 = sorted(word2)
#print ''.join(w1), ''.join(w2)

#print ''.join(subWord(w1, w2))

#wordList = getWordList("data/words.txt")
#getAnagrams(wordList, "abacination")


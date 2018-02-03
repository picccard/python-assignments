"""

	Title:     exam.py
	Date:      30.11.2017
    	Subject:   IINI4014_A
	Author:    10013

"""


import re
from analyseTools import file_to_word_array
from analyseTools import countWords

# Saves the filenames as variables
textFile01 = "SecondTextFile.txt"
textFile02 = "FirstTextFile.txt"
textFile03 = "ThirdTextFile.txt"


def averageWordCount(someTextFile):
    '''
    Takes a text file as an argument.
    Reads every sentence in the file.
    Uses regex to split on any delimiters chosen.
    Calculates the average numbers of words in a sentence.
    '''
    with open(someTextFile, 'r') as textFile:
        wordCount = []
        sentences = []
        text = textFile.read()

        delimiters = ["!", "...", "?", "."]
        regexPattern = '|'.join(map(re.escape, delimiters))
        sentences = re.split(regexPattern, text)
        # sentences = text.split('.') # here we can see that just splitting on '.' will make avgLength larger

        for sentence in sentences:
            wordsInSentence = sentence.split()
            wordCount.append(len(wordsInSentence))
        averageWordCount = sum(wordCount) / len(sentences)
        return averageWordCount


print('average word count in sentences')
print(averageWordCount(textFile01))


def sentenceLength(someTextFile):
    '''
    Takes a text file as an argument.
    Reads every sentence in the file.
    Returns a list with the wordcount of every sentence.
    Every sentence got the same index in the list as in the text.
    '''
    with open(someTextFile, 'r') as textFile:
        wordCount = []
        sentences = []
        text = textFile.read()

        delimiters = ["!", "...", "?", "."]
        regexPattern = '|'.join(map(re.escape, delimiters))
        sentences = re.split(regexPattern, text)
        # here we can see that just splitting on '.' wont catch all the sentences
        # sentences = text.split('.')

        for sentence in sentences:
            wordsInSentence = sentence.split()
            wordCount.append(len(wordsInSentence))

        return wordCount


print('every sentence\'s length in words')
print(sentenceLength(textFile01))


def percentageOfEasyWords(someTextFile):
    '''
    Takes a text file as an argument.
    Makes a array of every word in the text.
    Count how many times a unique words appears.
    Calculates the percentage of unique words that matches the 'easyword' criteria.

    More criterias SHOULD be added to make if more 'real' and
    criterias should be dynamic and change based on text length, number of unique words, etc.
    '''
    words = file_to_word_array(someTextFile)  # Every word in the text, could be dupes

    # Every unique word, and the number of times is appears in the text
    wordInstanceCount = countWords(words)
    numberOfWords = len(wordInstanceCount.keys())  # Number of unique words in the text

    easyWordCriteria = 10  # Hardcoded a value. a word is easy if it appears 10 or more times.
    easyWords = 0  # how many easy words the is in the text
    for word in wordInstanceCount.keys():
        if wordInstanceCount[word] >= easyWordCriteria:
            easyWords += 1

    # Returns the persentage of words that are marked 'easy'
    return (easyWords / numberOfWords * 100)


print('percentageOfEasyWords')
print(percentageOfEasyWords(textFile02))


def percentageOfDifficultWords(someTextFile):
    '''
    Takes a text file as an argument.
    Makes a array of every word in the text.
    Count how many times a unique words appears.
    Calculates the percentage of unique words that matches the 'hardword' criteria.

    More criterias SHOULD be added to make if more 'real' and
    criterias should be dynamic and change based on text length,
    number of unique words, average word length, average number a word occures, etc.
    Maybe the word should be rare AND be longer than 9 chars.
    '''
    words = file_to_word_array(someTextFile)  # Every word in the text, could be dupes

    # Every unique word, and the number of times is appears in the text
    wordInstanceCount = countWords(words)
    numberOfWords = len(wordInstanceCount.keys())  # Number of unique words in the text

    hardWordCriteriaOccurence = 1  # Hardcoded a value. a word is hard if it appears only 1 time.
    hardWordCriteriaLength = 10  # Hardcoded value. a word is hard if it got more than 9 characters.
    hardWords = 0  # how many hard words the is in the text
    for word in wordInstanceCount.keys():
        if wordInstanceCount[word] <= hardWordCriteriaOccurence:
            hardWords += 1
            continue
        if len(word) >= hardWordCriteriaLength:
            hardWords += 1
            continue

    # Returns the persentage of words that are marked 'hard'
    return (hardWords / numberOfWords * 100)


print('percentageOfDifficultWords')
print(percentageOfDifficultWords(textFile01))


def percentageOfDifferentWords(someTextFile):
    words = file_to_word_array(someTextFile)  # Every word in the text
    numberOfWords = len(words)
    wordInstanceCount = countWords(words)
    numberOfUniqueWords = len(wordInstanceCount.keys())
    return (numberOfUniqueWords / numberOfWords * 100)


print('percentageOfDifferentWords')
print(percentageOfDifferentWords(textFile01))


def numberOfSentencesPerParagraph(someTextFile):
    # Mr. Holmes is trubble. Should exclude known shortings like ['mr.', 'ms.', 'sir.']
    # Also centensen ending with ... wil count as 3 seperate sentences.
    # See content of textFile03
    with open(someTextFile, 'r') as textFile:
        numberOfSentences = 0
        # index 0 is the first paragrah and sentencePerParagraph[0] will should numberOfSentences i 0th paragrah, etc.
        sentenceInParagraph = []
        for line in textFile:
            numberOfSentences += line.count('.')
            numberOfSentences += line.count('?')
            numberOfSentences += line.count('!')
            if '\n' in line:
                sentenceInParagraph.append(numberOfSentences)
                numberOfSentences = 0

        return sentenceInParagraph


print('numberOfSentencesPerParagraph')
print(numberOfSentencesPerParagraph(textFile03))

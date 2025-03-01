# sentence = 'how are you'
sentence = 'My name is Oliver'

#function to remove unnecessary whitespace in the sentence
def cleanSentence(sentence):
    newSentence = sentence.strip()
    newSentence = newSentence.lower()
    result = ' '.join(newSentence.split())
    return repr(result)

# function to convert sentence to alien
def alienSentence(sentence):
    forConsonant = 'ay'
    forVowel = 'way'
    sentenceArr = []
    # strip off unneccessary white spaces in the string.
    cleanedSent = cleanSentence(sentence)
    cleanedSent = cleanedSent.strip("'")
    print(cleanedSent)
    # separate each word from sentence and push to array
    sentenceArr = cleanedSent.split()
    # print(sentenceArr)
    # loop through each word and apply the rules
    for word in sentenceArr:
        # check the first character if it matches our conditions and act on it respectively
        if (word[0] in ('a', 'e', 'i', 'o', 'u')):
            updatedWord = word+forVowel
            sentenceArr[sentenceArr.index(word)] = updatedWord
        else:
            # take first letter to the end of word and add 'ay'
            result = word[1:] + word[0]
            result2 = result+forConsonant
            sentenceArr[sentenceArr.index(word)] = result2
    # capitalize first word
    for word in sentenceArr:
        if (sentenceArr.index(word) == 0):
            list_of_chars = list(word)
            list_of_chars[0] = list_of_chars[0].upper()
            word = ''.join(list_of_chars)
            sentenceArr[0] = word
            break
    # generate the final result
    finalResult = ' '.join(sentenceArr)
    return finalResult


def alienTranslator():
    print("Hello!")
    # allow mutiple inputs from user
    x = list(map(str, input("Enter a sentence to be translated: ").split('  ')))
    # check for empty input
    isEmpty = True
    for i in x:
        if len(i) != 0:
            isEmpty = False
            break
    # print "Bye!" if input is empty
    if (isEmpty):
        print("Bye!")
    else:
        # proceed with next operations
        for sentence in x:
            # convert sentence to alien
            print(alienSentence(sentence))


# print(alienSentence(sentence))
alienTranslator()

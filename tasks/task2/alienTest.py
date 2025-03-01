# function to convert user iput to boolean
def bool(value):
    if(len(value) == 0):
        return False
    if(value.lower() == 'true' or value.lower() == 'false'):
        return True

# correct user input
def checkInput(value,question):
    print(value)
    value = value.strip()
    if(len(value)==0):
        return value
    if(value.lower() != 'true' and value.lower() != 'false'):
        print("Invalid input arguments!! acceptable argument are either 'true' ,'false' or empty")
        answer = input("What is your answer to "+ question +"? ")
        answer = checkInput(answer,question)
        return answer
    return value

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


def humanOrAlien():
    # prompt user input to answer questions.
    q1_answer = input("What is your answer to Q1? ")
    q1_answer = checkInput(q1_answer,'Q1')   
    q2_answer = input("What is your answer to Q2? ") 
    q2_answer = checkInput(q2_answer,'Q2')    
    q3_answer = input("What is your answer to Q3? ")
    q3_answer = checkInput(q3_answer,'Q3')   

    # convert user input to boolean
    q1_value = bool(q1_answer)
    q2_value = bool(q2_answer)
    q3_value = bool(q3_answer)    

    # use the boolean values to determine human or alien
    # if someone answers two or more wrong then alien otherwise human.
    # create an array
    responseArr = [q1_value, q2_value, q3_value]
    trueVals = []
    falseVals = []
    # separate true and false
    for i in responseArr:
        if i == True:
            trueVals.append(i)
        else:
            falseVals.append(i)
    if(len(falseVals) >= 2):
        print(alienSentence("You are an alien"))
    else:
        print("You are a human")

humanOrAlien() 
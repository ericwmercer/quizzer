'''
Created on Dec 2, 2011

@author: ericmercer
'''

def getNumberOfQuestions(quizType):
    '''
    Returns the number of questions for a quiz based on user input.
    '''
    is_number = False
    upperBound = {"state" : 100, "math" : 325, "vocab" : 115}
    errorMessage = "That is not a valid number. Number must be between 1 and " + str(upperBound[quizType]) + ".\n"
    while is_number == False:
        numQuestions = raw_input("How many questions would you like? ")
        try:
            numQuestions = int(numQuestions)
        except ValueError:
            print errorMessage
            continue
        if numQuestions <= 0:
            print errorMessage
            continue
        is_number = True
    if numQuestions > 115:
        numQuestions = 115
    print
    return numQuestions

def getMultipleChoiceAnswer(inputQuery):
    '''
    Returns the user's answer to a multiple-choice question as prompted by inputQuery.
    '''
    possibleAnswers = "abcd"
    input = raw_input(inputQuery).lower()
    while input not in possibleAnswers or len(input) != 1:
        print "That is not a valid answer.\n"
        input = raw_input(inputQuery).lower()
    return input

def displayMultipleChoiceQuestion(choices):
    '''
    Prints a formatted multiple-choice question from the given answer choices.
    '''
    possibleAnswers = "abcd"
    for i in xrange(4):
        print "\t" + possibleAnswers[i] + " - " + choices[i]
    print


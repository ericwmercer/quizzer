'''
Created on Nov 28, 2011

@author: Eric Mercer (ewm10)
'''

import random
import utils

def quizzer():
    # initialize
    print "Welcome to Quizzer to test your facts!\n"
    totalQuestions, totalCorrect = 0, 0
    choices = ["state capital quiz", "multiplication/division quiz", "vocabulary quiz", "EXIT"]
    quizzes = [stateQuiz, mathQuiz, vocabQuiz]
    currentQuiz = ""
    
    # run
    while currentQuiz != "d":
        if totalQuestions != 0:
            print "----------------------------------------\n"
            print "Your total is " + str(totalCorrect) + " of " + str(totalQuestions) + " questions correct.\n"
        
        print "Which quiz would you like to take?"
        utils.displayMultipleChoiceQuestion(choices)
        currentQuiz = utils.getMultipleChoiceAnswer("Enter letter (a, b, c, d): ")
        if currentQuiz == "d":
            break
        results = quizzes["abcd".index(currentQuiz)]()
        totalQuestions += results[0]
        totalCorrect += results[1]
    
    # exit
    print "\nThanks for taking the quiz!"
    return

def takeQuiz(quizType, numQuestions, questionBank):
    options = ["state", "math", "vocab"]
    questionTypes = [generateStateQuestion, generateMathQuestion, generateVocabQuestion]
    numCorrect = 0
    questionsRemaining = numQuestions
    while questionsRemaining > 0:
        correct = questionTypes[options.index(quizType)](questionBank)
        if correct:
            numCorrect += 1
        questionsRemaining -= 1
    print "You answered " + str(numCorrect) + " of " + str(numQuestions) + " questions correct.\n"
    return (numQuestions, numCorrect)

def stateQuiz():
    numQuestions = utils.getNumberOfQuestions("state")
    stateMap = getStateData()
    results = takeQuiz("state", numQuestions, stateMap)
    return results

def mathQuiz():
    numQuestions = utils.getNumberOfQuestions("math")
    problems = getMathProblems()
    results = takeQuiz("math", numQuestions, problems)
    return results

def vocabQuiz():
    numQuestions = utils.getNumberOfQuestions("vocab")
    vocabMap = getVocabData()
    results = takeQuiz("vocab", numQuestions, vocabMap)
    return results

def getStateData():
    '''
    Map states and abbreviations to a list of cities, the first of which is the capital
    '''
    file = open("../data/capitals.txt")
    stateMap = {}
    for line in file:
        info = line.split(":")
        state = info[0]
        abbrev = info[1]
        cities = [c.strip() for c in info[2:]]
        if state not in stateMap:
            stateMap[state] = cities
        if abbrev not in stateMap:
            stateMap[abbrev] = cities
    file.close()
    return stateMap

def getMathProblems():
    '''
    Generate all valid multiplication and division problems for the integers 0-12
    '''
    multProblems, divProblems = set(), set()
    for i in xrange(0, 13):
        for j in xrange(0, 13):
            multProblems.add(str(i) + " * " + str(j))
            divProblems.add(str(i*j) + " / " + str(i))
            divProblems.add(str(i*j) + " / " + str(j))
    divProblems.remove("0 / 0")
    return [list(multProblems), list(divProblems)]

def getVocabData():
    '''
    Map words to a list of possible meanings, the first of which is the correct definition
    '''
    file = open("../data/vocabulary.txt")
    vocabMap = {}
    for line in file:
        info = line.split(":")
        word = info[0]
        possibleMeanings = [c.strip() for c in info[1:]]
        if word not in vocabMap:
            vocabMap[word] = possibleMeanings
    file.close()
    return vocabMap

def generateStateQuestion(stateMap):
    # choose random question from question bank
    allStates = stateMap.keys()
    allCities = [c.strip() for cities in stateMap.values() for c in cities]
    randomState = random.choice(allStates)
    stateCities = stateMap[randomState]
    capital = stateCities[0]
    otherCities = stateCities[1:]
    del stateMap[randomState]

    # generate answer choices   
    choices = set()
    choices.add(capital)
    while len(choices) < 4:
        if len(choices) < len(otherCities) + 1:
            choices.add(random.choice(otherCities))
        else:
            choices.add(random.choice(allCities))

    # create and display random question
    print "What is the capital of " + randomState + "?"
    possibleAnswers = "abcd"
    choices = list(choices)
    random.shuffle(choices)
    utils.displayMultipleChoiceQuestion(choices)
    
    # get user's answer
    userAnswer = utils.getMultipleChoiceAnswer("Enter letter of answer: ")

    # check user's answer
    if choices[possibleAnswers.find(userAnswer)] == capital:
        print "That is correct!\n"
        return True
    print "That is not correct, " + capital + " is the capital of " + randomState + ".\n"
    return False

def generateMathQuestion(problems):
    randomOperation = random.randint(0, 1)
    problemType = ["multiplication", "division"]
    
    # get multiplication problem from question bank
    if problemType[randomOperation] == "multiplication":
        randomProblem = random.choice(problems[0])
        parts = randomProblem.split(" ")
        correctAnswer = int(parts[0]) * int(parts[2])
        problems[0].remove(randomProblem)
        problems[0].remove(parts[2] + " * " + parts[0])
        
    # else get division problem from question bank
    elif problemType[randomOperation] == "division":
        randomProblem = random.choice(problems[1])
        parts = randomProblem.split(" ")
        correctAnswer = int(parts[0]) / int(parts[2])
        problems[1].remove(randomProblem)

    # get user's answer
    is_number = False
    while is_number == False:
        userAnswer = raw_input(randomProblem + " = ")
        try:
            userAnswer = int(userAnswer)
        except ValueError:
            print "That is not a valid number. Please try again."
            continue
        is_number = True
        
    # check user's answer
    if userAnswer == correctAnswer:
        print "That is correct!\n"
        return True
    print "That is not correct, " + randomProblem + " = " + str(correctAnswer) + ".\n"
    return False

def generateVocabQuestion(vocabMap):
    # choose random question from question bank
    allWords = vocabMap.keys()
    randomWord = random.choice(allWords)
    possibleMeanings = vocabMap[randomWord]
    definition = possibleMeanings[0]
    del vocabMap[randomWord]

    # create and display random question
    print "What is the definition of " + randomWord + "?"
    possibleAnswers = "abcd"
    choices = possibleMeanings
    random.shuffle(choices)
    utils.displayMultipleChoiceQuestion(choices)
    
    # get user's answer
    userAnswer = utils.getMultipleChoiceAnswer("Enter letter of answer: ")
    
    # check user's answer    
    if choices[possibleAnswers.find(userAnswer)] == definition:
        print "That is correct!\n"
        return True
    print "That is not correct, the definition of " + randomWord + " is " + definition + ".\n"
    return False

if __name__ == "__main__":
    quizzer()


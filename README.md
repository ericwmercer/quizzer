Quizzer
=======
Interactive math, vocab, and US state capital quizzes with auto-scoring

Overview
--------
This assignment was first given in my second semester working as a CS101 TA. In the course of answering many student questions about this assignment, I eventually pieced together my own solution from scratch, including my first attempt at error-handling in Python. This interactive quizzer allows the user to work through randomly generated math, vocab, and US state capital quizzes while keeping track of score (number of questions correct out of total questions attempted).

Math Quiz
---------
This quiz offers multiplication and division problems using the numbers 0-12 (e.g. ``9*8`` and ``72/9``) and requires the user to type in the answer. Duplicate problems are avoided within the same quiz. For example, only one of ``9*8`` and ``8*9`` can be asking in a quiz since they're identical problems under the commutative property, but asking both ``12/3`` and ``12/4`` is valid since they are different problems with different answers.

Vocabulary Quiz
---------------
This quiz reads in a ``vocabulary.txt`` file where each line has an initial word followed by a word or phrase with the same meaning and then three distractors, all separated by colons:

```
checkup:medical examination:commemorative:restriction:boaster
aid:help:couch:robber:ship
accuse:blame:frighten:laugh softly:slap
assist:help:say:catch:menace
```

Questions are given by randomly selecting one of the initial words and then randomly shuffling the four possible answers from which the user is expected to select the correct meaning of the word.

US State Capital Quiz
---------------------
This quiz reads in a ``capitals.txt`` file where each line has a state followed by its abbreviation, capital city, and then 0 or more cities from that state, all separated by colons:

```
South Dakota:SD:Pierre
Ohio:OH:Columbus:Toledo:Cleveland
South Carolina:SC:Columbia:Charleston:Aiken:Spartanburg:Myrtle Beach:Edgefield:Cheraw:Anderson:Gaffney
New York:NY:Albany:New York
```

 Questions are given by randomly picking a state or state abbreviation and then presenting four choices for the capital. The three distractors are determined by first randomly choosing from all non-capital cities listed for the given state and then drawing from cities in other states if there aren't enough cities for the given state (while avoiding the risk of duplicate city names).

Instructions
------------
Run ``python quizzer.py`` to launch the program and enter the letter corresponding to the quiz you'd like to take (or "d" to exit). Then enter how many questions you'd like to attempt and answer questions in the format prompted by the selected quiz. Once a quiz is complete, you will be returned to the quiz selection screen, where you can either enter the letter corresponding to the next quiz you'd like to take or enter "d" to exit.

Sample Output
-------------
```shell
$ python quiz.py
Welcome to Quizzer to test your facts!

Which quiz would you like to take?
    a - state capital quiz
    b - multiplication/division quiz
    c - vocabulary quiz
    d - EXIT

Enter letter (a, b, c, d): a
How many questions would you like? 2

What is the capital of UT?
    a - Fayetteville
    b - Richmond
    c - Salt Lake City
    d - Ogden

Enter letter of answer: c
That is correct!

What is the capital of California?
    a - San Francisco
    b - Concord
    c - Los Angeles
    d - Sacramento

Enter letter of answer: d
That is correct!

You answered 2 of 2 questions correct.

----------------------------------------

Your total is 2 of 2 questions correct.

Which quiz would you like to take?
    a - state capital quiz
    b - multiplication/division quiz
    c - vocabulary quiz
    d - EXIT

Enter letter (a, b, c, d): b
How many questions would you like? 2

4 * 11 = 44
That is correct!

3 / 3 = 1
That is correct!

You answered 2 of 2 questions correct.

----------------------------------------

Your total is 4 of 4 questions correct.

Which quiz would you like to take?
    a - state capital quiz
    b - multiplication/division quiz
    c - vocabulary quiz
    d - EXIT

Enter letter (a, b, c, d): c
How many questions would you like? 2

What is the definition of pupil?
    a - student
    b - comment
    c - taxi
    d - error

Enter letter of answer: a
That is correct!

What is the definition of ornament?
    a - reporter
    b - decoration
    c - alarm
    d - counselor

Enter letter of answer: b
That is correct!

You answered 2 of 2 questions correct.

----------------------------------------

Your total is 6 of 6 questions correct.

Which quiz would you like to take?
    a - state capital quiz
    b - multiplication/division quiz
    c - vocabulary quiz
    d - EXIT

Enter letter (a, b, c, d): d

Thanks for taking the quiz!
```
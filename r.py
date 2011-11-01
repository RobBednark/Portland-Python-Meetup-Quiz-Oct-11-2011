QUESTION = 'Q: What does the code below the hash marks do?'

GUESSES = '''
    0 a
    1 b
    2 c
'''

import quiz
quiz.show(question=QUESTION, guesses=GUESSES, py_file=__file__, is_code=True)

################################################################################
myList = ['a', 'b', 'c']
for x,y in enumerate(myList):
    print(x,y)

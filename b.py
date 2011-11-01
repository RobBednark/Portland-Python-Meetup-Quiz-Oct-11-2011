QUESTION = 'What does the code below the hash marks do?'

import quiz
quiz.show(question=QUESTION, py_file=__file__, is_code=True)

################################################################################
def A(x):
    x()

def B():
    print("B")

A(B)

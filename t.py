QUESTION = 'Q: What does the code below the hash marks do?'

import quiz
quiz.show(question=QUESTION, py_file=__file__, is_code=True)

################################################################################
def x():
    print("function x")
x = ('a','b','c')
x = ['one','two','three']
x = {1:2, 3:4}
x = "foo"
print(x)

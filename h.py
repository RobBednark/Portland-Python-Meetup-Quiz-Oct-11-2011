QUESTION = 'Q: What does the code below the hash marks do?'

import quiz
quiz.show(question=QUESTION, py_file=__file__, is_code=True)

################################################################################
a = ["one"]
a += ["two"]
print(a)

b = ["larry"]
b += "moe"
print(b)

c = [1]
c += 2
print(c)

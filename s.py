QUESTION = 'Q: What does the code below the hash marks do?'

import quiz
quiz.show(question=QUESTION, py_file=__file__, is_code=True)

################################################################################
x = 5
assert x == 5
assert x == 6

QUESTION = 'Q: What does the code below the hash marks do?'

import quiz
quiz.show(question=QUESTION, py_file=__file__, is_code=True)

################################################################################
larry = { 2 : 4 }
moe = { 1 : 3 }
larry.update(moe)
print(larry)

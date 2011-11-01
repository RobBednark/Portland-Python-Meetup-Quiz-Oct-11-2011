QUESTION = 'Q: What does the code below the hash marks do?'

import quiz
quiz.show(question=QUESTION, py_file=__file__, is_code=True)

################################################################################
my_list = [3,1,2]
print(my_list)
print(my_list.sort())

print(my_list)
print(sorted(my_list))

print(my_list)

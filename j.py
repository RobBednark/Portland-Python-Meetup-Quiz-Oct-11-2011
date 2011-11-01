QUESTION = 'Q: What does the code below the hash marks do?'

import quiz
quiz.show(question=QUESTION, py_file=__file__, is_code=True)

################################################################################
import urllib
import re
x = urllib.urlopen('http://python.org/download').read()
y,z = re.search(string=x,
                pattern='(?s)The current production versions are.*?'
                        'Python (2\.\d+\.\d+).*?and.*?Python (3\.\d+\.\d+)').groups()
print("y: [%s]\nz: [%s]" % (y,z))

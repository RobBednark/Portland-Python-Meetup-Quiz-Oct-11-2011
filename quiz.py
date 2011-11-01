import os
import re
import sys

def show(question, py_file, guesses=None, is_code=False):
    PY_VERSION = sys.version
    PY_VERSION = PY_VERSION.replace("\n","")
    PY_FILE_BASE = py_file.replace(".py", "")
    SEP = "=" * 80
    question = question.strip()

    # Get the answer
    answer = ''
    ans_file = "answer."
    ans_file += py_file.replace("py","txt")
    if os.path.exists(ans_file):
        answer = open(ans_file).read()

    if is_code:
        # Grab the code below the hash marks
        whole_file = open(py_file).read()
        code = re.search(string=whole_file,
                         pattern="(?s)(#{10,}.*)").group(1)

    # Get the guesses
    if guesses:
        # Use the value of guesses passed-in
        pass
    else:
        guessesFilename = "guesses.%s.txt" % PY_FILE_BASE

        if os.path.exists(guessesFilename):
            guesses = open(guessesFilename).read()
        else:
            guesses = ''

    print(SEP)
    print("QUESTION [%s]:" % PY_FILE_BASE)
    print(SEP)
    print(question)

    if is_code:
        print(code)

    print(SEP)
    print("GUESSES:")
    print(SEP)
    print(guesses)


    if py_file and not is_code:
        print(SEP)
        print("ANSWER:")
        print(SEP)
        print(answer)

    if is_code:
        print(SEP)
        print("ANSWER / OUTPUT:  [Python version: %s]" % PY_VERSION)
        print(SEP)

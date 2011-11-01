#!/bin/sh

# Run each of the *.py quiz questions
for oneFile in [a-z].py; do
    python $oneFile
    echo "Hit return for the next question..."
    read keyboard_input
done

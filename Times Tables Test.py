# Test Times Tables.
from random import randint

# Ask the user which table to test:
xtable = int(input("Enter the times table to test? "))
xtable = int(xtable)

numCorrect = 0
answer = -1
while answer != 0:
    # ask question
    num = randint(1,12)
    answer = input("What is " + str(xtable) + " x " + str(num) + "? ")
    answer = int(answer)

    if answer == xtable * num:
        print("Correct.")
        numCorrect = numCorrect + 1

print("You got " + str(numCorrect) + " correct. ")
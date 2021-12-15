import math

def calcTimesPi(amount):
    amount = amount * math.pi
    return amount

question = int(input("give me a number"))

#This prints a long answer
answer = calcTimesPi(question)
print(question,"times Pi is",answer)

#This prints an answer limited to 2 decimal places
answer = round(answer, 2)
print(question,"times Pi is",answer)

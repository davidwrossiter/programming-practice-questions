def validateguess(answer, guess, mode):
    positions = {}
    correct = 0
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            positions[i+1] = guess[i]
            correct += 1
        else:
            positions[i+1] = "?"
    if mode == 0:
        print(positions)
    else:
        print(correct)
    return(correct)
import random
correctglobal = 0
answerglobal = ""
try:
    length = int(input("please select length of password to guess (4 is recomended)\n>>>"))
except(TypeError):
    print("please input a number *restart program*")
if input("please type 'easy' (without quotes) if you want to play on easy mode \n>>>") == "easy":
    modeglobal = 0
else:
    modeglobal = 1
for i in range(length):
    answerglobal += str(random.randint(0,9))
while correctglobal != length:
    guessglobal = input("please make a guess\n>>>")
    if len(guessglobal) == length:
        correctglobal = validateguess(answerglobal, guessglobal, modeglobal)
print("congratulations")
atsigns = 0
stopafterat=0
validstart=0
containsspace=0
emailtocheck = input("please enter your email adress\n>>>")
for i in emailtocheck:
    if i != "@":
        validstart=1
    if i == "@":
        atsigns += 1
    if atsigns == 1 and i == ".":
        stopafterat += 1
    if i == " ":
        containsspace = 1
if validstart == 1 and atsigns == 1 and stopafterat == 1 and containsspace == 0:
    print("email valid")
else:
    print("email invalid")
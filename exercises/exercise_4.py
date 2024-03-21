# Exercise 4
symmetry = input("Input a 4 digit number: ")
symmetry = list(symmetry)
checker = True

if symmetry[0] != symmetry[3]:
    checker = False
elif symmetry[1] != symmetry[2]:
    checker = False

if checker == False:
    print(0)
else:
    print(1)

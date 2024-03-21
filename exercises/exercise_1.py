# Exercise 1
# Your solution comes here

n = input("Enter a 5 Digit number : ")
string = list(n)

sum1 = int(string[0]) + int(string[2]) + int(string[4])
sum2 = int(string[1]) + int(string[3])

final = str(sum1) + str(sum2)
print(final)




# Exercise 6
a = int(input("Enter Integer:"))
b = int(input("Enter another Integer:"))

div = "Yes" * (a%b == 0) or "no"
print(div)
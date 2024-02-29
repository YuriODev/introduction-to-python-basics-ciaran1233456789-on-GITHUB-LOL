# Exercise 5
a = int(input("Input Integer: "))
b = int(input("Input another Integer: "))

max_value = a * (a > b) + b * (b >= a)
print(max_value)
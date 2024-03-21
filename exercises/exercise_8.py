# Exercise 8
a = int(input("Enter a value"))
b = int(input("Enter a value"))
c = int(input("Enter a value"))

if a < b:
    if b < c:
        print(c, "is the biggest value.\n", b, "is the mid value\n",a,"is the smallest")
    else:
        print(b, "is the biggest value.\n", c, "is the mid value\n",a,"is the smallest")
else:
    if a < c:
        print(c, "is the biggest value.\n", a, "is the mid value\n",b,"is the smallest")
    else:
        print(a, "is the biggest value.\n", c, "is the mid value\n",b,"is the smallest")
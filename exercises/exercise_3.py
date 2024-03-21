#Exercise 3
n = int(input("Input a number of seconds: "))

hours = n // 3600
temp = n % 3600
mins = temp // 60
seconds = temp % 60

print(hours,":",mins,":",seconds)
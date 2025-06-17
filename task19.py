year = int(input("enter year: "))

result = year % 4 == 0 or year % 100 == 0
print(result)
S = input("Enter the string of number : ")
result = 0
for s in S:
    i = int(s)
    if (result == 0 or result == 1 or i == 0 or i == 1):
        result += i
    else:
        result *= i

print(f"Max : {result}")

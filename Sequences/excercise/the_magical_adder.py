num = input("Please enter three numbers:").split(",")

for index in range(len(num)):
    num[index] = int(num[index])

result = num[0] + num[1] - num[2]
print(result)

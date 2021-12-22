number = int(input("Введите число "))

if (number == 0):
    print(1)
    exit()

countZero = 0
while (number % 10 == 0):
    number //= 10
    countZero += 1

print(countZero)
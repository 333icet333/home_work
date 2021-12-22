s = input("Введите числа через пробел ").split()
n = 0
for i in range(len(s)):
    if s[i].isdigit():
        n += int(s[i])
print(n)
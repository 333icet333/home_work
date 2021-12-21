word = input("Введите слово ")
print(word)
word = set(word)
word_A = set('A')
check_A = word_A <= word
print(check_A)

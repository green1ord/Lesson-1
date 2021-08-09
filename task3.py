#task 3

percent = int(input('Ввдите число процена: '))
if percent == 1:
  word = 'процент'
elif percent <= 4:
    word = 'процентов'
else:
    word = 'процентов'
print(percent, word)
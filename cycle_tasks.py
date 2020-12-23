import random
"""
Спросили у пользователя предел и от нуля до предела выводим(принтуем) все числа кроме кратных 18ти. На числе 42 принтуем "Потому что".  Числа от 50ти до 80ти игнорируем.
"""
# number = int(input("Enter the number "))
# i = 0
# while i < number:
#     i += 1
#     if i >= 50 and i <= 80:
#         continue
#     elif i != 48 and i % 18 != 0 :
#         print(i)
#     elif i == 48:
#         print('Потому что')
"""
Спросить у пользователя сколько попыток и до скольки максимум пробовать. Сделать генерацию рендомного значения столько то раз. Каждое значение вывести и потом вывести итоговое максимально выпавшее число.
"""
attempt = int(input('Enter a number '))
b = 0
max = 0
while b < attempt:
    b += 1
    rand = random.randint(0, b)
    print(rand)
    if rand > max:
        max = rand
print('Max number ', max)
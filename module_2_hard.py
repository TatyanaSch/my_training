a = ''
x  = int (input("Введите число от 3 до 20: "))

if  x > 20 or x < 3:
    print('Неверно введено число, попробуйте еще раз')
else:
    a += f' Ключ для {x} найден:{a}'
    for i in range (1,21):
        for j in range(i, 21):
            k = i + j
            if i >= x or j >= x or k > x:
                break
            if x % k == 0 and j!= i:
                a += f'{i}{j}'
            else:
                 continue
print(a)


#Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes =[]
not_primes = []
is_prime = True
for i in numbers [1:]:
    for j in range (2,i):
        if i % j == 0:
            is_prime = False
            break
        else:
            is_prime = True
            continue
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print ('Primes: ', primes)
print ('Not Primes: ', not_primes)






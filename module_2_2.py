first = int (input ('Введите первое число:'))
second = int (input ('Введите второе число:'))
third = int (input ('Введите третье число:'))
if first==second and second==third:
    print (3)
elif first==second and second!=third or  first==third and third!=second or second==third and third!= first:
    print (2)
else:
    print(0)

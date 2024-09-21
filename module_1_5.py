immutable_var= 1,2,True,("hello")
print(immutable_var)
#immutable_var [0]=2
#print (immutable_var)
# кортеж неизменяемый объект, не поддерживает обращение к элементам, поэтому выдает ошибку
mutable_list=[1,2,7,'hi',False]
mutable_list [4] = True
print (mutable_list)
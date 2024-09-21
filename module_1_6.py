my_dict = {'Tanya': 1976, 'Misha': 1974, 'Valera': 2003, 'Arseniy': 2013}
print ('Dict:', my_dict)
print ('Existing value:', my_dict ['Tanya'])
print ('Not existing value:', my_dict.get ('Katya'))
my_dict.update({'Lena': 2007, 'Sonya': 2010})
a= my_dict.pop ('Valera')
print ('Deleted value:',a)
print ('Modified dictionary:',my_dict)

my_set = {(4,5,3,6),'fly',5,True}
print ('Set:',my_set)
my_set.add(9)
my_set.add(3.421)
my_set.discard('fly')
print ('Modified set:',my_set)

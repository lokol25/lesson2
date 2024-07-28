my_dict = {'Никита': 1999, 'Андрей': 1995}
print(my_dict)
print(my_dict.get('Андрей'))
print(my_dict.get('Денис'))
my_dict.update({'Сергей': 2000 , 'Олег': 1987})
new_my_dict = my_dict.pop('Никита')
print(new_my_dict)
my_set = {1,2,3,2,1}
print(my_set)
my_set.update({4,5})
my_set.remove(3)
print(my_set)

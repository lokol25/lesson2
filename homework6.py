my_dict = {'Никита': 25_10_1999, 'Андрей': 13_05_1995}
print(my_dict)
print(my_dict.get('Андрей'))
print(my_dict.get('Денис'))
my_dict.update({'Сергей': 5_12_2000 , 'Олег': 10_08_1987})
del my_dict['Никита']
print(my_dict)
my_set = {1,2,3,2,1}
print(my_set)
my_set.update({4,5})
my_set.remove(3)
print(my_set)
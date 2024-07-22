immutable_var = ([1, 2], 'a', 'b')
print(immutable_var)
print(immutable_var[0])
print(immutable_var[-1])
# immutable_var.remove('a') AttributeError: 'tuple' object has no attribute 'remove'
# Кортеж не поддерживает обращение к элементу соответственно нельзя внести изменения
immutable_var[0][0] = 5  # Но можно изменить список который находится в внутри кортежа
print(immutable_var)
mutable_list = [1, 2, 3, 4]
print(mutable_list)
mutable_list[0] = 5
print(mutable_list)

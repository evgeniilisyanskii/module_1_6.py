my_dict = {'Евгения': 1990, 'Анна': 1989, 'Ксения': 2016}
print(my_dict)
print(my_dict['Ксения'])
print(my_dict.get('Иван'))
my_dict.update({'Полина': 2005, 'Иван': 2023})
print(my_dict)
d=my_dict.pop('Анна')
print(d)

my_set = {3,3,5,5,7,7,8,8,9,9, 'Победа', 2.468, (1,2,3)}
print(my_set)
my_set.add(1812)
print(my_set)
my_set.add(1941)
print(my_set)
my_set.discard(2.468)
print(my_set)


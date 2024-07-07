my_dict = {'Mila': 1985, 'Den': 1994, 'Mark': 2002}
print('Dict:', my_dict)
print('Existing value:', my_dict['Den'])
print('Not existing value:', my_dict.get('Ket'))
my_dict.update({'Vika': 1982, 'Ivan': 1984})
my_dict1 = my_dict.pop('Mark')
print('Deleted value:', my_dict1)
print('Modified dictionary:', my_dict)

my_set = {1, 2, 1, 5, 'appel', 'lemon', 'appel', 5}
print('Set:', my_set)
my_set.add('wednesday')
my_set.add('peach')
my_set.discard('lemon')
print('Modified set:' , my_set)
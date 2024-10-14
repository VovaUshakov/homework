def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(2, 1, 'vk')
print_params()
print_params(1, 3, 1)
print_params(2, 'fid')
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = [344, 'poker', False]
values_dict = {'a': 404, 'b': 'Reaper', 'c': [1, 2, 3]}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [True, 'sun']
print_params(*values_list_2, 42)

def calculate_structure_sum(structur):
    sumer = 0
    for i in structur:
        if isinstance(i, int):
           sumer += i
        elif isinstance(i, str):
            sumer += len(i)
        elif isinstance(i, list) or isinstance(i, tuple):
            sumer += calculate_structure_sum(i)
        elif isinstance(i, dict):
            sumer += calculate_structure_sum(list(i.keys()))
            sumer += calculate_structure_sum(list(i.values()))
        elif isinstance(i, set):
            sumer += calculate_structure_sum(i)
    return sumer






data_structure = [

[1, 2, 3],

{'a': 4, 'b': 5},

(6, {'cube': 7, 'drum': 8}),

"Hello",

((), [{(2, 'Urban', ('Urban2', 35))}])

]

print(calculate_structure_sum(data_structure))
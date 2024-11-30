from pprint import pprint


def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'a', encoding='utf-8')
    i = 1
    for k in strings:
        strings_positions.update({f'{i},{file.tell()}': k})
        file.write(f'{k}\n')
        i += 1
    file.close()
    return strings_positions


info = [

    'Text for tell.',

    'Используйте кодировку utf-8.',

    'Because there are 2 languages!',

    'Спасибо!'

]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)

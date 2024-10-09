calls = 0


def count_calls():
    global calls
    calls += 1
    return


def string_info(string=''):
    count_calls()
    return (tuple((len(string), string.upper(), string.lower())))


def is_contains(string="", list_to_search=[]):
    uppercase_list = [s.upper() for s in list_to_search]
    string = string.upper()
    a = False
    for i in uppercase_list:
        if string == i:
            a = True
            break
    count_calls()
    return a


print((string_info('Песня')))
print(string_info('vova'))
print(string_info('Музыка'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

x = int(input("Скорее , вводи число из  первой вставки "))
nambers = ''
for i in range(1, x):
    for k in range(i + 1, x):
        if x % (i + k) == 0:
            nambers += str(i) + str(k)
print('Вводи код и беги : ', nambers)

from fake_math import divide as divfake
from true_math import divide as divtru


print(int(divtru(12,2)))
print(divtru(12,0))
print(divfake(12,4))
print(divfake(50,0))

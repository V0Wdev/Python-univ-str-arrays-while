from random import *
def sorting(a, b):
    if b==0:
        a.sort()
        return print(a)
    elif b==1:
        a.sort(reverse=True)
        return print(a)
    else:
        return print('Ошибка ввода данных')

a=[]
print('Input array size:')
N=int(input())
for i in range(N+5):
    a.append(randint(0, 100))
print(a)
b = int(input('Choose how to sort the array: 0 - in ascending order, 1 - in descending order:'))
print('Array:')
sorting(a, b)



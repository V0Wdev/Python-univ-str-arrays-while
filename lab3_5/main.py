from random import *
def sorting(a, b):
    if b==0:
        a.sort()
        return print(a)
    elif b==1:
        a.sort(reverse = True)
        return print(a)
    else:
        return print('Error')

def changed(a):
    i = 1
    while i<N:
        a[i]+=i
        i+=1
    return print(a)
a=[]
print('Input array size:')
N=int(input())
for i in range(N):
    a.append(randint(0, 100))
print(a)
b = int(input('Choose how to sort the array: 0 - in ascending order, 1 - in descending order:'))
print('Array:')
sorting(a, b)
print('Array with adding indexes:')
changed(a)


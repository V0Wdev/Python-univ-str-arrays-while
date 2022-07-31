n = 6
b = ''
c = 0
while n > 0:
    b = str(n % 2) + b
    n = n // 2
print('Number of units=')
print(b.count('1'))

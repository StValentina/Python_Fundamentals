n = int(input('Enter a number:'))

if n % 2 == 0:
    n += 1

for i in range(n):
    for j in range(n):
        if i % 2 == 0 and j % 2 == 0 or i % 2 != 0 and j % 2 != 0:
            print('*', end='')
        else:
            print('_', end='')
    print()

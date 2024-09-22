n = 5
for i in range(n):
    for j in range(i, n):
        print(' ', end=' ')
    for j in range(i):
        print('*', end=' ')
    for j in range(i+1):
        print('*', end=' ')
    print()
n -= 1

for i in range(n):
    for j in range(0, i + 2):
        print(' ', end=' ')
    for j in range(0, n - i - 1):
        print('*', end=' ')
    for j in range(i, n):
        print('*', end=' ')
    print()
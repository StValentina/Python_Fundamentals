n = int(input('Enter a number:'))

for i in range(1, n):
    for j in range(i, n):
        print(' ', end=' ')
    for j in range(1, i):
        print(j, end=' ')
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()

for i in range(1, n-1):
    for j in range(i + 1):
        print(' ', end=' ')
    for j in range(1, n - i):
        print(j, end=' ')
    for j in range(n - i - 2, 0, -1):
        print(j, end=' ')
    print()
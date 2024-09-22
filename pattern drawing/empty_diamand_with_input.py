n = int(input("Въведете размер на диаманта (нечетно число): "))

if n % 2 == 0:
    n += 1

for row in range(n):
    for col in range(n):
        if (row + col == n // 2) or (col - row == n // 2) or \
           (row - col == n // 2) or (row + col == n + n // 2 - 1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

# Въвеждане на размера от потребителя
size = int(input("Въведете размер на диаманта (нечетно число): "))

# Проверка дали въведеното число е нечетно
if size % 2 == 0:
    size += 1

for row in range(size):
    for col in range(size):
        if (row + col == size // 2) or (col - row == size // 2) or \
           (row - col == size // 2) or (row + col == size + size // 2 - 1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
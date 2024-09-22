while True:
    n = int(input('Enter odd number:'))
    if n % 2 == 0:
        print('Please, enter ODD number (e.g. 3, 5, 7 or 9)!')
        continue
    else:
        for i in range(n):
            for j in range(n):
                if i % 2 == 0 and j % 2 == 0 or i % 2 != 0 and j % 2 != 0:
                    print('*', end=' ')
                else:
                    print('_', end=' ')
            print()
        break

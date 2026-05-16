n = int(input())

if n >= 10 and n % 2 != 0:
    print('100')
elif n >= 10 and n % 2 == 0:
    print('200')
elif n < 10 and n % 2 != 0:
    print('300')
elif n < 10 and n % 2 == 0:
    print('400')

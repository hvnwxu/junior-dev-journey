l, m, n = map(int, input().split())

if l >= 70:
    if n * 50 <= m:
        print('possible')
    else:
        print('impossible')
else:
    print('no entry')

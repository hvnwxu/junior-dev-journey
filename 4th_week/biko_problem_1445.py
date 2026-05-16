a, b = map(int, input().split())
if a + b >= 10:
    if a + b >= 100:
        lose = list(map(int, str(a + b)))
        plus = lose[-1] + lose[-2]
    else:
        lose = list(map(int, str(a + b)))
        plus = lose[-2] + lose[-1]
    print(plus)
else:
    print(a + b)
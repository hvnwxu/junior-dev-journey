h1, m1 = map(int, input().split())
h2, m2 = map(int, input().split())
time = (h2 * 60 + m2) - (h1 * 60 + m1)
print(f'{time // 60}:{time % 60}')
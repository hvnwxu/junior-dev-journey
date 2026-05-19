n = int(input())
c = input()
blank = ' '
tt = n // 2
uu = n // 2 - 1
for i in range(1, n + 1, 2):
    print(tt * blank, end = '')
    print(c * i)
    tt = tt - 1
for j in range(n - 2, 0 - 1, -1):
    if j % 2 != 0:
        print(uu * blank, end = '')
        print(c * j)
        uu = uu + 1
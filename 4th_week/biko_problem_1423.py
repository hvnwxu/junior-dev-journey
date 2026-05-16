n, m = map(int, input().split())
c = int(input())
for _ in range(1, n+1):
    for _ in range(2, m+1):
        print(c, end='')
    print(c)
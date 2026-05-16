n = int(input())
c = input()
time = 1
that = n
for i in range(1, n+1):
    print(c * time)
    time += 1
for _ in range(n):
    that = that - 1
    print(c * that)
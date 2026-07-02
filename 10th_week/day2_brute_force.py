X = []

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

max_heart = 0

for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if i != j and i != k and i != l and j != k and j != l and k != l:
                    jigum_heart = a[i] + b[j] + c[k] + d[l]

                    if jigum_heart > max_heart:
                        max_heart = jigum_heart

print(max_heart)

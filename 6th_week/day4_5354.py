N = int(input())
NN = list(map(int, input().split()))

distance = 0
no_change = 0

for i in range(2 * N):
    change = 0

    for j in range(2 * N):

        if i == j:
            continue
        
        if NN[i] == NN[j]:
            change = j - i - 1
    
    if no_change < change:
        no_change = change
print(no_change)    
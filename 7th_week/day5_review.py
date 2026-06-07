#1. 입력:10
#9 11
#10 14
#8 10
#12 15
#9 11
#11 13
#10 15
#9 10
#8 11
#13 15
#   출력:5
#2. 1,학생수를 입력받고 컴퓨터 사용시간을 리스트로 입력받는다
#   2,반복문을 사용해 각 시간마다 그 시간을 쓰는 학생들을 합한 수중 가장 큰 수를 찾는다
#   3,그 수를 출력한다

n = int(input())

A = [0] * 101
ans = 0

for i in range(n):
    s, e = map(int, input().split())
    for j in range(s, e):
        A[j] = 1 + A[j]

for i in range(n):
    if A[i] > ans:
        ans = A[i]

print(ans)
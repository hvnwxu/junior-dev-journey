#1. 입력:10
#   출력:2 4 6 8 10
#2. 1,한 정수를 입력받는다
#   2,반복문을 사용해 그 정수
n=int(input())
for i in range(1, n+1):
    if i//2!=0 and i%2==0:
        print(i, end=' ')
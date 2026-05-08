#1. 입력:5 10
#   출력:10
#2. 1,두 정수를 입력받는다
#   2,두 정수의 크기를 비교한다
#   3,큰수가 있으면 그 수를 출력하고 두수가 같으면 그 수를 출력한다
a, b=map(int, input().split())
if a>b:
    print(a)
elif a<b:
    print(b)
else:
    print(a)
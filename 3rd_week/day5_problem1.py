#1. 입력:5 10 3
#   출력:10
#2  1,세 정수를 입력받는다
#   2,반목문이랑 if문을 사용해 세 수를 비교한다
a, b, c=map(int, input().split())
if a>b:
    print(a)
elif a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)
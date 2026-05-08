#1. 입력:5 10 3
#   출력:3
#2  1,세 정수를 입력받는다
#   2,if문을 사용해 세 수를 비교하고 작은 값을 출력한다
a, b, c=map(int, input().split())
if a<=b and a<=c:
    print(a)
elif b<=c and b<=a:
    print(b)
else:
    print(c)
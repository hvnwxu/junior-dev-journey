#1. 입력:30241
#   출력:30241
#2  1,정수 m을 입력받는다
#   2,함수를 이용해 m이 10보다 작으면 그대로 return 크면 m의 몪으로 함수를 돌리고 return으로 m의 나머지를 돌려준다
#   3,m을 출력한다



def sum(m):
    
    if m < 10:
        print(m, end='')
    else:
        sum(m // 10)
        print(m % 10, end='')
m = int(input())
sum(m)
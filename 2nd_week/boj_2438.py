#1. 입력:5
#   출력:*
#       **
#       ***
#       ****
#       *****
#2. 정수를 입력받는다
#   반복문을 사용해 받은 정수의 값만큼 한줄씩내려가면서 하나씩 더하면서 별을 출력한다
a=int(input())
number=0
for number in range(a):
    number+=1
    print(number*'*')
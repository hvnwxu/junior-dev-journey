#1. 입력:25
#   출력:good
#2. 1,정수를 입력받는다
#   2,if문을 써서 정수가 어디 사이에있는지 구분한다
#   3,구분한 값을 출력한다
n=int(input())
if n>=0 and n<=500:
    
    if n>=0 and n<=30:
         print('good')
    elif n>=31 and n<=80:
        print('Moderate')
    elif n>=81 and a<=150:
        print('Unhealthy')
    elif n>=151:
        print('Very Unhealthy')
else:
    print('0에서 500사이의 값을 출력해주세요')
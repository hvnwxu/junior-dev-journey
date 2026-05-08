#1. 입력:100
#   출력:A
#2. 시험 점수를 입력받는다
#   받은 점수를 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F로 나눈다
#   그 나눈 값을 출력한다
test_result=int(input())
if test_result>89 and test_result<101:
    print('A')
elif test_result>79 and test_result<90:
    print('B')
elif test_result>69 and test_result<80:
    print('C')
elif test_result>59 and test_result<70:
    print('D')
else:
    print('F')
#3. and 랑 or 이랑 헷갈렸어요

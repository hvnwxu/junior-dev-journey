#1. 입력:OOXXOXXOOO
#   출력:10
#2. 1,ox문제의 결과를 입력받는다
#   2,반복문과 if문을 활용해 가중치를 더한값을 출력한다
result='OOXXOXXOOO'
score=0
total=0
for i in result:
    if i=='O':
        score+=1
        total+=score
    else:
        score=0
print(total)
    
    
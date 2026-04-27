a=int(input())
if a>=0 and a<=100:
    if a>=90 and a<=100:
        print('A')
    elif a>=80 and a<=89:
        print('B')
    elif a>=70 and a<=79:
        print('C')
    elif a>=60 and a<=69:
        print('D')
    else:
        print('F')
else:
    print('0이상 100이하의 값을 입력해주세요')
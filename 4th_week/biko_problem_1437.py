a, b, c = map(int, input().split())
gong = 100
dojec = 50
junsa = 70
gang = a * gong
dojac = dojec *b
junsu = junsa * c
if gang + dojac + junsu >= 370:
    print('win')
else:
    print('lose')
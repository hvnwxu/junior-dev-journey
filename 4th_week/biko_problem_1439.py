a, b, c = map(int, input().split())
gong = 100
dojec = 50
junse = 70
gang = a * gong
dojac = dojec * b
junsu = junse * c
maple = gang + dojac + junsu
if 4 < a + b + c < 6:
    if maple >= 370:
        print('win')
    else:
        print('lose')
else:
    print('team error')
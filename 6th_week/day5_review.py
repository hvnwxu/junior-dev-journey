def f(c):
    if c < 10:
     print(c, end='') 

    else:
        f(c // 10)
        print(c % 10, end='')
    
m = int(input())

f(m)
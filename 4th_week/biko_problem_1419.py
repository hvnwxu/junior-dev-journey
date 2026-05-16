n = int(input())
gold = 0
mad = 0
day = 0
while gold <= n:
    mad += 1
    gold += mad
    day += 1
    if gold >= n:
        break
print(day)
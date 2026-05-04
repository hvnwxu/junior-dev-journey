import sys

"""
입력값의 샘플을 따로 입력받지 않고 배열로 만들어 처리하는 방법
"""
arr_input = {"OOXXOXXOOO","OOXXOOXXOO","OXOXOXOXOXOXOX","OOOOOOOOOO","OOOOXOOOOXOOOOX"}

score = 0
total = 0
for input in arr_input:
    print(f"input :: {input}")
    for char in input:
        if char == "O":
            score += 1
            total += score
        else:
            score = 0
    
    print(total)
    score = 0
    total = 0


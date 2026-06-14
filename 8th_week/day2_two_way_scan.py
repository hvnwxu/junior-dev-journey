scores = [75, 85, 90, 88, 60]
i = 2 # 기준점 (90점)
count = 0

# 1. 왼쪽 스캔 ⬅️
j = i - 1
while j >= 0:
    if scores[j] < 80:   # 80점 미만이면?
        break            # 어떻게 해야 할까?
    count += 1
    j -= 1

# 2. 오른쪽 스캔 ➡️
j = i + 1
while j < len(scores):
    if scores[j] < 80: # 80점 미만이면?
        break            # 어떻게 해야 할까?
    count += 1
    j += 1

print(count)
houses = [25, 3, 9, 14, 11]

# 1단계: 무조건 뭐부터 해야 한다?
houses.sort()

min_distance = float('inf')

# 2단계: 이웃한 집끼리 거리 비교하기
for i in range(len(houses) - 1):
    distance = houses[i + 1] - houses[i]
    if distance < min_distance:
        min_distance = distance
print(min_distance) # 정렬이 잘 되었다면 답은 2(11과 9의 차이)가 나와야 해!
houses = [25, 3, 9, 14, 11]

# 1단계: 무조건 뭐부터 해야 한다?
houses.sort()

min_distance = float('inf')

# ✅ float('inf') 를 초기값으로 쓴 게 아주 좋아.
#    "아직 아무것도 비교 안 했으니 일단 무한대로 시작" 이라는 뜻인데,
#    이렇게 하면 첫 번째 비교에서 무조건 min_distance 가 갱신되거든.
#    앞으로도 최솟값/최댓값을 구할 때 이 패턴 자주 쓰게 될 거야!

# 2단계: 이웃한 집끼리 거리 비교하기
for i in range(len(houses) - 1):
    distance = houses[i + 1] - houses[i]
    if distance < min_distance:
        min_distance = distance
print(min_distance) # 정렬이 잘 되었다면 답은 2(11과 9의 차이)가 나와야 해!

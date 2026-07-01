# 📝 코드 리뷰 (2026-07-02)
# 
# ✅ 잘한 점:
# 1. 정렬 후 양방향 탐색으로 불필요한 비교 제거 (시간 복잡도 개선)
# 2. 원본 인덱스 보존 ([x, s, i] 구조)으로 정렬 후에도 올바른 순서 유지
# 3. 실전 타임어택 완료
#
# ⚠️ 개선 필요:
# 1. [치명적 버그] 49번째 줄: abs(X[j][0] - X[j][0]) → 항상 0 반환! abs(X[j][0] - X[i][0])로 수정 필요
# 2. [구조 문제] 두 문제(친구 찾기 + 수열 정렬)가 한 파일에 섞여 있어 채점 불가
# 3. [비효율] 거리 계산을 3번 반복 → 한 번만 계산해서 재사용
# 4. [가독성] 주석 부족, 변수명 개선 필요 (count → original_idx)

import sys

# ===== 문제 1: 친구 찾기 (KOI 2026 Q1) =====
N, K1, K2 = map(int, sys.stdin.readline().split())

X = []

for i in range(N):
    x, s = map(int, sys.stdin.readline().split())
    X.append([x, s, i])  # [좌표, 학교, 원본_인덱스]

# 좌표 기준 오름차순 정렬 (조기 종료 최적화 위해)
X.sort(key=lambda x: x[0])

# 원본 입력 순서대로 친구 수 저장
friend = [0] * N

# 왼쪽(작은 좌표) 방향 탐색
for i in range(N):
    j = i - 1
    original_idx = X[i][2]  # 정렬 전 원래 인덱스
    while j >= 0:
        dist = abs(X[i][0] - X[j][0])  # ✅ 거리 한 번만 계산
        
        # K2를 넘으면 더 이상 친구 가능성 없음
        if dist > K2:
            break
        
        # 같은 학교: K1 이내만 친구
        if X[i][1] == X[j][1] and dist <= K1:
            friend[original_idx] += 1
        
        # 다른 학교: K2 이내면 무조건 친구
        if X[i][1] != X[j][1]:  # dist <= K2는 이미 확정됨
            friend[original_idx] += 1
        
        j -= 1

# 오른쪽(큰 좌표) 방향 탐색
for i in range(N):
    original_idx = X[i][2]
    j = i + 1
    while j < N:
        dist = abs(X[j][0] - X[i][0])  # ✅ 거리 한 번만 계산
        
        if dist > K2:
            break

        # 같은 학교: K1 이내만 친구
        if X[i][1] == X[j][1] and dist <= K1:
            friend[original_idx] += 1
        
        # 🐛 [버그 수정 필요!]
        # 원래 코드: abs(X[j][0] - X[j][0]) → 항상 0이 나옴
        # 수정 필요: abs(X[j][0] - X[i][0]) 또는 위에서 계산한 dist 사용
        if X[i][1] != X[j][1]:
            friend[original_idx] += 1
        
        j += 1
        
print(*friend)

# ===== 문제 2: 수열 정렬 판단 (KOI 2026 Q2 Subtask) =====
# ⚠️ 실전에서는 별도 파일로 분리해야 채점 가능!
N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

B = sorted(A)

# 이미 정렬되어 있으면 0, 아니면 1 출력
if A == B:
    print(0)
else:
    print(1)

# ===== 다음 주 액션 아이템 =====
# [ ] 1. 49번째 줄 버그 수정 (X[j][0] - X[j][0] → X[j][0] - X[i][0])
# [ ] 2. 문제 1, 2를 별도 파일로 분리 (day1_q1_friends.py, day1_q2_sort.py)
# [ ] 3. 디버그 프린트 추가하여 변수 값 추적 습관화
# [ ] 4. 주석과 변수명 개선한 "클린 코드 버전" 작성
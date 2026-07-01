# 📝 코드 리뷰 (2026-07-02)
#
# ✅ 잘한 점:
# 1. 문제 분석이 명확함 (입력/출력 예시 + 단계별 풀이 계획)
# 2. XOR 누적합 개념을 정확히 파악하고 구현
# 3. 인덱스 범위를 명확히 분리 (0번과 1~N 구분)하여 IndexError 방지
#
# ⚠️ 개선 필요:
# 1. [비효율] elif 조건이 불필요 (위에서 != 검사했으므로 else면 충분)
# 2. [가독성] 변수명 개선 필요 (SA → xor_prefix_a, cnt → diff_count)
# 3. [간결성] Pythonic한 방식으로 카운트 가능 (sum + generator)

#1. 입력:3
#1 2 3
#3 2 1
#   출력:2
#2. 1, 정수N이랑 수열 a,b를 입력받는다
#   2, XOR연산을 사용해 새로운 변수 SA, SB에다가 누적 합을 저장한다
#   3, 누적합의 마지막 숫자가 다르면 -1을 출력하고 같으면 다른 숫자들의 수를 출력한다
import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

# 수열 A의 XOR 누적합 계산
SA = [0] * N  
SA[0] = a[0] 
for i in range(1, N):
    SA[i] = SA[i-1] ^ a[i]

# 수열 B의 XOR 누적합 계산
SB = [0] * N
SB[0] = b[0]
for j in range(1, N):
    SB[j] = SB[j-1] ^ b[j]

# 최종 누적 XOR 값이 다르면 불가능
if SA[-1] != SB[-1]:
    print(-1)
else:
    # ✅ elif 대신 else 사용 (조건 재검사 불필요)
    # 누적합이 다른 위치의 개수 세기
    cnt = 0
    for k in range(N):
        if SA[k] != SB[k]:
            cnt += 1
    print(cnt)
    
    # ✅ [개선 버전] Pythonic한 방식으로 한 줄로 작성 가능:
    # cnt = sum(1 for k in range(N) if SA[k] != SB[k])
    # print(cnt)

# ===== 다음 주 액션 아이템 =====
# [ ] 1. elif → else로 수정하여 불필요한 조건 제거
# [ ] 2. 변수명 개선 (SA → xor_prefix_a, cnt → diff_count)
# [ ] 3. sum + generator 표현식으로 간결하게 리팩토링
# [ ] 4. itertools.accumulate 사용한 함수형 버전 학습해보기
import sys

N, K1, K2 = map(int, sys.stdin.readline().split())

X = []

for i in range(N):
    x, s = map(int, sys.stdin.readline().split())
    X.append([x, s, i])

# ✅ 여기까지 완벽해!
#    집 좌표(x), 성적(s), 원래 번호(i) 를 함께 저장해서
#    정렬 후에도 누가 누구인지 추적할 수 있도록 한 게 핵심 아이디어야.
X.sort(key=lambda x: x[0])

# ⚠️ 여기서 멈췄지? 방향은 맞아. j = i + 1 로 오른쪽을 보는 것도 맞고.
#    다음 단계는 while 루프 안에서 두 가지 조건을 처리하는 거야:
#    1) X[j][0] - X[i][0] 이 너무 크면 → break (더 볼 필요 없음)
#    2) 두 사람의 성적 차이가 K1~K2 사이면 → 정답 처리
#    종이에 예제를 직접 써가며 언제 break하고 언제 세는지 순서를 잡아봐!
for i in range(N):
    j = i + 1

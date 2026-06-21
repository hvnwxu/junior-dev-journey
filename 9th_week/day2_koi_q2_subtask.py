import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = A.copy()
B.sort()
if B == A:
    print(0)
else:
    print(1)

# ✅ 깔끔하고 잘 짰어! 정렬된 결과와 원본을 비교하는 아이디어가 정확해.
#    A.copy()로 원본을 보존한 것도 좋은 습관이야.
#
# 💡 한 가지만 알아두면 좋은 점:
#    sorted()를 쓰면 copy + sort를 한 줄로 줄일 수 있어.
#    예) if sorted(A) == A:  ← 이 한 줄이 B = A.copy() + B.sort() + if B == A 와 같아.
#    지금 코드도 충분히 좋으니까, 나중에 코드를 짧게 쓰고 싶을 때 써봐!
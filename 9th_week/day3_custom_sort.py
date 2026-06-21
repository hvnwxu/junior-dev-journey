N = int(input())
A = []
for _ in range(N):
    i, s, f = map(int, input().split())
    A.append(i, s, f)
    # ⚠️ [버그] day1과 같은 실수! append에는 값을 하나만 넣을 수 있어.
    #    A.append([i, s, f]) 로 리스트로 감싸야 해.
    #    이 한 글자 차이(대괄호)가 프로그램을 실행 못하게 만드니까 꼭 기억해!

A.sort(key=lambda x: x[1])
cnt = 0
ii = []
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if A[i][2] < A[j][1]:
            cnt += 1
            ii.append(A[0])
            # ⚠️ [논리 확인] 여기서 A[0]을 넣고 있는데,
            #    A[0]은 항상 "첫 번째 원소"를 가리켜.
            #    조건에 맞는 i나 j의 데이터를 넣으려면
            #    A[i] 또는 A[j] 가 되어야 하지 않을까?
            #    어떤 값을 결과에 담고 싶은 건지 다시 생각해봐!

print(cnt)
print(*(ii))
# 💡 print(*(ii)) 에서 괄호가 두 겹인데, print(*ii) 로 써도 같은 결과야.
#    *ii 는 리스트를 풀어서 출력하는 거니까 깔끔하게 print(*ii) 로 쓰면 돼.
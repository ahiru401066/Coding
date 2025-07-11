from collections import deque

def main():
    N,M = map(int,input().split())
    S = input()
    C = list(map(int,input().split()))

    # dic = {key: deque() for key in [i for i in range(1,M+1)]}
    L = [deque() for _ in range(M+1)]
    for i in range(N):
        L[C[i]].append(S[i])
    else:
        for i in range(1,M+1):
            tail = L[i].pop()
            L[i].appendleft(tail)
    # print(dic)
    ans = ""
    for i in range(N):
        top = L[C[i]].popleft()
        ans += top
    print(ans)

main()
# インデックスではない
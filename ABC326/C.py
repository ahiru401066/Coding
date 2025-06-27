from collections import deque

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    Q = deque()

    maxThings = 1
    for i in range(N):
        if i == 0: 
            Q.append(A[i])
            continue
        
        Q.append(A[i])
        if not Q[-1] < Q[0] + M:
            Q.popleft()
        maxThings = max(maxThings, len(Q))

    print(maxThings)

main()
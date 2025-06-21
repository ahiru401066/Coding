import sys

def main():
    N = int(input())
    Q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    INF = 10**18
    ans = 0
    for x in range(max(Q) + 1):
        y = INF
        for i in range(N):
            if Q[i] < A[i] * x:
                y = -INF
            elif B[i] > 0:
                y = min(y, (Q[i] - A[i] * x) // B[i])
        ans = max(ans, x + y)
    print(ans)

    # Aのみ
    # maxPeople = 0
    # count = 0
    # while True:
    #     if any(x > q for x,q in zip(X,Q)):
    #         break
    #     X = [X[i]+A[i] for i in range(N)]
    #     count += 1
    #     maxPeople += 1

main()
# 貪欲法？
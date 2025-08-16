def main():
    N,M = map(int,input().split())
    S = input()
    T = input()
    L = []; R = []
    for _ in range(M):
        l,r = map(int,input().split())
        L.append(l); R.append(r)
    
    W = [0] * (N+1)
    for i in range(M):
        W[L[i]-1] += 1
        W[R[i]] -= 1
        # print(W)

    for i in range(N):
        W[i+1] += W[i]
    # print(W)

    ans = []
    for i in range(N):
        if W[i] % 2 == 0: ans.append(S[i])
        else: ans.append(T[i])
    print("".join(ans))
        
    

main()
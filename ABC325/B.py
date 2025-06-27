def main():
    N = int(input())
    W = []; X = []
    for _ in range(N):
        w,x = map(int,input().split())
        W.append(w); X.append(x)
    
    L = [0] * 24 # 0 ~ 1, 1 ~ 2, ...
    for i in range(N):
        for j in range(9+X[i],18+X[i]):
            L[j%24] += W[i]
    print(max(L))

    

main()
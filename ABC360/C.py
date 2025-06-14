def main():
    N = int(input())
    A = list(map(int,input().split()))
    W = list(map(int,input().split()))
    dic = {}
    for i in range(N):
        if not A[i] in dic.keys():
            dic[A[i]] = W[i]
        else:
            dic[A[i]] = max(dic[A[i]],W[i])
    
    V = [v for v in dic.values()]
    # V = dic.values()
    print(sum(W) - sum(V))



main()
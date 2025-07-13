def main():
    def bs(x):
        total = 0
        for k,v in dic.items():
            if k >= x:
                total += v
        if total <= K: return True
        else: return False

    N,K = map(int,input().split())
    dic = {}
    for _ in range(N):
        a,b = map(int,input().split())
        if not a in dic:
            dic[a] = b
        else:
            dic[a] += b
    # print(dic)
    left = 0; right = 10**9+1
    while left + 1 < right:
        mid = (left+right)//2
        if bs(mid): right = mid
        else: left = mid
    print(right)

main()
# ２分探索
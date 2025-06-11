import sys
sys.setrecursionlimit(120000)

def main():
    def rec(n,li):
        if n == N:
            if sum(li) % K == 0:
                print(*li)
            return 
        
        for i in range(1,R[n]+1):
            rec(n+1,li+[i])
        return 

    N,K = map(int,input().split())
    R = list(map(int,input().split()))

    rec(0,[])

main()
# 全組み合わせを調べる必要がある、、
# 実装がわからない、、n回のforループ
# 再帰
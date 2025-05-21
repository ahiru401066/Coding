def main():
    def compare(s,t):
        for i in range(m):
            for j in range(m):
                if s[i][j] != t[i][j]: return False
        return True
    
    def sList(i,j):
        s = []
        for k in range(i,i+m):
            s.append(S[k][j:j+m])
        return s
            

    n, m = map(int, input().split())
    S = [input() for _ in range(n)]
    T = [input() for _ in range(m)]

    for i in range(n-m+1):
        for j in range(n-m+1):
            s = sList(i,j)
            flg = compare(s,T)
            if flg: print(i+1,j+1); return

main()
# 総当たり 右と下に注意
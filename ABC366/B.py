def main():
    n = int(input())
    S = [list(input()) for _ in range(n)]
    l = 0
    for i in range(n):
        if i == 0: l = len(S[i])
        else:
            if l > len(S[i]):
                # S[i].append("*" * (l - len(S[i])))
                while len(S[i]) < l:
                    S[i].append("*")
            else:
                l = len(S[i])
    
    for i in range(len(S[-1])):
        o = ""
        for j in range(len(S)):
            if i > len(S[n-j-1])-1:
                break
            o += S[n-j-1][i]
        print(o)

main()
# 入力受け取り + 空白補填
# 縦 -> 横
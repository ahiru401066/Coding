def main():
    N,M = map(int,input().split())
    S = [input() for _ in range(N)]
    
    minStore = 10
    for bit in range(1 << N):
        txt = ""
        for i in range(N):
            if bit & (1 << i):
               txt += "1"
            else:
               txt += "0"
        
        s = ["x"] * M
        for i in range(len(txt)):
            if txt[i] == "1":
                for j in range(M):
                    if s[j] == "o" or S[i][j] == "o":
                        s[j] = "o"

        if "".join(s) == "o"*M:
            store = sum(1 for i in range(len(txt)) if txt[i] == "1")
            minStore = min(minStore,store)
    print(minStore)

main()
# 全探索
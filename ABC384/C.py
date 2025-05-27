def main():
    # a,b,c,d,e = map(int,input().split())
    A = list(map(int,input().split()))
    B = ["A","B","C","D","E"]
    li = []
    
    for bit in range(1 << 5):
        if bit == 0: continue
        pattern = [0,""]
        for i in range(5):
            if bit & (1 << i):
                pattern[0] += A[i]
                pattern[1] += B[i]
        li.append(pattern)
    fixPattern = sorted(li, key=lambda x: (-x[0],x[1]),reverse=False)
    for i in range(len(fixPattern)):
        print(fixPattern[i][1])

main()
# ビット全探索？
# 得点と問題文字列を持つ
def main():
    W,B = map(int,input().split())
    S = "wbwbwwbwbwbw"*100
    for i in range(len(S)-(W+B-1)):
        txt = (S[i:i+(W+B)])
        w = 0; b = 0
        for j in range(len(txt)):
            if txt[j] == "w": w += 1
            else: b += 1
        if w == W and b == B:
            print("Yes")
            return
    print("No")

main()
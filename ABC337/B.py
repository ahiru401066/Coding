def main():
    S = input()
    F = set(["BA","CA","CB"])
    for i in range(len(S)-1):
        txt = S[i] + S[i+1]
        if txt in F: 
            print("No")
            return
    print("Yes")

main()
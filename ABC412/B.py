def main():
    S = input()
    T = input()

    txt = ""
    for i in range(1,len(S)):
        if S[i].isupper():
            txt += S[i-1]

    for t in txt:
        if not t in list(T):
            print("No")
            return 
    print("Yes")

main()
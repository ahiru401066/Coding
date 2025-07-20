def main():
    S = input()

    l = []
    for i in range(len(S)):
        if S[i] == "#":
            l.append(str(i+1))
        
        if len(l) == 2:
            txt = ",".join(l)
            print(txt)
            l = []

main()
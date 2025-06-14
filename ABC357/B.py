def main():
    S = input()
    l = 0; u = 0
    for i in range(len(S)):
        if S[i].islower(): l += 1
        else: u += 1
    
    if l > u: print(S.lower())
    else: print(S.upper())


main()
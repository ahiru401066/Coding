def main():
    S = input()
    N = len(S)
    L = [True] * N

    for i in range(N):
        if i == 0 or i == 1: continue

        if S[i] == "C":
            c = 1
            j = i-1; b = 0
            while j >= 0:
                if L[j] == False:
                    j -= 1
                    continue

                if S[j] == "B":
                    if c == 1:
                        c += 1
                        b = j
                    else: break

                elif S[j] == "A":
                    if c == 2:
                        L[i] = False
                        L[b] = False
                        L[j] = False     
                    break

                j -= 1
    ans = ""
    for i in range(len(L)):
        if L[i]: ans += S[i]
    print(ans)

main()
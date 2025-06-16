def main():
    S = input()
    T = input()

    L = []
    l = 0; k = 0
    while l < len(S) and k < len(T):
        if S[l] == T[k]:
            L.append(k+1)
            l += 1
        k += 1
    print(*L)

main()
def main():
    N = int(input())
    S = []; A = []
    for _ in range(N):
        s,a = input().split()
        S.append(s)
        A.append(int(a))
    
    p = A.index(min(A))

    k = 1
    while k <= N:
        p %= N
        print(S[p])
        p += 1
        k += 1

main()
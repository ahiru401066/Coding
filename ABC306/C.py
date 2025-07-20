def main():
    N = int(input())
    A = list(map(int,input().split()))
    I = [0] * (N+1)
    L = []

    for i in range(len(A)):
        I[A[i]] += 1

        if I[A[i]] == 2:
            L.append([A[i],i+1])

    L.sort(key=lambda x:x[1])
    # print(L)
    result = [x[0] for x in L]
    print(*result)

main()
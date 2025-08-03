def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [i + A[i] for i in range(N)]
    C = [j - A[j] for j in range(N)]

    dicB = {}
    for i in range(N):
        if not B[i] in dicB: dicB[B[i]] = 1
        else: dicB[B[i]] += 1
    # print(dicB)
    # for i in range(N):
    #     dicB[B[i]] = dicB.get(B[i],0) + 1

    dicC = {}
    for i in range(N):
        if not C[i] in dicC: dicC[C[i]] = 1
        else: dicC[C[i]] += 1
    # print(dicC)

    count = 0
    keys = set(list(dicB.keys()) + list(dicC.keys()))
    for k in keys:
        if k in dicB and k in dicC:
            count += dicB[k] * dicC[k]
    print(count)

main()
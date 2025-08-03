from collections import Counter

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [i + A[i] for i in range(N)]
    C = [j - A[j] for j in range(N)]

    dicB = Counter(B)
    dicC = Counter(C)

    count = 0
    for k in dicB.keys():
        for j in dicC.keys():
            if k == j:
                count += dicB[k] * dicC[j]
    print(count)

main()
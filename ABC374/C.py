def main():
    n = int(input())
    K = list(map(int,input().split()))

    maxRecord = 10 ** 10
    for bit in range(1 << n):
        A = 0
        B = 0
        for i in range(n):
            if bit & (1 << i): A += K[i]
            else: B += K[i]
        maxRecord = min(maxRecord, max(A,B))
    print(maxRecord)


main()
# ビット全探索
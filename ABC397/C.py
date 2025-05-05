def main():
    n = int(input())
    a = list(map(int, input().split()))

    left = [0] * n
    seenLeft = set()
    for i in range(n):
        seenLeft.add(a[i])
        left[i] = len(seenLeft)

    right = [0] * n
    seenRight = set()
    for i in reversed(range(n)):
        seenRight.add(a[i])
        right[i] = len(seenRight)
    
    maxCount = 0
    for i in range(n-1):
        maxCount = max(maxCount, left[i] + right[i+1])
    print(maxCount)

main()
# 切れ込みの位置は全探索
# 集合の種類数の計算で工夫？
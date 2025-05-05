def main():
    n = int(input())
    a = list(map(int, input().split()))

    left = [0] * (n-1)
    seenLeft = set()
    for i in range(len(a)-1):
        seenLeft.add(a[i])
        left[i] = len(seenLeft)
    
    right = [0] * (n-1)
    seenRight = set()
    for i in range(len(a)-1):
        seenRight.add(a[n-i-1])
        right[i] = len(seenRight)

    maxCount = 0
    for i in range(len(left)):
        maxCount = max(maxCount, left[i] + right[len(left)-i-1])
    print(maxCount)

main()
def main():
    n = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    maxA = max(A)
    maxB = max(B)
    print(maxA + maxB)


main()
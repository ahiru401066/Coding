def main():
    N = int(input())
    A = list(map(int,input().split()))

    count = 0
    for i in range(N):
        if A[i] + count <= 0: count = 0
        else: count += A[i]
    print(count)


main()
def main():
    n = int(input())
    A = list(map(int, input().split()))

    for i in range(n-1):
        if not A[i+1] > A[i]:
            print("No")
            return
    print("Yes")

main()
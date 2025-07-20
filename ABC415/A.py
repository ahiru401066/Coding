def main():
    N = int(input())
    A = list(map(int,input().split()))
    X = int(input())

    for i in range(N):
        if A[i] == X:
            print("Yes")
            return
    print("No")

main()
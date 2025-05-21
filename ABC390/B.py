def main():
    n = int(input())
    A = list(map(int,input().split()))
    if len(A) == 2:
        print("Yes")
        return

    for i in range(len(A)-2):
        if not A[i] * A[i+2] == A[i+1] * A[i+1]:
            print("No")
            return
    print("Yes")

main()
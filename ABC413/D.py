def main():
    T =int(input())
    N = []
    LA = []
    for _ in range(T):
        n = int(input())
        A = sorted(list(map(int,input().split())))
        N.append(n); LA.append(A)

    for i in range(T):
        n = N[i]; A = LA[i]
        k = 0
        mid = len(A)//2; pre = A[0] * A[-1]
        while k < mid+1:
            if A[k] * A[len(A)-(k+1)] != pre:
                print("No")
                break
            k += 1
        else: print("Yes")

main()
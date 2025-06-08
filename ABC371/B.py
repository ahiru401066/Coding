def main():
    n,m = map(int,input().split())
    L = [True] * n
    A = []; B = []
    for i in range(m):
        a,b = input().split()
        A.append(a)
        B.append(b)

    for i in range(m):
        if B[i] == "F":
            print("No")
        elif L[int(A[i])-1]:
            print("Yes")
            L[int(A[i])-1] = False
        else:
            print("No")

main()

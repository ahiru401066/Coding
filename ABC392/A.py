def main():
    A = list(map(int,input().split()))
    li = [(0,1,2),(0,2,1),(1,2,0)]

    for i,j,k in li:
        if A[i] * A[j] == A[k]:
            print("Yes")
            return
    print("No")

main()
def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    A = [[A[i],"A"] for i in range(N)]
    B = [[B[i],"B"] for i in range(M)]
    
    C = A+B
    C.sort(key=lambda x:x[0])
   
   
    for i in range(N+M-1):
        if C[i][1] == "A" and C[i+1][1] == "A":
            print("Yes")
            return
    print("No")


main()
# マージソート的な？
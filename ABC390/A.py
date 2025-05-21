def main():
    A = list(map(int, input().split()))
    li = [(1,0,2,3,4),(0,2,1,3,4),(0,1,3,2,4),(0,1,2,4,3)]
    for i,j,k,l,m in li:
        if A[i] < A[j] and A[j] < A[k] and A[k] < A[l] and A[l] < A[m]:
            print("Yes"); return
    print("No")            

main()
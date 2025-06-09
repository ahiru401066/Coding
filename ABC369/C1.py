def main():
    n = int(input())
    A = list(map(int,input().split()))
    if n == 1:
        print(1)
        return
    
    B = []
    for i in range(n-1):
        B.append(A[i+1]-A[i])
    
    total = 0
    l = 1
    for i in range(len(B)-1):
        if B[i] == B[i+1]:
            l += 1
        else:
            total += l*(l+1)//2
            l = 1
    total += l*(l+1)//2

    print(total + n)

main()
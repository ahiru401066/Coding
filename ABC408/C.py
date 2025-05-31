def main():
    n,m = map(int,input().split())
    A = [0] * (n+2)
    for _ in range(m):
        l,r = map(int,input().split())
        A[l] += 1
        A[r+1] -= 1
    
    v = A[0]
    for i in range(len(A)):
        if i == 0: continue
        A[i] += v
        v = A[i]

    x = 10**6
    for i in range(1,n+1):
        x = min(x,A[i])
    print(x)
    # print(A)

main()
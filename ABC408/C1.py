def main():
    n,m = map(int,input().split())
    A = [0] * (n+2)
    for _ in range(m):
        l,r = map(int,input().split())
        A[l] += 1
        A[r+1] -= 1

    for i in range(len(A)):
        if i == 0: continue
        A[i] += A[i-1]

    m = min(A[1:n+1])
    print(m)
    

main()
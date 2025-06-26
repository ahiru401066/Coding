def main():
    N = int(input())
    A = list(map(int,input().split()))

    total = sum(A)
    R = [0] * (10**6+1)
    for a in A:
        R[a] += a 
    
    for i in range(1,len(R)):
        R[i] += R[i-1]

    print(*[total - R[a] for a in A])

main()
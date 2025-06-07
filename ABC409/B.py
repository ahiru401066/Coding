def main():
    n = int(input())
    A = list(map(int,input().split()))
    maxEle = 0
    for i in range(1,n+1):
        count = 0
        for j in range(n):
            if A[j] >= i:
                count += 1
        if count >= i and maxEle < i: 
            maxEle = i
    print(maxEle)

main()
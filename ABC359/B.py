def main():
    n = int(input())
    A = list(map(int,input().split()))

    count = 0
    for i in range(len(A)):
        if i == 0 or i == len(A)-1: continue
        if A[i-1] == A[i+1]: count += 1
    print(count)

main()
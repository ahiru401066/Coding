def main():
    N = int(input())
    A = list(map(int,input().split()))
    minV = min(A)
    maxV = max(A)
    for i in range(minV,maxV+1):
        if not i in A:
            print(i)
            return
    if minV == 1: print(maxV+1)
    else: print(minV-1)

main()
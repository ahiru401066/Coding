def main():
    n = int(input())
    A = list(map(int,input().split()))

    total = 0
    l = 1; dis = 0
    for i in range(n-1):
        if i == 0:
            dis = A[i+1] - A[i]
            l += 1
            continue
        
        if A[i] + dis == A[i+1]:
            l += 1
        elif A[i] + dis != A[i+1]:
            total += calc(l)-1
            dis = A[i+1] - A[i]
            l = 2

    total += calc(l)
    print(total)

def calc(l):
    return l*(l+1)//2

main()
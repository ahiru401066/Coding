def main():
    n = int(input())
    A = list(map(int,input().split()))

    count = 0
    while True:
        A.sort(reverse=True)
        A[0] -= 1
        A[1] -= 1
        count += 1
        # c = 0
        # for i in range(n):
        #     if A[i] > 0: c+= 1
        # if c <= 1:
        #     break
        c = sum(1 for i in range(n) if A[i] > 0)
        if c <= 1: break
            
    print(count)

main()
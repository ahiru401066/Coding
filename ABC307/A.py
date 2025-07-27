def main():
    N = int(input())
    A = list(map(int,input().split()))
    li = []
    count = 0
    for i in range(len(A)):
        count += A[i]

        if (i+1) % 7 == 0:
            li.append(count)
            count = 0
    print(*li)

main()
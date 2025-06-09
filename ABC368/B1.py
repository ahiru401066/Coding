def main():
    n = int(input())
    A = list(map(int,input().split()))

    count = 0
    while sum(1 for x in A if x > 0) > 1:
        A.sort(reverse=True)
        A[0] -= 1
        A[1] -= 1
        count += 1
    print(count)

main()
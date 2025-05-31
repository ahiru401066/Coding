def main():
    n = int(input())
    A = list(map(int,input().split()))
    li = [0] * 101
    for i in range(len(A)):
        li[A[i]] += 1
    ans = []
    for i in range(len(li)):
        if li[i] != 0: ans.append(i)
    print(len(ans))
    print(*ans)


main()
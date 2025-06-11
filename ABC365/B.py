def main():
    li = []
    n = int(input())
    A = list(map(int,input().split()))
    for i in range(n):
        li.append([A[i],i])

    li.sort(key=lambda x:x[0],reverse=True)
    print(li[1][1]+1)


main()
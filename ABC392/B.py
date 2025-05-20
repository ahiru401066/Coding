def main():
    n,m = map(int,input().split())
    A = set(map(int,input().split()))
    li = []

    for i in range(1,n+1):
        if not i in A:
            li.append(i)
    print(len(li))
    print(*li)
main()
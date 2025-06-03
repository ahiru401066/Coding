def main():
    n,c = map(int,input().split())
    T = list(map(int,input().split()))

    count = 0
    get = 0
    for i in range(len(T)):
        if i == 0: get = T[i]; count += 1
        else:
            if T[i] - get >= c:
                count += 1
                get = T[i]
    print(count)

main()
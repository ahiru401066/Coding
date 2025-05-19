def main():
    n,m,q = map(int, input().split())
    all = [False] * (n+1)
    users = [set() for i in range(n+1)]

    for i in range(q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            _, x, y = query
            users[x].add(y)
        elif query[0] == 2:
            _, x = query
            all[x] = True
        else:
            _,x,y = query
            if all[x] or y in users[x]: print("Yes")
            else: print("No")

main()
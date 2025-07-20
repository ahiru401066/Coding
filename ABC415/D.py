def main():
    N,M = map(int,input().split())
    AB = []
    for _ in range(M):
        a,b = map(int,input().split())
        AB.append([a,b])
    AB.sort(key=lambda x:x[0] - x[1])
    # print(AB)

    cola = N
    empty = 0
    ans = 0

    while True:
        empty += cola
        cola = 0

        while True:
            used = False
            for a,b in AB:
                if empty < a:
                    continue
                times = empty // a
                if times == 0:
                    continue
                empty -= a * times
                cola += b * times
                ans += times
                used = True
            if not used:
                break

        if cola == 0:
            break

    print(ans)
    
main()
# シュミュレーションできるけど...
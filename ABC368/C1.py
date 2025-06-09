def main():
    n = int(input())
    H = list(map(int,input().split()))

    t = 0
    for h in H:
        n = h // 5
        t += n * 3
        h %= 5

        while h > 0:
            t += 1
            if t % 3 == 0:
                h -= 3
            else:
                h -= 1

    print(t)

main()
def main():
    n, l = map(int,input().split())
    D = list(map(int,input().split()))
    li = [0] * l
    if l % 3 != 0: print(0); return

    pre = 0
    li[0] = 1
    for i in range(n-1):
        x = ((pre + D[i]) % l)
        li[x] += 1
        pre = x

    total = 0
    for i in range(l//3):
        total += li[i] * li[i+(l//3)] * li[i+(l//3)*2]
    print(total)


main()
# あまり
def main():
    n,s = map(int,input().split())
    T = list(map(int,input().split()))

    s += 0.5
    pre = 0
    for i in range(len(T)):
        if T[i] - pre > s:
            print("No"); return
        else:
            pre = T[i]
    print("Yes")

main()
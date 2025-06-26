def main():
    N,L,R = map(int,input().split())
    A = list(map(int,input().split()))
    
    li = []
    for a in A:
        if L <= a <= R: li.append(a)
        elif a < L: li.append(L)
        else: li.append(R)

    print(*li)

main()
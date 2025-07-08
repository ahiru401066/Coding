def main():
    N,D,P = map(int,input().split())
    F = list(map(int,input().split()))
    F.sort(reverse=True)

    total = 0; li = []
    for i in range(len(F)):
        li.append(F[i])
        if len(li) == D:
            cost = P if sum(li) > P else sum(li)
            total += cost
            li = []
            # total += min(sum(li),P)
            # li = []
    else:
        total += P if sum(li) > P else sum(li)
        # total += min(sum(li),P)
        
    print(total)

main()
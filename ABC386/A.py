def main():
    A = list(map(int,input().split()))
    dic = {}
    for a in A:
        if not a in dic.keys():
            dic[a] = 1
        else: dic[a] += 1
    
    count = 0
    for v in dic.values():
        if v == 3:
            print("Yes"); return
        elif v == 2: count += 1
    if count == 2: print("Yes")
    else: print("No")


main()
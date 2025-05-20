def main():
    A = list(map(int, input().split()))
    dic = {} #種類と枚数の保持
    for a in A:
        if not a in dic.keys():
            dic[a] = 1
        else: dic[a] += 1

    count3 = 0; count2 = 0
    for v in dic.values():
        if v >= 3: count3 += 1
        elif v >= 2: count2 += 1
    
    if count3 >= 2: print("Yes")
    elif count3 >= 1 and count2 >= 1: print("Yes")
    else: print("No")

main()
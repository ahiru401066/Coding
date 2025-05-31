def main():
    n = int(input())
    l = calc(n)
    dic = {}
    for e in l:
        if  not e in dic.keys():
            dic[e] = 1
        else: dic[e] += 1
    # print(dic)
    for k,v in dic.items():
        if k == 1 and not v == 1:
            print("No"); return
        if k == 2 and not v == 2:
            print("No"); return 
        if k == 3 and not v == 3:
            print("No"); return
        elif k != 1 and k != 2 and k != 3:
            print("No"); return
    print("Yes")

def calc(n):
    li = []
    while n // 10 != 0:
        li.append(n % 10)
        n //= 10
    li.append(n)
    return li

main()
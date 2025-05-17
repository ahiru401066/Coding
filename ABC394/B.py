def main():
    n = int(input())
    dic = {}
    for _ in range(n):
        s = input()
        dic[s] = len(s)

    sortedDic = sorted(dic.items(), key=lambda x: x[1])
    sortedDic = dict(sortedDic)
    # print(sortedDic)

    ans = ""
    for key in sortedDic.keys():
        ans += key
    print(ans)

main()
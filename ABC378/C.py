def main():
    n = int(input())
    A = list(map(int,input().split()))
    dic = {}
    ans = []
    for i in range(n):
        if not A[i] in dic.keys():
            dic[A[i]] = i+1
            ans.append(-1)
        else:
            ans.append(dic[A[i]])
            dic[A[i]] = i+1
    print(*ans)

main()

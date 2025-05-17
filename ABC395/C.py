def main():
    n = int(input())
    A = list(map(int, input().split()))

    dic = {}
    minLength = n+1
    for i in range(len(A)):
        if A[i] in dic.keys():
            length = i - dic[A[i]] + 1
            minLength = min(minLength, length)
        dic[A[i]] = i
    
    if minLength == n+1: print(-1)
    else:print(minLength)

main()

# おそらくO(n)で行ける
# 同じ数字で囲まれる区間のうち、最も短い区間を見つける

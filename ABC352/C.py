def main():
    N = int(input())
    li = []
    for i in range(N):
        a,b = map(int,input().split())
        li.append([a,b-a])
    li.sort(key=lambda x:x[1])

    ans = 0
    for i in range(N):
        ans += li[i][0]
    ans += li[-1][1]
    print(ans)


main()
# 肩から頭までの長さ　でソート？
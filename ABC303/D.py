def main():
    X,Y,Z = map(int,input().split())
    S = input()
    INF = 10**18
    dp = [[INF,INF] for _ in range(len(S))] # 0:on, 1:off
    # print(dp)

    for i in range(len(S)):
        if i == 0:
            if S[i] == "a":
                dp[0][0] = min(Z+Y,X+Z)
                dp[0][1] = min(X,Z+Y+Z)
            elif S[i] == "A":
                dp[0][0] = min(Y+Z,Z+X)
                dp[0][1] = min(Y,Z+X+Z)
            continue
        
        if S[i] == "a":
            dp[i][0] = min(dp[i-1][0]+Y, dp[i-1][1]+X+Z)
            dp[i][1] = min(dp[i-1][0]+Y+Z, dp[i-1][1]+X)
        
        if S[i] == "A":
            dp[i][0] = min(dp[i-1][0]+X,dp[i-1][1]+Z+Y)
            dp[i][1] = min(dp[i-1][0]+X+Z, dp[i-1][1]+Y)
    # print(dp)
    print(min(dp[-1]))


main()
# 貪欲? <- ダメそう...
# DPだと思う...
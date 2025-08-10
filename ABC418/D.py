def main():
    N = int(input())
    T = input()

    dp = [[0] * (N+1) for _ in range(2)]
    dp[0][0] = 0; dp[1][0] = 0
    for i in range(N):
        if T[i] == "0":
            dp[0][i+1] = dp[1][i]
            dp[1][i+1] = dp[0][i] + 1
        elif T[i] == "1":
            dp[0][i+1] = dp[0][i] + 1
            dp[1][i+1] = dp[1][i]
    
    # print(dp)
    print(sum(dp[0][i] for i in range(N+1)))

main()

# 方向性：0の偶奇で判定

# DPっぽい...
# 1 only
# 1は何個あってもいい
# 00にして0を消すのがポイント
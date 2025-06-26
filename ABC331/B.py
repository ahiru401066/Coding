def main():
    N,S,M,L = map(int,input().split())
    cost = 10**8

    for i in range(18):
        for j in range(14):
            for k in range(10):
                if 6*i + 8*j + 12*k >= N:
                    cost = min(cost, S*i+M*j+L*k)
    print(cost)

main()
# 全探索
def main():
    N = int(input())
    X = 0; Y = 0
    for _ in range(N):
        x,y = map(int,input().split())
        X += x; Y += y 
    if X > Y: print("Takahashi")
    elif Y > X: print("Aoki")
    else: print("Draw")

    # X = []; Y = []
    # for _ in range(N):
    #     x,y = map(int,input().split())
    #     X.append(x)
    #     Y.append(y)

    # xSum = sum(X)
    # ySum = sum(Y)
    # if xSum > ySum: print("Takahashi")
    # elif ySum > xSum: print("Aoki")
    # else: print("Draw")

main()
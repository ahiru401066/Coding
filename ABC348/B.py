import math

def main():
    N = int(input())
    X = []; Y = []
    for _ in range(N):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)

    for i in range(N):
        maxNum = 0; index = 1000
        for j in range(N):
            dis = math.sqrt((X[i] - X[j])**2 + (Y[i] - Y[j])**2)
            if dis > maxNum:
                maxNum = dis
                index = j+1
        print(index)

    # for i in range(N):
    #     maxNum = 0; index = 1000
    #     for j in range(N-1,-1,-1):
    #         if math.sqrt((X[i] - X[j])**2 + (Y[i] - Y[j])**2) >= maxNum:
    #             maxNum = math.sqrt((X[i] - X[j])**2 + (Y[i] - Y[j])**2)
    #             index = j+1
    #     print(index)

main()
def main():
    N,M = map(int,input().split())
    D = []
    for _ in range(N):
        data = list(map(int,input().split()))
        D.append([data[0],set(data[2:])])
    D.sort(key=lambda x:x[0],reverse=True)
    
    # print(D)

    for i in range(N):
        for j in range(i+1,N):
            if not D[i][0] >= D[j][0]:
                continue
            
            if not D[i][1] <= D[j][1]:
                continue

            if not (D[i][0] > D[j][0] or len(D[j][1] - D[i][1]) >= 1):
                continue
                
            print("Yes")
            return
    print("No")

main()
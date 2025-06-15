def main():
    N, T = map(int,input().split())
    A = list(map(lambda x:int(x)-1,input().split()))
    row = [0] * N
    col = [0] * N
    diag = [0] * 2

    for i in range(T):
        x = A[i] // N
        y = A[i] % N

        row[x] += 1
        if row[x] == N:
            print(i+1)
            return

        col[y] += 1
        if col[y] == N:
            print(i+1)
            return
        
        if x == y:
            diag[0] += 1
            if diag[0] == N:
                print(i+1)
                return
        
        if x+y == N-1:
            diag[1] += 1
            if diag[1] == N:
                print(i+1)
                return
    print(-1)

main()
# 最低限のビンゴチェック
# 各マスの状態の持ち方とビンゴチェックがわからない
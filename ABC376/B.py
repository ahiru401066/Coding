def main():
    n,q = map(int,input().split())
    H = []; T = []
    for _ in range(q):
        query = list(input().split())
        H.append(query[0])
        T.append(int(query[1]))

    l = 1; r = 2
    count = 0
    for i in range(q):
        if H[i] == "L":
            if T[i] > l and T[i] > r > l: count += (n-T[i]+1) + l-1; l = T[i]
            elif T[i] > l: count += T[i] - l; l = T[i]
            elif T[i] < l and T[i] < r < l: count += (n-l+1) + T[i]-1; l = T[i]
            elif T[i] < l: count += l - T[i]; l = T[i]
        elif H[i] == "R":
            if T[i] > r and T[i] > l > r: count += (n-T[i]+1) + r-1; r = T[i]
            elif T[i] > r: count += T[i] - r; r = T[i]
            elif T[i] < r and T[i] < l < r: count += (n-r+1) + T[i]-1; r = T[i]
            elif T[i] < r: count += r - T[i]; r = T[i]
    print(count)

main()
# 迂回場合の処理を書く
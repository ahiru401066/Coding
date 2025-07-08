def main():
    def calc(mid):
        count = M
        length = 0; c = 0
        while c < N:
            # 追加
            padding = 0 if length == 0 else 1
            length += padding+L[c]

            # 改行判定
            if length > mid:
                count -= 1
                length = 0
                c -= 1 # 要素を次の行に入れる
            
            # 縦行判定
            if count == 0:
                return False

            c += 1
        return True

    N,M = map(int,input().split())
    L = list(map(int,input().split()))

    left = -1; right = 10**9 * 2*10**5 
    right = 10**9 + (10**9+1) * (2*10**5-1)
    while left + 1 < right:
        mid = (left+right)//2
        if calc(mid): right = mid
        else: left = mid
    print(right)

main()
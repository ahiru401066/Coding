def main():
    N,M,K = map(int,input().split())
    tests = []
    for _ in range(M):
        parts = input().split()
        C = int(parts[0])
        A = list(map(int,parts[1:-1]))
        R = parts[-1]
        tests.append((A,R))
    
    ans = 0
        # print(tests)

    for bit in range(1 << N):
        ok = True

        for A,R in tests:
            count = sum((bit >> key - 1) & 1 for key in A)

            if R == "o" and count < K:
                ok = False
                break

            if R == "x" and count >= K:
                ok = False
                break
        
        if ok: ans += 1

    print(ans)
    

main()
# 鍵の組みわせ全探索
# 全体から矛盾するものを引く or 矛盾しないものを求める
# 4パターン？ 

# 悩み：ダミーか本物か最後まで判断できなさそうに見える
# 入力受け取りめんどくさ
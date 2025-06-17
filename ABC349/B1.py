def main():
    S = input()
    cnt = [0] * 26
    for c in S:
        cnt[ord(c) - ord("a")] += 1 #ポイント1

    cnt2 = [0] * 101
    for c in cnt:
        if c > 0:
            cnt2[c] += 1
    
    print("Yes" if all(c in (0,2) for c in cnt2) else "No") #ポイント2


main()
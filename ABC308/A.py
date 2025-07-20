def main():
    S = list(map(int,input().split()))

    for i in range(len(S)-1):
        if not S[i] <= S[i+1]:
            print("No")
            return
    
    if sum(1 for s in S if not 100 <= s <= 675) >= 1:
        print("No")
        return
    
    if sum(1 for s in S if s % 25 != 0) >= 1:
        print("No")
        return

    print("Yes")

main()
def main():
    N,M = map(int,input().split())
    S = input()
    T = input()

    flg1 = S == T[:N]
    flg2 = S[::-1] == T[::-1][:N]
    # flg2 = S == T[-N:]

    if flg1 and flg2: print(0)
    elif flg1 and not flg2: print(1)
    elif not flg1 and flg2: print(2)
    else: print(3)
    

main()
def main():
    N = int(input())
    S = input()
    Q = int(input())
    L = [list(input().split()) for _ in range(Q)]
    txt = list(S)

    change = "1"; changeFlg = 0
    for i in range(Q):
        t,x,c = L[i]
        x = int(x)
        if t == "1":
            txt[x-1] = c
        elif t == "2":
            change = "2"
            changeFlg = i
        else:
            change = "3"
            changeFlg = i
    
    ans = "".join(txt)
    if change == "1": pass
    elif change == "2": ans = ans.lower()
    else: ans = ans.upper()

    txt = list(ans)
    for i in range(changeFlg+1,Q):
        t,x,c = L[i]
        x = int(x)
        txt[x-1] = c
    ans = "".join(txt)
    print(ans)

main()
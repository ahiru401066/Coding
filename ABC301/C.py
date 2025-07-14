def main():
    S = input()
    T = input()
    N = len(S)
    keys = list("abcdefghijklmnopqrstuvwxyz@")
    dicS = {key: 0 for key in keys}
    dicT = {key: 0 for key in keys}
    for i in range(N):
        dicS[S[i]] += 1
        dicT[T[i]] += 1
    special = list("atcoder")
    # print(dicS)
    # print(dicT)

    # S -> T 
    w = 0
    for i in range(N):
        if T[i] == "@":
            w += 1
            
        elif not T[i] in special:
            dicS[T[i]] -= 1
            if dicS[T[i]] < 0:
                print("No")
                return
        
        else:
            if dicS[T[i]] > 0:
                dicS[T[i]] -= 1
            else:
                dicS["@"] -= 1
                if dicS["@"] < 0:
                    print("No")
                    return
                
    total = sum(dicS[k] for k in special+["@"])
    if total != w:
        print("No")
        return

    # T -> S
    w = 0
    for i in range(N):
        if S[i] == "@":
            w += 1
            
        elif not S[i] in special:
            dicT[S[i]] -= 1
            if dicT[S[i]] < 0:
                print("No")
                return
        
        else:
            if dicT[S[i]] > 0:
                dicT[S[i]] -= 1
            else:
                dicT["@"] -= 1
                if dicT["@"] < 0:
                    print("No")
                    return
                
    total = sum(dicT[k] for k in special+["@"])
    if total != w:
        print("No")
        return
            
    print("Yes")

main()
# 順番は関係ない
# 一方が合わせられればもう一方も合わせられる？ No
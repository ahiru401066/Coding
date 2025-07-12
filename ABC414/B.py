def main():
    N = int(input())
    C = []; L = []
    for _ in range(N):
        c,l = input().split()
        C.append(c)
        L.append(int(l))
    
    ans = ""
    for i in range(N):
        if L[i] > 100:
            print("Too Long")
            return
        if len(ans) > 100:
            print("Too Long")
            return
    
        ans += C[i] * L[i]
    
    if len(ans) > 100:
        print("Too Long")
    else:
        print(ans)

main()
def main():
    N = int(input())
    L = []
    for i in range(1,10):
        if N % i == 0: L.append(i)
    
    ans = ""
    for i in range(N+1):
        for l in L:
            if i % (N//l) == 0:
                ans += str(l)
                break
        else:
            ans += "-"
    print(ans)

main()
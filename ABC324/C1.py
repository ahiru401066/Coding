def main():
    N,T = input().split()
    N = int(N)
    S = [input() for _ in range(N)]

    ans = []
    for i in range(N):
        s = S[i]
        if len(T) == len(s):
            err = 0
            k = 0
            while k < len(T):
                if s[k] != T[k]: err += 1
                k += 1
            if err <= 1: ans.append(i+1)

        elif abs(len(T) - len(s)) == 1:
            long = T if len(T) > len(s) else s 
            short = T if len(T) < len(s) else s

            err = 0; x=0; y=0
            while x < len(long) and y < len(short):
                if short[y] != long[x]:
                    err += 1
                    x += 1
                    continue
                x += 1; y += 1
            if err <= 1: ans.append(i+1)
    print(len(ans))
    print(*ans)
            
main()
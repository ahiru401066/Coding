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
            if len(T) > len(s):
                err = 0; x=0; y=0
                while x < len(T) and y < len(s):
                    if T[x] != s[y]:
                        err += 1
                        x += 1
                        continue
                    x += 1; y += 1
                if err <= 1: ans.append(i+1)

            elif len(T) < len(s):
                err = 0; x=0; y=0
                while x < len(T) and y < len(s):
                    if T[x] != s[y]:
                        err += 1
                        y += 1
                        continue
                    x += 1; y += 1
                if err <= 1: ans.append(i+1)
    print(len(ans))
    print(*ans)
            
main()
def main():
    def bs(x):
        l = 0; r = 10**6
        md = minValue
        while l <= r:
            y = (l+r)//2
            d = x**2 + y**2
            md = min(md,abs(d - D))

            if d == D: return 0
            elif d > D: r = y-1
            elif d < D: l = y+1 
        return md

    D = int(input())
    minValue = 10**6
    for x in range(int(D**0.5)+2):
        minValue = min(minValue, bs(x))

    print(minValue)

main()
# ２分探索
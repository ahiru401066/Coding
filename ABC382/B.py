def main():
    n,d = map(int,input().split())
    s = list(input())

    for i in range(len(s)-1,-1,-1):
        if d > 0 and s[i] == "@":
            d -= 1
            s[i] = "."
    s = "".join(s)
    print(s)

main()
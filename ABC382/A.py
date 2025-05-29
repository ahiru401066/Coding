def main():
    n,d = map(int,input().split())
    s = list(input())

    for i in range(len(s)):
        if d > 0 and s[i] == "@":
            d -= 1
            s[i] = "."
    count = 0
    for i in range(len(s)):
        if s[i] == ".": count += 1
    print(count)

main()
# 方針ミスった、、
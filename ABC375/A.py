def main():
    n = int(input())
    s = input()

    count = 0
    for i in range(n):
        if i == 0 or i == n-1: continue
        if s[i] == "." and s[i-1] == "#" and s[i+1] == "#":
            count += 1
    print(count)

main()
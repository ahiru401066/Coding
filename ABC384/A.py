def main():
    n,c1,c2 = input().split()
    s = input()
    t = ""
    for i in range(len(s)):
        if s[i] != c1: t += c2
        else: t += c1
    print(t)
main()
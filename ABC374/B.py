def main():
    s = input()
    t = input()

    moreLen = len(s) if len(s) > len(t) else len(t)
    lessLen = len(s) if len(s) < len(t) else len(t)
    for i in range(moreLen):
        if i > lessLen-1:
            print(i+1)
            return
        if s[i] != t[i]:
            print(i+1)
            return
    print(0)

main()
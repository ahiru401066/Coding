def main():
    s = input()
    li = []
    count = 0
    for i in range(1,len(s)):
        if s[i] == "-": count += 1
        else:
            li.append(count)
            count = 0
    print(*li)


main()
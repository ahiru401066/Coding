def main():
    s = input()
    count = 0

    dis = 1
    while(dis*2 < len(s)):
        for i in range(len(s)):
            j = i+dis; k = j+dis
            if k >= len(s) : break
            if s[i] == "A" and s[j] == "B" and s[k] == "C":
                count += 1 
        dis += 1
    print(count)
main()
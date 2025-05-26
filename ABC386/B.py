def main():
    s =  input()

    count = 0  
    l = len(s)
    i = 0
    while(i < l):
        if s[i] == "0" and i < l-1 and s[i+1] == "0":
            count += 1
            i += 2
            continue
        i += 1
        count += 1
    print(count)

main()
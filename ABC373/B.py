def main():
    s = input()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    count = 0; currentIndex = 0
    for i in range(len(alphabet)):
        if i == 0: 
            for j in range(len(s)):
                if s[j] == alphabet[i]: 
                    currentIndex = j
            continue

        for j in range(len(s)):
            if s[j] == alphabet[i]:
                count += abs(currentIndex - j)
                currentIndex = j
    print(count)

    pass
main()
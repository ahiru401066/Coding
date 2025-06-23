def main():
    N = int(input())
    
    txt = ""
    while N != 0:
        txt += str(N%2)
        N //= 2
    
    count = 0
    for i in range(len(txt)):
        if txt[i] == "1": break
        count += 1
    print(count)

main()
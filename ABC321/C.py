def main():
    K = int(input())
    L = set()
    number = "0123456789"
    for bit in range(1,1024):
        num = ""
        for i in range(10):
            if bit & (1 << i):
                num += number[i]

        L.add(int(num[::-1]))
        
    L = list(L)
    L.sort()
    print(L[K])

main()
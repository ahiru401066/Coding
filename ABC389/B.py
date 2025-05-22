def main():
    x = int(input())
    n = 1
    i = 1
    while(True):
        if x == n:
            print(i)
            break
        i += 1
        n *= i

main()
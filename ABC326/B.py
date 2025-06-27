def main():
    N = int(input())

    for i in range(N,920):
        a = int(str(i)[0])
        b = int(str(i)[1])
        c = int(str(i)[2])
        if a * b == c:
            print(i)
            return    

main()
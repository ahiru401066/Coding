def main():
    N,A,B = map(int,input().split())
    C = list(map(int,input().split()))

    for i in range(len(C)):
        if C[i] == A+B:
            print(i+1)
            return

main()
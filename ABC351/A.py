def main():
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    print(sum(A)-sum(B)+1)

main()
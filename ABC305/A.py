def main():
    N = int(input())
    R = N % 5
    if R >= 3:
        print(N + (5 - R))
    else:
        print(N - R)

main()
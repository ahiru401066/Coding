def main():
    N = int(input())
    S = input()
    for i in range(N-2):
        if S[i:i+3] == "ABC":
            print(i+1)
            return
    print(-1)

main()
def main():
    N = int(input())
    S = input()
    T = input()

    for i in range(N):
        if S[i] == T[i]:
            continue
        if S[i] == "1" and T[i] == "l" or S[i] == "l" and T[i] == "1":
            continue
        if S[i] == "0" and T[i] == "o" or S[i] == "o" and T[i] == "0":
            continue

        print("No")
        return
    print("Yes")

main()
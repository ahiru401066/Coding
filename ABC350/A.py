def main():
    S = input()
    n = int(S[3:])

    if n == 316:
        print("No")
    elif 1 <= n <= 349:
        print("Yes")
    else:
        print("No")

main()
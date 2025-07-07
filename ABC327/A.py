def main():
    N = int(input())
    S = input()

    li = ["ab", "ba"]
    for i in range(N-1):
        s = S[i:i+2]
        if s in li:
            print("Yes")
            break
    else:
        print("No")

main()
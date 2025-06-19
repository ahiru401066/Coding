def main():
    S = input()

    if S[0] != "<":
        print("No")
    elif S[-1] != ">":
        print("No")
    else:
        C = S[1:-1]
        for i in range(len(C)):
            if C[i] != "=":
                print("No")
                return
        print("Yes")

main()
def main():
    S = input()
    for i in range(len(S)):
        if i == 0:
            if not S[i].isupper():
                print("No")
                return
        else:
            if not S[i].islower():
                print("No")
                return
    print("Yes")

main()
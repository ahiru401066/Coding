def main():
    S = input()
    if S[0] == "M":
        print("No")
    elif S[1] == "M" and S[0] == "R":
        print("Yes")
    elif S[2] == "M" and S[0] == "R" or S[2] == "M" and S[1] == "R":
        print("Yes")
    else:
        print("No")

main()
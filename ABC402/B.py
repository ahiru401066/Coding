def main():
    T = input()
    U = input()

    for i in range(len(T)):
        if(T[i] == U[0] or T[i] == "?"):
            if check(T[i::],U): return "Yes"
    return "No"

def check(subT, U):
    if len(subT) < len(U): return False
    for i in range(len(U)):
        if subT[i] != "?" and subT[i] != U[i]: return False
    return True

print(main())
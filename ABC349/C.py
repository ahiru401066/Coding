def main():
    S = input()
    T = input()
    S = S.upper()

    count = 0; l = 0
    for i in range(len(T)):
        while l < len(S):
            if T[i] == S[l]:
                count += 1
                l += 1
                break
            l += 1

    if count == 3:
        print("Yes")
    elif count == 2 and T[-1] == "X":
        print("Yes")
    else:
        print("No")
    # print(count)

main()
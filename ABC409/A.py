def main():
    n = int(input())
    T = input()
    A = input()

    for i in range(n):
        if T[i] == "o" and A[i] == "o":
            print("Yes")
            return
    print("No")

main()
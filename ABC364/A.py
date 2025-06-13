import sys

def main():
    n = int(input())
    S = [input() for _ in range(n)]
    for i in range(n-1-1):
        if S[i] == "sweet" and S[i+1] == "sweet":
            print("No")
            return
    print("Yes")

main()
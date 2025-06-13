import sys

def main():
    h,w = map(int,input().split())
    S = list(map(int,input().split()))
    C = [input() for _ in range(h)]
    X = input()
    
    S[0] -= 1; S[1] -= 1
    for i in range(len(X)):
        if X[i] == "U" and S[0] - 1 >= 0:
            if C[S[0]-1][S[1]] == ".":
                S[0] -= 1
        elif X[i] == "D" and S[0] + 1 <= h - 1:
            if C[S[0]+1][S[1]] == ".":
                S[0] += 1
        elif X[i] == "L" and S[1] - 1 >= 0:
            if C[S[0]][S[1]-1] == ".":
                S[1] -= 1
        elif X[i] == "R" and S[1] + 1 <= w - 1:
            if C[S[0]][S[1]+1] == ".":
                S[1] += 1
    print(S[0]+1,S[1]+1)

main()
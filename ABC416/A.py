def main():
    N,L,R = map(int,input().split())
    S = input()
    for i in range(L-1,R):
        # print(i,S[i])
        if S[i] == "x":
            print("No")
            return
    print("Yes")

main()
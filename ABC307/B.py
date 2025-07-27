def main():
    N = int(input())
    S = [input() for _ in range(N)]

    for i in range(N):
        for j in range(i+1,N):
            txt1 = S[i]+S[j]
            txt2 = S[j]+S[i]

            if txt1 == txt1[::-1] or txt2 == txt2[::-1]:
                print("Yes")
                return
    print("No")
    
main()
def main():
    S = input()
    # ans = ""
    # for i in range(len(S)-1,-1,-1):
    #     if S[i] == ".":
    #         break
    #     ans += S[i]
    # print(ans[::-1])
    s = S.rsplit(".",1)[-1]
    print(s)

main()
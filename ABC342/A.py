def main():
    S = input()
    for i in range(len(S)-1):
        if i == 0 and S[i] != S[i+1]:
            ans = i+1 if S[i] != S[-1] else i+1+1
            print(ans)
            break
        elif S[i] != S[i+1]:
            print(i+1+1)
            break

main()
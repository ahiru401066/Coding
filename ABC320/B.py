def main():
    S = input()
    
    maxLength = 0
    for i in range(len(S)):
        for j in range(i+1,len(S)+1):
            if S[i:j] == S[i:j][::-1]:
                maxLength = max(maxLength,len(S[i:j]))
    print(maxLength)

main()
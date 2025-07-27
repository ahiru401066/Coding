def main():
    N = int(input())
    S = input()
    TF = [0] * (N+1)

    stack = []
    for i in range(N):
        if S[i] == "(":
            stack.append(i)
            continue
        elif S[i] == ")" and len(stack) != 0:
            top = stack.pop()
            TF[top] = -1
            TF[i+1] = 1
    
    for i in range(len(TF)-1):
        TF[i+1] += TF[i]
    
    ans = ""
    for i in range(len(TF)-1):
        if TF[i] >= 0:
            ans += S[i]
    print(TF)
    print(ans)

main()
def main():
    N = int(input())
    S = input()

    stack = []
    for i in range(N):
        if S[i] == "(":
            stack.append([S[i]])

        elif S[i] == ")":
            if len(stack) == 0:
                stack.append([S[i]])
            else:
                top = stack.pop()
                if top[0] != "(":
                    top.append(S[i])
                    stack.append(top)

        else:
            if len(stack) == 0:
                stack.append([S[i]])
            else:
                top = stack.pop()
                top.append(S[i])
                stack.append(top)

    ans = ""
    for s in stack:
        ans += "".join(s)
    print(ans)

main()
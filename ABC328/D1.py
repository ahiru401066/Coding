def main():
    S = input()
    N = len(S)

    stack = []
    i = 0
    while i < N:
        stack.append(S[i])
        if len(stack) < 3:
            i += 1
            continue
        
        if stack[-1] == "C" and stack[-2] == "B" and stack[-3] == "A":
            for _ in range(3):
                stack.pop()

        i += 1
    ans = "".join(stack)
    print(ans)

main()
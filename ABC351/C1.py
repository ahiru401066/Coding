def main():
    N = int(input())
    A = list(map(int,input().split()))
    stack = []

    for i in range(N):
        stack.append(A[i])

        if len(stack) <= 1: continue
        
        top = stack[-1]
        second = stack[-2]

        while top == second:
            top = stack.pop()
            second = stack.pop()

            stack.append(top + 1)

            if len(stack) <= 1:
                break
            
            top = stack[-1]
            second = stack[-2]
            
    # print(*stack)
    print(len(stack))

main()
# ボールが増えることはない
# スタック？
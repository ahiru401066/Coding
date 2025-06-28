def main():
    def bs(x,li):
        l = 0; r = len(li)-1
        while l <= r:
            mid = (l+r)//2
            if li[mid] <= x: l = mid + 1
            else: r = mid - 1
        return l

    T = int(input())
    Number = []
    C = []
    for _ in range(T):
        N = int(input())
        S = list(map(int,input().split()))
        Number.append(N)
        C.append(S)

    for i in range(T):
        N,S = Number[i],C[i]
        stack = []
        for j in range(N):
            if j == 0 or j == len(N)-1:
                stack.append(S[i])
            else:
                top = stack[-1]
                if S[i]


        else:
            print(len(stack))

main()
# 2分探索
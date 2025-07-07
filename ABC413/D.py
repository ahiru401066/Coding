def main():
    T =int(input())
    N = []
    LA = []
    LB = []
    for _ in range(T):
        n = int(input())
        A = sorted(list(map(int,input().split())))
        B = sorted(A,key=abs)
        N.append(n); LA.append(A); LB.append(B)

    for i in range(T):
        n = N[i]; A = LA[i]; B = LB[i]

        #通常ソート
        for i in range(n-2):
            if not A[i] * A[i+2] == A[i+1]**2:
                break
        else:
            print("Yes")
            continue

        #絶対値ソート
        for i in range(n-2):
            if not B[i] * B[i+2] == B[i+1]**2:
                break
        else:
            print("Yes")
            continue
        
        # コーナーケース対応
        if abs(A[0]) == abs(A[-1]):
            x = 0; y = 0
            for i in range(n):
                if A[i] == A[0]: x += 1
                elif A[i] == A[-1]: y += 1
                else: break
            else:
                if abs(x - y) <= 1:
                    print("Yes")
                    continue
            print("No")
        else:
            print("No")

main()
#通常ソート
#絶対値ソート
#コーナーケース対応
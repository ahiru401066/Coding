def main():
    N = int(input())
    A = list(map(int,input().split()))
    pos = [0] * (N+1)
    for i in range(N):
        pos[A[i]] = i

    ans = []

    for i in range(N):
        correct = i+1
        if A[i] == correct:
            continue
        j = pos[correct]

        A[i],A[j] = A[j],A[i]
        pos[A[j]] = j
        pos[A[i]] = i
        
        ans.append((i+1,j+1))

    print(len(ans))
    for i,j in ans:
        print(i,j)


main()
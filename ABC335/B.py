def main():
    N = int(input())

    for i in range(N+1):
        for j in range(N+1):
            for k in range(N+1):
                # print(i,j,k)
                li = []
                if i + j + k <= N:
                    li.append(i)
                    li.append(j)
                    li.append(k)
                    print(*li)
main()


def main():
    N,Q = map(int,input().split())
    querys = [list(map(int,input().split())) for _ in range(Q)]
    A = [i for i in range(1,N+1)]
    
    i = 0
    for query in querys:
        if query[0] == 1:
            A[(query[1]+i-1)%N] = query[2]
        elif query[0] == 2:
            print(A[(query[1]+i-1)%N])
        elif query[0] == 3:
            k = query[1]
            i = (i+k) % N
    # print(A)

main()
import heapq

def main():
    Q = int(input())
    query = [list(map(int,input().split())) for _ in range(Q)]
    L = []
    heapq.heapify(L)

    for q in query:
        c = q[0]
        if c == 1: heapq.heappush(L,q[1])
        else:
            if len(L) == 0: continue
            top = heapq.heappop(L)
            print(top)

main()
# 優先度付きキュー
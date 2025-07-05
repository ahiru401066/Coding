from collections import deque

def main():
    Q = int(input())
    Query = [list(input().split()) for _ in range(Q)]
    q = deque()

    for query in Query:
        if query[0] == "1":
            c = int(query[1]); x = int(query[2])
            q.append([x,c])

        elif query[0] == "2":
            k = int(query[1])
            total = 0
            while k > 0:
                top = q.popleft()
                m = top[1]
                if m <= k:
                    k -= m
                    total += top[0] * top[1]
                else:
                    c = m - k
                    total += top[0] * k
                    q.appendleft([top[0],c])
                    k = 0
            print(total)

main()
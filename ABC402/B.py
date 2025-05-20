from collections import deque

def main():
    q = int(input())
    Q = deque()
    for _ in range(q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            Q.append(query[1])
        elif query[0] == 2:
            x = Q.popleft()
            print(x)

main()
# キューで要素を保持
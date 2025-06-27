from collections import deque

def main():
    H,W = map(int,input().split())
    S = [list(input()) for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    D = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    
    def bfs(sy,sx):
        queue = deque()
        queue.append((sy,sx))
        visited[sy][sx] = True

        while queue:
            y, x = queue.popleft()
            for d in D:
                dy,dx = d
                ny,nx = y+dy, x+dx
                if 0 <= ny < H and 0 <= nx < W:
                    if S[ny][nx] == "#" and not visited[ny][nx]:
                        visited[ny][nx] = True
                        queue.append((ny,nx))

    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#" and not visited[i][j]:
                bfs(i,j)
                count += 1
    print(count)

main()
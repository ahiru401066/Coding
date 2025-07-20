from collections import deque

def main():
    H,W = map(int,input().split())
    grid = [input() for _ in range(H)]
    pattern = "snuke"

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    if grid[0][0] != "s":
        print("No")
        return
    
    visited = [[[False] * 5 for _ in range(W)] for _ in range(H)]
    queue = deque()
    queue.append((0,0,0))

    visited[0][0][0] = True

    while queue:
        x,y,k = queue.popleft()
        nextK = (k+1) % 5
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < H and 0 <= ny < W:
                if not visited[nx][ny][nextK] and grid[nx][ny] == pattern[nextK]:
                    visited[nx][ny][nextK] = True
                    queue.append((nx,ny,nextK))
    found = any(visited[H-1][W-1][k] for k in range(5))
    if found: print("Yes")
    else: print("No")

main()
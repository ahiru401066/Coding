from collections import deque

def bfs_with_path(grid, start, goal):
    h, w = len(grid), len(grid[0])
    visited = [[False] * w for _ in range(h)]
    prev = [[None] * w for _ in range(h)]

    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True

    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    while q:
        y, x = q.popleft()
        if (y, x) == goal:
            break
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and grid[ny][nx] != "#":
                visited[ny][nx] = True
                prev[ny][nx] = (y,x)
                q.append((ny,nx))


# おそらく、非常口を見つけた場合幅優先探索を行い、上書きをしていく？
# 幅優先探索
# ・１点スタート、１点ゴール、最短距離
# ・１点スタート、１点ゴール、最短経路
# ・全ての点スタート、１点ゴール、最短距離、最短経路
# ・全ての点スタート、全てのゴール、最短距離、最短経路
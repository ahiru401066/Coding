H, W, N = map(int, input().split())
T = input()
S = [list(input()) for _ in range(H)]

move = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

total = 0
for i in range(1, H - 1):
    for j in range(1, W - 1):
        if S[i][j] == '#':
            continue
        y, x = i, j
        for t in T:
            dy, dx = move[t]
            y += dy
            x += dx
            if S[y][x] == '#':
                break
        else:
            total += 1

print(total)

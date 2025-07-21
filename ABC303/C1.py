def main():
    N, M, H, K = map(int, input().split())
    S = input()
    items = set()
    for _ in range(M):
        x, y = map(int, input().split())
        items.add((x, y))

    pos = [0, 0]
    for c in S:
        H -= 1
        if H < 0:
            print("No")
            return

        if c == "R":
            pos[0] += 1
        elif c == "L":
            pos[0] -= 1
        elif c == "U":
            pos[1] += 1
        elif c == "D":
            pos[1] -= 1

        if H < K and tuple(pos) in items:
            H = K
            items.remove(tuple(pos))  # 一度使ったら消す

    print("Yes")
main()
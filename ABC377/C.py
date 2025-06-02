def main():
    s = set()
    n,m = map(int,input().split())
    for _ in range(m):
        a,b = map(int,input().split())
        s.add((a,b))
        if a+2 <= n:
            if b+1 <= n: s.add((a+2,b+1))
            if b-1 >= 1: s.add((a+2,b-1))
        if a+1 <= n:
            if b+2 <= n: s.add((a+1,b+2))
            if b-2 >= 1: s.add((a+1,b-2))
        if a-1 >= 1:
            if b+2 <= n: s.add((a-1,b+2))
            if b-2 >= 1: s.add((a-1,b-2))
        if a-2 >= 1:
            if b+1 <= n: s.add((a-2,b+1))
            if b-1 >= 1: s.add((a-2,b-1))
    print(n*n - len(s))

main()
# 全マスの記録してたら無理
# 全マス - おけないマス = おけるマス
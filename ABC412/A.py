def main():
    N = int(input())
    count = 0
    for _ in range(N):
        a,b = map(int,input().split())
        if b > a: count += 1
    print(count)

main()
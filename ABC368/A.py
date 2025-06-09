def main():
    n, k = map(int,input().split())
    A = list(map(int,input().split()))
    ans = []
    for _ in range(k):
        x = A.pop()
        ans.append(x)
    ans = ans[::-1]
    print(*(ans+A))

main()
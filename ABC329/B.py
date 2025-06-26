def main():
    N = int(input())
    A = list(map(int,input().split()))
    S = set(A)
    L = sorted(list(S))
    print(L[-2])

main()
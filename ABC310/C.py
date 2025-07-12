def main():
    N = int(input())
    S = []
    for _ in range(N):
        s = input()
        S.append(s)
    
    Set = set()
    for s in S:
        e = s if s > s[::-1] else s[::-1]
        Set.add(e)
    print(len(Set))

main()
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    dic = {}
    for _ in range(N):
        a,c = map(int,input().split())
        if not c in dic.keys():
            dic[c] = a
        else:
            dic[c] = min(dic[c],a)
    m = max(v for v in dic.values())
    print(m)
    



main()
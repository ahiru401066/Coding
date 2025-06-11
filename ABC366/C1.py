import sys

def main():
    input = sys.stdin.readline
    Q = int(input())

    dic = {}; s = 0
    for _ in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            x = query[1]
            if not x in dic.keys(): dic[x] = 1
            else: dic[x] += 1
            if dic[x] == 1: s += 1

        elif query[0] == 2:
            x = query[1]
            dic[x] -= 1
            if dic[x] < 1: s -= 1
            
        elif query[0] == 3:
            print(s)
    
main()
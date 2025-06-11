import sys

def main():
    input = sys.stdin.readline 
    Q = int(input())

    dic = {}
    for _ in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            x = query[1]
            if not x in dic.keys():
                dic[x] = 1
            else: dic[x] += 1
        elif query[0] == 2:
            dic[query[1]] -= 1
            if dic[query[1]] == 0: del dic[query[1]]
        elif query[0] == 3:
            print(len(dic.keys()))

main()
# ボールの種類と個数
# dict型で種類と個数を管理
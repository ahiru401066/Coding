import sys

def main():
    input = sys.stdin.readline 
    n,q = map(int,input().split())

    li = [i for i in range(n+1)] #鳩と存在する巣　はとiはli[i]にいる
    count = [1 for i in range(n+1)] #巣にいる鳩の数

    num = 0
    for _ in range(q):
        query = list(map(int,input().split()))
        if query[0] == 2:
            print(num)

        elif query[0] == 1:
            pre = li[query[1]]
            next = query[2]
            count[pre] -= 1
            count[next] += 1
            if count[pre] == 1: num -= 1
            if count[next] == 2: num += 1

            li[query[1]] = query[2]


main()
# 巣の中にいる鳩の数、鳩の移動を保持
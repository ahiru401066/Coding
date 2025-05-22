import sys

def main():
    input = sys.stdin.readline 
    q = int(input())
    li = [0]
    dec = 0
    head = 0

    for _ in range(q):
        query = list(map(int,input().split()))
        
        if query[0] == 1:
            li.append(li[-1] + query[1])
        elif query[0] == 2:
            dec = li[head+1]
            head += 1
        elif query[0] == 3:
            k = query[1]
            print(li[head+k-1]-dec)


main()
# タイプ２、タイプ３の時、0(n)にならないようにする
# 減少する長さmをデータとして保持する
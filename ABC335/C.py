import sys

def main():
    input = sys.stdin.readline
    N,Q = map(int,input().split())
    Query = []
    for _ in range(Q):
        query = list(input().split())
        if query[0] == "1":
            Query.append([int(query[0]),query[1]])
        elif query[0] == "2":
            Query.append([int(query[0]),int(query[1])])

    print("="*50)
    L = [[0,0]]; pre1 = [1,0]; pre2 = [2,0]; count = 0
    dic = {"R":(1,0),"L":(-1,0),"U":(0,1),"D":(0,-1)}
    for i in range(len(Query)):
        if Query[i][0] == 1:
            L.append([L[-1][0]+pre1[0]-pre2[0],L[-1][1]+pre1[1]-pre2[1]])
            dx, dy = dic[Query[i][1]]
            pre2 = [pre1[0],pre1[1]]
            pre1 = [pre1[0]+dx,pre1[1]+dy]
            count += 1
        elif Query[i][0] == 2:
            print(Query[i][1]+L[count][0],0+L[count][1])

    print(L)

main()
# どのデータを保持するか
# 変化量を記録？
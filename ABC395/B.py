def main():
    n = int(input())
    li = [["." for _ in range(n)] for _ in range(n)]
    
    for i in range(1,n+1):
        j = n + 1 - i
        if i > j: continue

        color = "#" if i % 2 == 1 else "."

        for x in range(i-1,j):
            for y in range(i-1,j):
                li[x][y] = color
    printList(li)
    
def printList(l):
    for i in range(len(l)):
        s = ""
        for e in l[i]:
            s += e
        print(s)

main()

#はじめに N*N を作る -> 編集
# 短形領域を塗りつぶす <- !
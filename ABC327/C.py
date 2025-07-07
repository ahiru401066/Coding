def main():
    A = [list(map(int,input().split())) for _ in range(9)]
    
    # 縦
    for i in range(9):
        s = set(A[i][0:9])
        if len(s) != 9:
            print("No")
            return
    
    # 横         
    for i in range(9):
        li = []
        for j in range(9):
            li.append(A[j][i])
        s = set(li)
        if len(s) != 9:
            print("No")
            return
    
    # 3 * 3
    for i in range(0,9,3):
        for j in range(0,9,3):
            s = set()
            s.update(A[i][j:j+3])
            s.update(A[i+1][j:j+3])
            s.update(A[i+2][j:j+3])
            if len(s) != 9:
                print("No")
                return
    print("Yes")

main()
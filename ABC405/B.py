def main():
    n,m = map(int, input().split())
    A = list(map(int, input().split()))
    li = [i for i in range(1,m+1)]
    
    count = 0
    while(True):
        for l in li:
            if not l in A: 
                print(count)
                return
        A.pop()
        count += 1

main()

# 全探索でOK
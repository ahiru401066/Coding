import sys
sys.setrecursionlimit(120000)

def main():
    dic = {1:0}

    def recursion(n):
        if n == 1: return 0
        else:
            floor = n//2
            ceil = (n+1)//2
        
            if not floor in dic:
                dic[floor] = recursion(floor)
            if not ceil in dic:
                dic[ceil] = recursion(ceil)

            dic[n] = dic[floor] + dic[ceil] + n
            return dic[n]


    N = int(input())
    total = recursion(N)
    print(total)

main()
# メモ化再帰
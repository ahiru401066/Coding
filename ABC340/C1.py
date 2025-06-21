import sys
sys.setrecursionlimit(120000)

def main():
    dic = {1:0}

    def recursion(n):
        if n in dic:
            return dic[n]
        
        left = n//2
        right = (n+1)//2

        cost = n + recursion(left) + recursion(right)
        dic[n] = cost
        return cost

    N = int(input())
    total = recursion(N)
    print(total)

main()
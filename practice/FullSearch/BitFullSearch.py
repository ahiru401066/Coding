"""
問題:部分集合の和
N 個の整数が与えられる。これらの整数の部分集合の和を全て求め、その中で最大の和を求めなさい。
"""

def main():
    n = int(input())
    a = list(map(int, input().split()))
    total = 0

    for mask in range(1 << n):
        currentSum = 0
        for i in range(len(a)):
            if(mask & (1 << i)):
                currentSum += a[i]
        total = max(total, currentSum)
    
    print(total)

    
main()
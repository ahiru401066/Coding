import math

def main():
    total = 0
    preX = 0; preY = 0
    n = int(input())
    for _ in range(n):
        x, y = map(int,input().split())
        total += math.sqrt((x - preX) ** 2 + (y - preY)**2)
        preX = x; preY = y
    total += math.sqrt((0 - preX) ** 2 + (0 - preY) ** 2)
    print(total)

main()
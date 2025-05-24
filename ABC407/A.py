import math

def main():
    a, b = map(int,input().split())
    l = math.floor(a/b)
    u = math.ceil(a/b)
    if a % b == 0: print(a//b)
    elif abs(a/b - l) <= abs(a/b - u): print(l)
    else: print(u)
    

main()
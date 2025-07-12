import sys

def main():
    input = sys.stdin.readline
    N,L,R = map(int,input().split())
    count = 0
    for i in range(N):
        x,y = map(int,input().split())
        if x <= L and R <= y:
            count += 1
    print(count)
main()
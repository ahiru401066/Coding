import sys

def main():
    A,B,D = map(int,input().split())

    li = []
    for i in range(A,B+1,D):
        li.append(i)
    print(*li)

main()
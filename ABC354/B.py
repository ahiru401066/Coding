import sys

def main():
    n = int(input())
    li = []; total = 0
    for i in range(n):
        s,c = input().split()
        total += int(c)
        li.append([s,int(c)])

    x = total % n
    li.sort(key=lambda x:x[0])

    print(li[x][0])

main()
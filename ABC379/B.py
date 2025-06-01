import re

def main():
    n,k = map(int,input().split())
    s = input()

    oneBlock = re.findall(r'O+',s)
    total = 0
    for i in range(len(oneBlock)):
        total += len(oneBlock[i])//k
    print(total)

main()
# 歯を塊に分ける
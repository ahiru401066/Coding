from collections import defaultdict

def main():
    n = int(input())
    li = list(map(int,input().split()))
    dic = defaultdict(list)
    
    for i in range(len(li)):
        dic[li[i]].append(i)

    maxValue = -1
    maxIndex = -1
    for key, value in dic.items():
        if len(value) == 1 and key > maxValue:
            maxValue = key
            maxIndex = value[0]+1
    print(maxIndex)

main()
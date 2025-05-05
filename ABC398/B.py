from collections import Counter

def main():
    li = list(map(int, input().split()))
    dic = Counter(li)
    
    count2 = 0; count3 = 0
    for key, value in dic.items():
        if value >= 3: count3 += 1
        elif value >= 2: count2 += 1
    
    if count3 >= 2: print("Yes")
    elif count3 == 1 and count2 >= 1: print("Yes")
    else: print("No")

main()

#数字と枚数
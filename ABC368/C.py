def main():
    n = int(input())
    H = list(map(int,input().split()))

    total = 0; R = [1,1,3,0]; pos = 3
    for i in range(n):
        h = H[i]
        if i == 0: pos = 0
        else: 
            while pos < 3:
                h -= R[pos]
                total += 1
                pos += 1
                if h <= 0:
                    break
        if h <= 0:
            pos = 0 if pos > 2 else pos
            continue
                    
        c,pos = calc(h)
        total += (h//5)*3 + c

    print(total)

def calc(n):
    if n % 5 == 0: return 0,3
    elif n % 5 == 1: return 1,1
    elif n % 5 == 2: return 2,2
    elif n % 5 == 3: return 3,3
    elif n % 5 == 4: return 3,3

main()
# シュミュレーションしてはダメ
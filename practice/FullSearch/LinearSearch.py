def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    flg = False
    for e in a:
        if e == x: 
            flg = True
            break
    if(flg):print("Yes")
    else: print("No")

main()
def main():
    r,x = map(int, input().split())

    if x == 1 and r >= 1600 and r <= 2999: print("Yes")
    elif x == 2 and r >= 1200 and r <= 2399: print("Yes")
    else: print("No")

main()
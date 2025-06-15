def main():
    A,B = map(int,input().split())
    if A == B: print(-1)
    else:
        if A == 1 and B == 2 or A == 2 and B == 1:
            print(3)
        elif A == 2 and B == 3 or A == 3 and B == 2:
            print(1)
        elif A == 3 and B == 1 or A == 1 and B == 3:
            print(2)

main()
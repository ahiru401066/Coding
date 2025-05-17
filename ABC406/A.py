def main():
    a,b,c,d = map(int, input().split())
    if a < c:
        print("No")
        return
    elif a == c:
        if b > d:
            print("Yes")
            return
        else:
            print("No")
            return
    else:
        print("Yes")

main()
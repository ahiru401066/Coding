def main():
    n,t,a = map(int,input().split())
    m = n - (t+a)
    x = min(t,a); y = max(t,a)

    if x + m > y:
        print("No")
    else:
        print("Yes")

main()
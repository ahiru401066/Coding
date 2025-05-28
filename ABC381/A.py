def main():
    n = int(input())
    s = input()

    l = len(s)
    if l % 2 == 0:
        print("No"); return
    for i in range(l):
        if i <= (l+1)//2 - 2 and s[i] != "1":
            print("No"); return
        elif i == (l+1)//2 - 1 and s[i] != "/":
            print("No"); return
        elif i >= (l+1)//2 and s[i] != "2":
            print("No"); return
    print("Yes")

main()
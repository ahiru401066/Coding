def main():
    N = int(input())
    li = ["0","2","4","6","8"]
    if N == 1:
        print(0)
        return

    N -= 1
    five = ""
    while N != 0:
        five += str(N%5)
        N //= 5
        
    five = five[::-1]
    ans = ""
    for i in range(len(five)):
        ans += li[int(five[i])]

    print(int(ans))

main()
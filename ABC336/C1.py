def main():
    N = int(input())

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
        ans += str(int(five[i]) * 2)
    print(ans)

main()
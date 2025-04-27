def main():
    n = int(input())
    bin = toBinary(n)
    while(len(bin) != 10):
        bin += "0"
    ans = bin[::-1]
    print(ans)
    

def toBinary(n):
    ans = ""
    while(n > 0):
        ans += str(n % 2)
        n //= 2
    return ans

main()
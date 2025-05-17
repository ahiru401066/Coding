def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    num = 1

    for i in range(n):
        num *= A[i]
        digits = checkDigits(num)
        if digits > k: num = 1
    print(num)

def checkDigits(n):
    count = 1
    while(True):
        if n // 10 == 0: break
        n //= 10
        count += 1
    return count

main()
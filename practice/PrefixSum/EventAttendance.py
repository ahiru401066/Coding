# いもす法（差分＋累積和）
def main():
    d = int(input())
    n = int(input())
    b = [0] * (d+2)
    s = [0] * (d+3)

    for i in range(n):
        l, r = map(int, input().split())
        b[l] += 1; b[r+1] -= 1 

    for i in range(len(b)):
        s[i+1] = s[i] + b[i]

    for i in range(2,len(s)-1):
        print(s[i])
main()
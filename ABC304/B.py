def main():
    N = int(input())

    if N <= 10**3-1:
        print(N)
    elif N <= 10**4-1:
        ans = str(N)[:-1] + "0" * 1
        print(ans)
    elif N <= 10**5-1:
        ans = str(N)[:-2] + "0" * 2
        print(ans)
    elif N <= 10**6-1:
        ans = str(N)[:-3] + "0" * 3
        print(ans)
    elif N <= 10**7-1:
        ans = str(N)[:-4] + "0" * 4
        print(ans)
    elif N <= 10**8-1:
        ans = str(N)[:-5] + "0" * 5
        print(ans)
    else:
        ans = str(N)[:-6] + "0" * 6
        print(ans)



main()
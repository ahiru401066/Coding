def main():
    N = int(input())
    # for i in range(10**6,0,-1):
    #     if i**3 > N: continue
        
    #     if palindrome(str(i**3)):
    #         print(i ** 3)
    #         break

    i = 1; ans = 1
    while i**3 <= N:
        if palindrome(str(i**3)):
            ans = i**3
        i += 1
    print(ans)

def palindrome(s):
    return s == s[::-1]


main()
# Nが10**18以下であることより 1 <= x <= x * 10**6を調べればいい?
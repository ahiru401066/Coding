from collections import Counter

def isPalindrome(s):
    return s == s[::-1]

def main():
    N,K = map(int,input().split())
    S = input()

    counter = Counter(S)
    total = 0

    def dfs(path, counter):
        nonlocal total
        if len(path) == N:
            total += 1
            return
        for ch in counter:
            if counter[ch] > 0:
                nextPath = path + ch
                if len(nextPath) >= K:
                    if isPalindrome(nextPath[-K:]):
                        continue
                counter[ch] -= 1
                dfs(nextPath, counter)
                counter[ch] += 1
    dfs("",counter)
    print(total)

main()
def main():
    N = int(input())
    S = input()
    li = [0] * 26
    
    l = 0; a = S[0]
    for i in range(len(S)):
        if S[i] == a:
            l += 1
        else:
            li[ord(a)-97] = max(li[ord(a)-97],l)
            a = S[i]
            l = 1
    else: #good!!
        li[ord(a)-97] = max(li[ord(a)-97],l)

    print(sum(li))

main()
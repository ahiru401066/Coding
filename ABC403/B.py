def main():
    n = int(input())
    li = list(map(int, input().split()))
    
    ans = [0] * (len(li))
    index = 1
    for i in range(100,1,-1):
        for j in range(len(li)):
            if li[j] == i:
                ans[j] = index

    print(ans)

main()
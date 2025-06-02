def main():
    A = list(map(int,input().split()))
    li = [0]*5
    for i in range(len(A)):
        li[A[i]] += 1
    count = 0
    for i in range(1,5):
        if li[i] >= 4: count += 2
        elif li[i] >= 2: count += 1
    print(count)

main()
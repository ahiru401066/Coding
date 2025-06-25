def main():
    N = int(input())
    li = []
    for i in range(1,15):
        li.append(int(str("1" * i)))

    L = set()
    for i in range(len(li)):
        for j in range(len(li)):
            for k in range(len(li)):
                L.add(li[i]+li[j]+li[k])

    L = list(L)
    L.sort()
    print(L[N-1])

main()
# liの中から重複ありで3つ選びたい
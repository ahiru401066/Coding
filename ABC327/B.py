def main():
    B = int(input())

    li = [i**i for i in range(20)]
    for i in range(1,len(li)):
        if B == li[i]:
            print(i)
            break
    else:
        print(-1)

main()
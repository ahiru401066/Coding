def main():
    x, y = map(int, input().split())

    count = 0
    for i in range(1,7):
        for j in range(1,7):
            if i + j >= x: count += 1
            elif abs(i - j) >= y: count += 1
    print(count / 36)


main()
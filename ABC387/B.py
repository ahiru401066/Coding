def main():
    x = int(input())

    total = 0
    for i in range(1,10):
        for j in range(1,10):
            if i*j != x: total += i*j
    print(total)

main()
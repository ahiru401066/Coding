def main():
    n = int(input())
    count = 0
    for _ in range(n):
        s = input()
        if len(s) != 4: count += 1
    print(count)

main()
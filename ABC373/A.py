def main():
    n = 12
    count = 0
    for i in range(12):
        s = input()
        l = len(s)
        if i+1 == l: count += 1
    print(count)
main()
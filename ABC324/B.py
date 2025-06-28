def main():
    N = int(input())
    for i in range(100):
        for j in range(100):
            if 2**i * 3**j == N:
                print("Yes")
                return
    print("No")

main()
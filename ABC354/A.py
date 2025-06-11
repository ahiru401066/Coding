import sys

def main():
    h = int(input())
    i = 0; l = 0
    while True:
        # print(l)
        if l > h:
            print(i)
            break
        l += 2**i
        i += 1

main()
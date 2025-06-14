import sys

def main():
    r = int(input())
    if r <= 99:
        print(100 - r)
    elif r <= 199:
        print(200 - r)
    elif r <= 299:
        print(300 - r)
    elif r <= 399:
        print(400 - r)

    # print(100 - r%100)

main()

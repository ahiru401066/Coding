from decimal import Decimal

def main():
    x = input()
    while True:
        if ("." in x and x[-1] == "0") or (x[-1] == "."):
            x = x[:-1]
            continue
        break
    print(x)

main()
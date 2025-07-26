def main():
    S = input()
    flg = True
    T = ""
    for s in S:
        if s == "#":
            T += "#"
            flg = True
            continue

        if flg:
            T += "o"
            flg = False
            continue

        T += "."

    print(T)

main()
def main():
    s = input()
    txt = ""
    for e in s:
        if e.isupper():
            txt += e
    print(txt)

main()
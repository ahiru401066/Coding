def main():
    s = input()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for e in alphabet:
        if not e in s:
            return e

print(main())
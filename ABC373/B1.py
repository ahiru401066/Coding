def main():
    s = input()
    pos = {char: i for i, char in enumerate(s)}
    print(pos)

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total = 0
    current = pos["A"]

    for ch in alphabet[1:]:
        total += abs(pos[ch] - current)
        current = pos[ch]
    
    print(total)

main()
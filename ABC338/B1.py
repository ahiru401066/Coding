from collections import Counter

def main():
    S = input()
    counts = Counter(S)
    maxCount = max(counts.values())

    for k,v in counts.items():
        if v == maxCount:
            print(k)
            return

main()
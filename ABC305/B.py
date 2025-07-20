def main():
    p,q = input().split()
    t = p if p > q else q
    s = p if p < q else q
    dic = {
        "A": 0,
        "B": 3,
        "C": 4,
        "D": 8,
        "E": 9,
        "F": 14,
        "G": 23,
    }
    print(dic[t] - dic[s])

main()
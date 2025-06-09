def main():
    # 入力受け取り
    n = int(input())
    A = []; S = []
    for _ in range(n):
        query = list(input().split())
        A.append(int(query[0]))
        S.append(query[1])

    total = 0
    preL = 0; preR = 0
    for i in range(n):
        a = A[i]
        s = S[i]
        if s == "L":
            if preL != 0:
                total += abs(preL - a)
            preL = a 
        elif s == "R":
            if preR != 0:
                total += abs(preR - a)
            preR = a 
    print(total)

main()
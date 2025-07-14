def main():
    N = int(input())
    S = input()
    t = 0; a = 0
    for i in range(N):
        if S[i] == "T": t += 1
        elif S[i] == "A": a += 1

    if t > a: print("T")
    elif t < a: print("A")
    else:
        if S[-1] == "T": print("A")
        else: print("T")

main()
from collections import deque

def main():
    S = input()
    T = input()
    # d = deque([e for e in S])

    for i in range(len(T)):
        stone = "b" if i % 2 == 0 else "w"
        if T[i] == "L":
            S = stone + S
            index = 0
            for j in range(1,len(S)):
                if S[j] == stone:
                    index = j
                    break
            if not index == 0: S = stone * (index+1) + S[index+1::]
        else:
            S = S + stone
            index = len(S)
            for j in range(len(S)-2,-1,-1):
                if S[j] == stone:
                    index = j
                    break
            if not index == len(S): S = S[0:index] + stone * (len(S) - index)
    b = 0; w = 0
    for s in S:
        if s == "b": b += 1
        else: w += 1
    print(b,w)

main()
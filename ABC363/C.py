from itertools import permutations

def main():
    def check(txt):
        l = len(txt)
        for i in range(l//2):
            if txt[i] != txt[l-i-1]:
                return False
        return True

    N,K = map(int,input().split())
    S = input()

    E = set()
    for e in permutations(S):
        E.add(e)

    count = set(); 
    for e in E:
        for i in range(N-K+1):
            txt = e[i:i+K]
            if txt in count: break
            elif check(txt):
                count.add(txt)
                break

    print(len(E) - (count))


main()
# 並び替え？
# 回文判定？
# シュミュレーション or 論理
def main():
    T = int(input())
    N = []; M = []
    A = []; B = []
    for _ in range(T):
        n,m = map(int,input().split())
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        N.append(n); M.append(m)
        A.append(a); B.append(b)

    for i in range(T):
        dicA = {}
        for a in A[i]:
            if not a in dicA:
                dicA[a] = 1
            else: dicA[a] += 1
        
        dicB = {}
        for b in B[i]:
            if (M[i]-b) in dicA:
                if dicA[M[i]-b] > 0:
                    dicA[M[i]-b] -= 1
            else:
                if b in dicB:
                    dicB[b] += 1
                else: dicB[b] = 1

        dicA = {k:v for k,v in dicA.items() if v > 0}
        dicB = {k:v for k,v in dicB.items() if v > 0}
        # print(dicA)
        # print(dicB)

        valueA = [k for k,v in dicA.items() for _ in range(v)]
        valueB = [k for k,v in dicB.items() for _ in range(v)] 
        valueA.sort()
        valueB.sort(reverse=True)
        # print(valueA)
        # print(valueB)

        Z = M[i]
        total = 0
        for i in range(len(valueA)):
            total += (valueA[i]+valueB[i]) % Z
        print(total)
main()
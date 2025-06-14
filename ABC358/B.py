def main():
    N,A = map(int,input().split())
    T = list(map(int,input().split()))

    for i in range(N):
        if i == 0:
            print(T[i]+A)
            T[i] += A
            continue
            
        if T[i-1] >= T[i]:
            print(T[i-1]+A)
            T[i] = T[i-1]+A
        else:
            print(T[i]+A)
            T[i] = T[i]+A


main()
# 待つ場合と待たない場合
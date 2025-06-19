def main():
    A = []
    while True:
        a = int(input())
        A.append(a)
        if a == 0:
            break
    
    for i in range(len(A)-1,-1,-1):
        print(A[i])

main()
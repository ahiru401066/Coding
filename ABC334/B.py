def main():
    A,M,L,R = map(int,input().split())

    L -= A; R -= A

    countL = (L-1)//M
    countR = R//M
    print(countR - countL)
    
    # count = 0
    # for i in range(L,R+1):
    #     if i % M == 0: count += 1
    # print(count)

main()
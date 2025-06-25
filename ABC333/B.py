def main():
    L1 = set(["AB","BC","CD","DE","AE"])
    L2 = set(["AC","AD","BD","BE","CE"])
    S1 = list(input())
    T1 = list(input())
    S1.sort(); S1 = "".join(S1)
    T1.sort(); T1 =  "".join(T1)

    if S1 in L1 and T1 in L1 or S1 in L2 and T1 in L2:
        print("Yes")
    else:
        print("No")

main()
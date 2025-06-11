def main():
    A,B,C = map(int,input().split())
    li = []
    i = B
    while True:
        if i == C+1: break
        i = i-24 if i >= 24 else i
        li.append(i)
        i += 1
    if A in li: print("No")
    else: print("Yes")

main()
# B,Cの区間内にAが入るか

# if B < C:
#     if B < A < C:
#         print("No")
#     else:
#         print("Yes")
# else:
#     if C < A < B:
#         print("Yes")
#     else:
#         print("No")
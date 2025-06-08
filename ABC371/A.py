def main():
    L = list(input().split())
    A = 0; B = 0; C = 0
    if L[0] == "<": B += 1
    else: A += 1
    if L[1] == "<": C += 1
    else: A += 1
    if L[2] == "<": C += 1
    else: B += 1
    if A == 1: print("A")
    elif B == 1: print("B")
    elif C == 1: print("C")

main()
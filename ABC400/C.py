import math

def main():
    n = int(input())
    count = 0
    for a in range(1,60):
        for b in range(1,int(math.sqrt(n//2**a))+1,2):
            count += 1
    return count

print(main())
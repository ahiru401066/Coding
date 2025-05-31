def main():
    n = input()
    li = [0] * 4
    for e in n:
        if e == "1": li[1] += 1
        elif e == "2": li[2] += 1
        elif e == "3": li[3] += 1
    
    for i in range(1,len(li)):
        if not i == li[i]:
            print("No"); return
    print("Yes")

main()
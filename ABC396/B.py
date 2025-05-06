def main():
    q = int(input())
    li = [0] * 100
    for _ in range(q):
        query = list(map(int,input().split()))
        if query[0] == 2:
           out = li.pop()
           print(out)
        else:
            li.append(query[1])
    
main()
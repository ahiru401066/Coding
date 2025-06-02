def main():
    l = [input() for _ in range(8)]
    record = [[True] * 8 for _ in range(8)]

    for i in range(8):
        for j in range(8):
            if l[i][j] == "#":
                for k in range(8):
                    record[i][k] = False
                    record[k][j] = False
    count = 0
    for i in range(8):
        for j in range(8):
            if record[i][j]: count += 1
    print(count)
    
main()
# T or Fの記録用配列を保持
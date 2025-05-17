def main():
    s = input()
    li = [e for e in s]

    i = 0; j = i+1
    while(i < len(li)-1):
        if li[i] == "W" and li[j] == "A":
            li[i] = "A"; li[j] = "C"
            i -= 1; j = i+1
            if i < 0: i = 0; j = i+1
        else:  
            i += 1; j = i+1
    print("".join(e for e in li))


main()
# O(n)で行けるはず
# 変更したら戻って変更影響を確認しながら進行する
def main():
    s = input()
    count = 0

    for i in range(len(s)-1):
        count += 1
        dis = calc(s[i], s[i+1])
        count += dis
    count += int(s[-1]) + 1

    print(count)




def calc(a,b):
    a = int(a); b = int(b)
    if a >= b: return a-b
    else: return 10 - (b - a)
    


main()
# 要素の挿入は絶対 len(s)
# 数字の変更処理の部分で工夫の余地あり
# おそらく揃えると思う
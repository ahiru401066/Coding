def main():
    n,k = map(int,input().split())
    s = input()
    liIndex = []
    liLength = []

    # 先頭位置を記録
    if s[0] == "1": liIndex.append(0)
    for i in range(len(s)-1):
        if s[i] == "0" and s[i+1] == "1":
            liIndex.append(i+1)
    
    # 塊の長さを記録
    count = 0
    for i in range(len(s)):
        if s[i] == "1": count += 1
        elif s[i] == "0" and count != 0:
            liLength.append(count)
            count = 0
    if count != 0: liLength.append(count)

    pre = s[:liIndex[k-1-1]]
    tail = s[liIndex[k-1]+liLength[k-1]:]
    mid = s[liIndex[k-1-1]:liIndex[k-1-1]+liLength[k-1-1]] + s[liIndex[k-1]:liIndex[k-1]+liLength[k-1]] + "0" * (liIndex[k-1] - (liIndex[k-1-1]+liLength[k-1-1]))
    # print(pre)
    # print(mid)
    # print(tail)
    print(pre + mid + tail)

main()
# 必要な情報
# K番目の先頭位置、要素数
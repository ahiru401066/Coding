def main():
    n = int(input())
    sList = []
    tList = []
    # 入力処理
    for i in range(n):
        s = input()
        sList.append(s)
    for i in range(n):
        t = input()
        tList.append(t)

    minTotal = 1000000
    rotationS = sList
    i=0
    while(i < 4):
        distance = calcDiff(rotationS,tList)
        if distance+i < minTotal:
            minTotal = distance+i
        rotationS = rotation(rotationS)
        i += 1
    
    print(minTotal) 


def calcDiff(sList, tList):
    count = 0
    for i in range(len(sList)):
        for j in range(len(sList)):
            if sList[i][j] != tList[i][j]:
                count += 1
    return count

def rotation(sList):
    rotationList = []
    reverseSList = sList[::-1]
    for i in range(len(sList)):
        text = ""
        for s in reverseSList:
            text += s[i]
        rotationList.append(text)
    return rotationList

main()

"""
1. 比較関数を作る
2. 全てのローテーション（４パターン）を試す、最もローテーションがないものを見つける
3. 正解との差を計算する
"""
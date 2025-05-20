from collections import defaultdict

def main():
    n, m = map(int, input().split())
    # K = [set(map(int, input().split()[1::])) for _ in range(m)]
    A = []
    ingredient_to_dishes = defaultdict(list)
    for dish_id in range(m):
        temp = list(map(int, input().split()))
        ingredients = temp[1:]
        A.append(ingredients)
        for ing in ingredients:
            ingredient_to_dishes[ing].append(dish_id)
    B = list(map(int, input().split()))
    unlikeCount = [len(a) for a in A]

    canEat = 0
    res = []
    for ing in B:
        for dish in ingredient_to_dishes[ing]:
            unlikeCount[dish] -= 1
            if unlikeCount[dish] == 0:
                canEat += 1
        res.append(canEat)

    for r in res:
        print(r)

main()
# メイン処理は日の経過のループ
# おそらく２重ループ、３重もある？　日の経過 -> 料理の食材チェック
# 工夫の対象はデータ構造の選び方とループの減らし方 2重ループから減らせない、、、

# 方針１：克服した食材を日の経過とともに記録、それぞれの食材について確認 <- 遅い、、、
# 方針２：それぞれの料理の食材一覧から克服した食材を消していく

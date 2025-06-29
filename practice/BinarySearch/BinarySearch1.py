def BinarySearch1(x,li):
    """xがあるかどうかを探す"""
    left = 0; right = len(li)-1
    while left <= right:
        mid = (left+right)//2
        if li[mid] == x: return mid
        elif li[mid] > x: right = mid - 1
        elif li[mid] < x: left = mid + 1
    return -1

def BinarySearch1_1(x,li):
    """基本形の改良版　right=mid, left=midに合わせる"""
    left = -1; right = len(li)
    while left +1 < right:
        mid = (left+right)//2
        if li[mid] == x: return mid
        elif li[mid] > x: right = mid
        elif li[mid] < x: left = mid
    return -1

def BinarySearch2(x,li):
    """x以上最小の数を探す"""
    left = -1; right = len(li)
    while left + 1 < right:
        mid = (left+right)//2
        if li[mid] >= x: right = mid
        elif li[mid] < x: left = mid
    return right

def BinarySearch3(x,li):
    """xより大きい数で最小の数を探す"""
    left = -1; right = len(li)
    while left + 1 < right:
        mid = (left+right)//2
        if li[mid] > x: right = mid
        elif li[mid] <= x: left = mid
    return right

def test(x,li):
    """x以下最大の数"""
    left = -1; right = len(li)
    while left + 1 < right:
        mid = (left+right)//2
        if li[mid] <= x: left = mid
        elif li[mid] > x: right = mid
    return left


li = [1,4,6,14,21,38,43,62,70,89]
# ans = BinarySearch3(1,li)
ans = BinarySearch1(0,li)
print(ans)

# xは整数
# ポイント：２分探索は探索しない範囲を大きくしていくと捉える！、範囲の消去法と捉える？
# 探索対象範囲を狭めていくと捉える！探索対象範囲、探索済み範囲（条件を満たさない範囲、条件を満たす範囲）
# 全て探索した = 探索済み範囲が隣り合う
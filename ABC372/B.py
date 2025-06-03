def main():
    m = int(input())
    t = ""
    while m != 0:
        t += str(m%3)
        m //= 3
    # reversedT = t[::-1]
    ans = []
    for i in range(len(t)):
        for j in range(int(t[i])):
            ans.append(i)
    print(len(ans))
    print(*ans)
main()
# 方向性がすぐに掴めない、、
# 要素が溜まったら次の3の累乗?
# ３進数だ、、
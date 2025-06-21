def main():
    S = input()
    dic = {}
    for s in S:
        if not s in dic:
            dic[s] = 1
        else:
            dic[s] += 1
    
    dic = dict(sorted(dic.items()))
    maxCount = max(dic.values())
    
    for k,v in dic.items():
        if v == maxCount:
            print(k)
            return
 
    # dic = dict(sorted(dic.items()))
    # maxAlphabet = ""; maxCount = 0
    # for k,v in sorted(dic.items(),reverse=True):
    #     if v >= maxCount:
    #         maxCount = v
    #         maxAlphabet = k
    # print(maxAlphabet)

main()
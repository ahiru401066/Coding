N = int(input())
ans = 0
flg = False


s = ""
for i in range(N):
    s = input()
    if s == "login": flg = True
    elif s == "logout": flg = False
    
    if(not flg and s == "private"): ans += 1

print(ans)
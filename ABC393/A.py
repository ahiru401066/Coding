def main():
    s1, s2 = input().split()
    if s1 == "fine" and s2 == "fine": print(4)
    elif s1 == "fine" and s2 == "sick": print(3)
    elif s1 == "sick" and s2 == "fine": print(2)
    else: print(1)

main()
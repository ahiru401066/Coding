def main():
    s = input()
    li = [(0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)]
    for a,b,c in li:
        if s[a] + s[b] + s[c] == "ABC":
            print("Yes"); return
    print("No")
main()
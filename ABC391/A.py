def main():
    d = input()
    if len(d) == 1: print(direction(d)) 
    else: 
        return print(direction(d[0]) + direction(d[1]))

def direction(s):
    if s == "N": return "S"
    elif s == "S": return "N"
    elif s == "W": return "E"
    elif s == "E": return "W"

main()
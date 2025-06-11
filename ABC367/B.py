def main():
    x = input()
    stack = list(x)
     
    
    while True:
        x = stack.pop()
        if x == ".":
            stack.append(x)
            break
        elif x != "0":
            stack.append(x)
            break
    
    if stack[-1] == ".":
        print("".join(stack[:-1]))
    else:
        print("".join(stack))

main()


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
class Tree:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        node = Node(data)

        if self.head is None: self.head = node
        else: self.insertRec(self.head, node)

    def insertRec(self, currentNode, node):
        if node.data < currentNode.data:
            if currentNode.left is None: currentNode.left = node
            else: self.insertRec(currentNode.left, node)
        else:
            if currentNode.right is None: currentNode.right = node
            else: self.insertRec(currentNode.right, node)
    
    def search(self, data):
        return self.searchRec(self.head, data)

    def searchRec(self, currentNode, data):
        if currentNode is None:
            return False 
        if currentNode.data == data:
            return True  
        elif data < currentNode.data:
            return self.searchRec(currentNode.left, data)  
        else:
            return self.searchRec(currentNode.right, data)  


def main():
    n,m,q = map(int, input().split())
    users = [None] * 1_000_000

    for i in range(q):
        z = list(input().split())
        if z[0] == "1":
            users[z[1]] = Tree()
            z[1].insert(int(z[2]))
        elif z[0] == "2":
            users[z[1]] = -1
        elif z[0] == "3":
            user = z[1]
            num = int(z[2])
            if users[user] == -1: 
                print("Yes")
                continue
            elif z[user].search(num): 
                print("Yes")
                continue
            print("No")

main()
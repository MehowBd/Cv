class node:
    def __init__(self, key, value, left = None, right = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
    
class bst:
    def __init__(self):
        self.root = None
    
    def search(self, key, node: node):
        if self.root == None:
            return None
        
        if node.key == key:
            return node.value
        elif node.key > key:
            return self.search(key, node.left)
        elif node.key < key:
            return self.search(key, node.right)
        
    def find_min(self, current):
        if self.root == None:
            return None
        while current.left:
            current = current.left
        return current.key, current.value

    def delete(self, key):
        current = self.root
        self._delete(key, current)
        
    def _delete(self, key, node):
        if key < node.key:
            if node.left != None:
                node.left = self._delete(key, node.left)
        elif key > node.key:
            if node.right != None:
                node.right = self._delete(key, node.right)
        else:
            if node.left == None and node.right == None:
                return None
            elif node.left == None:
                return node.right
            elif node.right == None:
                return node.left
            
            min = self.find_min(node.right)
            k, v = min
            node.key = k
            node.value = v
            node.right = self._delete(k, node.right)
        return node
            
    def insert(self, data: node):
        if self.root == None:
            self.root = data
            return
        current = self.root
        previous = None
        while current:
            if current.key == data.key:
                current.value = data.value
                return
            if current.key > data.key:
                previous = current
                current = current.left
            else:
                previous = current
                current = current.right
        if previous.key < data.key:
            previous.right = data
        elif previous.key > data.key:
            previous.left = data
    
    def height(self, node: node, depth = 1):
        if node.left != None and node.right != None:
            depth_r = self.height(node.right, depth+1)
            depth_l = self.height(node.left, depth+1)
            if depth_r > depth_l:
                depth = depth_r
            else:
                depth = depth_l
        elif node.left != None and node.right == None:
            depth = self.height(node.left, depth+1)
        elif node.left == None and node.right != None:
            depth = self.height(node.right, depth+1)
        return depth
        
                
    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node: node, lvl):
        if node!=None:
            self._print_tree(node.right, lvl+5)
            print()
            print(lvl*" ", node.key, node.value)
        
            self._print_tree(node.left, lvl+5)
            
    def order(self, node, tab):
        if node != None:
            self.order(node.left, tab)
            tab.append((node.key, node.value))
            self.order(node.right, tab)
            return
        
    def __str__(self):
        tab = []
        self.order(self.root, tab)
        pr = "["
        for el in tab:
            pr += str(el[0]) +":" + str(el[1]) + ", "
        pr_new = pr[:-2]
        pr_new += "]"
        return pr_new
    
def main():
    elements = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}
    test = bst()
    for key, value in elements.items():
        test.insert(node(key, value))
    test.print_tree()
    print(test)
    print(test.search(24, test.root))
    test.insert(node(20, "AA"))
    test.insert(node(6, "M"))
    test.delete(62)
    test.insert(node(59, "N"))
    test.insert(node(100, "P"))
    test.delete(8)
    test.delete(15)
    test.insert(node(55, "R"))
    test.delete(50)
    test.delete(5)
    test.delete(24)
    print(test.height(test.root))
    print(test)
    test.print_tree()
  
    
if __name__ == "__main__":
    main()
        
        
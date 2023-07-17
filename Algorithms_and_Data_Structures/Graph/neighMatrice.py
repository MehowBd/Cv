import polska

class node:
    def __init__(self, key = None):
        self.key = key
        
    def __eq__(self,key):
        if self.key == key:
            return True
        
    def __hash__(self):
        return hash(self.key)
    
class edge:
    def __init__(self, parent = None, child = []):
        self.parent = parent
        self.child = child

class neighMatrice:
    def __init__(self, list = []):
        self.dict = {}
        self.list = list  
    
    def insertVertex(self, node: node):
        if self.list == None:
            self.list.append([0])
            self.dict.update({node.key:len(self.list) - 1})
        else:
            for tab in self.list:
                tab.append(0)
            self.list.append([0 for i in range(len(self.list)+1)])
            self.dict.update({node.key:len(self.list) - 1})
          
    def insertEdge(self, node1: node, node2: node, edge):
        self.list[self.dict[node1.key]][self.dict[node2.key]] = edge
        self.list[self.dict[node2.key]][self.dict[node1.key]] = edge
        
    def deleteVertex(self, node: node):
        if self.list == None:
            return
        else:
            self.list.pop(self.dict[node.key])
            for tab in self.list:
                tab.pop(self.dict[node.key])
            for key in self.dict:
                if self.dict[key] > self.dict[node.key]:
                    self.dict[key] -= 1
            self.dict.pop(node.key, None)
            
    def deleteEdge(self, node1: node, node2:node):
        self.list[self.dict[node1.key]][self.dict[node2.key]] = 0
        self.list[self.dict[node2.key]][self.dict[node1.key]] = 0
    
    def getVertexIdx(self, node:node):
        return self.dict[node.key]
    
    def getVertex(self, node_idx):
        for keys, vals in self.dict.items():
            if node_idx == vals:
                return keys
    
    def neighbours(self, node_idx):
        return [i for i, e in enumerate(self.list[node_idx]) if e != 0]
    
    def order(self):
        return len(self.list[0])
    
    def size(self):
        num = self.edges()
        return len(num)//2
    
    def edges(self):
        pairs = []
        for i in range(len(self.list)):
            neigh = self.neighbours(i)
            for j in neigh:
                pairs.append((self.getVertex(i), self.getVertex(j)))
        return pairs
    
class neighList:
    def __init__(self, list = []):
        self.dict = {}
        self.list = list  
    
    def insertVertex(self, node: node):
        self.list.append([])
        self.dict.update({node.key:len(self.list) - 1})
          
    def insertEdge(self, node1: node, node2: node, edge):
        if not self.getVertexIdx(node2) in self.list[self.getVertexIdx(node1)]:
            self.list[self.getVertexIdx(node1)].append(self.getVertexIdx(node2))
        if not self.getVertexIdx(node1) in self.list[self.getVertexIdx(node2)]:
            self.list[self.getVertexIdx(node2)].append(self.getVertexIdx(node1))
        
    def deleteVertex(self, node: node):
        if self.list == None:
            return
        else:
            self.list.pop(self.getVertexIdx(node))
            id = self.getVertexIdx(node)
            
            for i in range(len(self.list)-1):
                if id in self.list[i]:
                    self.list[i].remove(id)
                for j in range(len(self.list[i])):
                    if self.list[i][j] >= id:
                        self.list[i][j] -= 1         

                        
            for key in self.dict:
                if self.dict[key] > id:
                    self.dict[key] -= 1
            self.dict.pop(node.key, None)
            
    def deleteEdge(self, node1: node, node2:node):
        self.list[self.getVertexIdx(node1)].remove(self.getVertexIdx(node2))
        self.list[self.getVertexIdx(node2)].remove(self.getVertexIdx(node1))
    
    def getVertexIdx(self, node:node):
        return self.dict[node.key]
    
    def getVertex(self, node_idx):
        for keys, vals in self.dict.items():
            if node_idx == vals:
                return keys
    
    def neighbours(self, node_idx):
        return self.list[node_idx]
    
    def order(self):
        return len(self.list[0])
    
    def size(self):
        num = self.edges()
        return len(num)//2
    
    def edges(self):
        pairs = []
        for i in range(len(self.dict)):
            for j in self.list[i]:
                pairs.append((self.getVertex(i), self.getVertex(j)))
        return pairs
        
def lista_sasiedztwa():
    test = neighList()
    nodes = ['Z', 'G', 'N', 'B', 'F', 'P', 'C', 'E', 'W', 'L', 'D', 'O', 'S', 'T', 'K', 'R']

    graf = [('Z', 'G'), ('Z', 'P'), ('Z', 'F'),
            ('G', 'Z'), ('G', 'P'), ('G', 'C'), ('G', 'N'),
            ('N', 'G'), ('N', 'C'), ('N', 'W'), ('N', 'B'),
            ('B', 'N'), ('B', 'W'), ('B', 'L'),
            ('F', 'Z'), ('F', 'P'), ('F', 'D'),
            ('P', 'F'), ('P', 'Z'), ('P', 'G'), ('P', 'C'), ('P', 'E'), ('P', 'O'), ('P', 'D'),
            ('C', 'P'), ('C', 'G'), ('C', 'N'), ('C', 'W'), ('C', 'E'),
            ('E', 'P'), ('E', 'C'), ('E', 'W'), ('E', 'T'), ('E', 'S'), ('E', 'O'),
            ('W', 'C'), ('W', 'N'), ('W', 'B'), ('W', 'L'), ('W', 'T'), ('W', 'E'),
            ('L', 'W'), ('L', 'B'), ('L', 'R'), ('L', 'T'),
            ('D', 'F'), ('D', 'P'), ('D', 'O'),
            ('O', 'D'), ('O', 'P'), ('O', 'E'), ('O', 'S'),
            ('S', 'O'), ('S', 'E'), ('S', 'T'), ('S', 'K'),
            ('T', 'S'), ('T', 'E'), ('T', 'W'), ('T', 'L'), ('T', 'R'), ('T', 'K'),
            ('K', 'S'), ('K', 'T'), ('K', 'R'),
            ('R', 'K'), ('R', 'T'), ('R', 'L')]

    for el in nodes:
        test.insertVertex(node(el))
    for el in graf:
        test.insertEdge(node(el[0]), node(el[1]), 1)
    test.deleteVertex(node("K"))
    test.deleteEdge(node("W"), node("E"))
    polska.draw_map(test.edges())
    
def macierz_sasiedztwa():
    test = neighMatrice()
    nodes = ['Z', 'G', 'N', 'B', 'F', 'P', 'C', 'E', 'W', 'L', 'D', 'O', 'S', 'T', 'K', 'R']

    graf = [('Z', 'G'), ('Z', 'P'), ('Z', 'F'),
            ('G', 'Z'), ('G', 'P'), ('G', 'C'), ('G', 'N'),
            ('N', 'G'), ('N', 'C'), ('N', 'W'), ('N', 'B'),
            ('B', 'N'), ('B', 'W'), ('B', 'L'),
            ('F', 'Z'), ('F', 'P'), ('F', 'D'),
            ('P', 'F'), ('P', 'Z'), ('P', 'G'), ('P', 'C'), ('P', 'E'), ('P', 'O'), ('P', 'D'),
            ('C', 'P'), ('C', 'G'), ('C', 'N'), ('C', 'W'), ('C', 'E'),
            ('E', 'P'), ('E', 'C'), ('E', 'W'), ('E', 'T'), ('E', 'S'), ('E', 'O'),
            ('W', 'C'), ('W', 'N'), ('W', 'B'), ('W', 'L'), ('W', 'T'), ('W', 'E'),
            ('L', 'W'), ('L', 'B'), ('L', 'R'), ('L', 'T'),
            ('D', 'F'), ('D', 'P'), ('D', 'O'),
            ('O', 'D'), ('O', 'P'), ('O', 'E'), ('O', 'S'),
            ('S', 'O'), ('S', 'E'), ('S', 'T'), ('S', 'K'),
            ('T', 'S'), ('T', 'E'), ('T', 'W'), ('T', 'L'), ('T', 'R'), ('T', 'K'),
            ('K', 'S'), ('K', 'T'), ('K', 'R'),
            ('R', 'K'), ('R', 'T'), ('R', 'L')]

    for el in nodes:
        test.insertVertex(node(el))
    for el in graf:
        test.insertEdge(node(el[0]), node(el[1]), 1)
    test.deleteVertex(node("K"))
    test.deleteEdge(node("W"), node("E"))
    polska.draw_map(test.edges())
                    
def main():
    lista_sasiedztwa()
    macierz_sasiedztwa()
    
if __name__ == "__main__":
    main()
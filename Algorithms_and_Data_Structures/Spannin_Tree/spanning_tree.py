from graf_mst import graf

class node:
    def __init__(self, key = None, colour = None):
        self.key = key
        self.colour = colour
        
    def __eq__(self,key):
        if self.key == key:
            return True
        
    def __hash__(self):
        return hash(self.key)
    
    def return_color(self):
        return self.color
    
    def set_color(self, new_color):
        self.color = new_color
    
class edge:
    def __init__(self, parent: node, child: node, weight = None):
        self.parent = parent
        self.child = child
        self.weight = weight
        
class neighList:
    def __init__(self, list = [], mst = []):
        self.dict = {}
        self.list = list  
        self.mst = mst
        
    def insertVertex(self, node: node):
        self.list.append([])
        self.mst.append([])
        self.dict.update({node.key:len(self.list) - 1})
          
    def insertEdge(self, edge: edge):
        if not self.getVertexIdx(node(edge.parent)) in self.list[self.getVertexIdx(node(edge.child))]:
            self.list[self.getVertexIdx(node(edge.child))].append((self.getVertexIdx(node(edge.parent)), edge.weight))
        if not self.getVertexIdx(node(edge.child)) in self.list[self.getVertexIdx(node(edge.parent))]:
            self.list[self.getVertexIdx(node(edge.parent))].append((self.getVertexIdx(node(edge.child)), edge.weight))

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
            
    def deleteEdge(self, edge: edge):
        self.list[self.getVertexIdx(edge.parent)].remove(self.getVertexIdx(edge.child))
        self.list[self.getVertexIdx(edge.child)].remove(self.getVertexIdx(edge.parent))
    
    def getVertexIdx(self, node:node):
        return self.dict[node.key]
    
    def getVertex(self, node_idx):
        for keys, vals in self.dict.items():
            if node_idx == vals:
                return keys
    
    def neighbours(self, node_idx):
        return self.list[node_idx]
    
    def order(self):
        return len(self.list)
    
    def size(self):
        num = self.edges()
        return len(num)//2
    
    def edges(self):
        pairs = []
        for i in range(len(self.dict)):
            for j in self.list[i]:
                pairs.append((self.getVertex(i), self.getVertex(j)))
        return pairs
    
    def __str__(self):
        pr = ""
        for i in range(len(self.list)):
            if self.getVertex(i) != None:
                pr += str(self.getVertex(i)) + ": "
                for j in self.list[i]:
                    pr += str((self.getVertex(j[0]), j[1]))
                pr += "\n"
        return pr
    
    def prim_alg(self, vertex:node, intree = [], distances = [], parent = []):
        intree = [0 for i in range(len(self.list))]
        parent = [-1 for i in range(len(self.list))] 
        distances = [float('inf') for i in range(len(self.list))] 
        vertex_id = self.getVertexIdx(vertex)
        
        while intree[vertex_id] == 0:
            intree[vertex_id] = 1
                 
            for index, tuple in enumerate(self.list[vertex_id]):
                weight = tuple[1]
                target = tuple[0]
                if weight < distances[target] and not intree[target]:
                    distances[target] = weight  
                    parent[target] = vertex_id
                    
            min_edge = float('inf')
            for i in range(len(intree)):
                if intree[i] == 0: 
                   if distances[i] < min_edge:
                        min_edge = distances[i] 
                        min_node = i
            
            if min_edge != float('inf'):
                        
                self.mst[min_node].append((parent[min_node], min_edge))
                self.mst[parent[min_node]].append((min_node, min_edge))
            vertex_id = min_node
                                        
def printGraph(g, l):
    n = l.order()
    print("------GRAPH------",n)
    for i in range(n):
        v = l.getVertex(i)
        print(v, end = " -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(l.getVertex(j), w, end=";")
        print()
    print("-------------------")

def main():
    nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    test = neighList()
    
    for i in nodes:
        test.insertVertex(node(i))
    
    for i in graf:
        test.insertEdge(edge(i[0], i[1], i[2]))
        
    test.prim_alg(node("A"))
    mst = test.mst
    printGraph(neighList(mst), test)

    
if __name__ == "__main__":
    main()
    
    
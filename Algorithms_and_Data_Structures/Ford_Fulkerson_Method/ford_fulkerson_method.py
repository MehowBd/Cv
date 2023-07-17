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
    def __init__(self, parent: node, child: node, capacity = None, flow = 0, isResidual = False):
        self.parent = parent
        self.child = child
        self.residual = capacity
        self.capacity = capacity
        self.flow = flow
        self.isResidual = isResidual
     
    def __repr__(self):
        return str(self.capacity) + " " + str(self.flow) + " " + str(self.residual) + " " + str(self.isResidual)
        
class neighList:
    def __init__(self):
        self.dict = {}
        self.list = []
        self.mst = []
        
    def insertVertex(self, node: node):
        self.list.append([])
        self.mst.append([])
        self.dict[node.key] = len(self.list) - 1
          
    def insertEdge(self, edge: edge):
        self.list[self.getVertexIdx(node(edge.child))].append([self.getVertexIdx(node(edge.parent)), 0, True, edge.flow, 0])
        self.list[self.getVertexIdx(node(edge.parent))].append([self.getVertexIdx(node(edge.child)), edge.residual, edge.isResidual, edge.flow, edge.capacity])

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


def smallest_capacity(lista: neighList, first_vert: node, last_vert: node, parent):
    first_vert_idx = lista.getVertexIdx(first_vert)
    last_vert_idx = lista.getVertexIdx(last_vert)
    smallest_cap = float('inf')
    current_vert_idx = lista.getVertexIdx(last_vert)
    
    if parent[last_vert_idx] == -1:
        return 0
    else:
        while current_vert_idx != first_vert_idx:
            parent_idx = parent[current_vert_idx]
            residual = 0
            
            neighbours = lista.neighbours(parent_idx)
            for neigh in neighbours:
                if neigh[0] == current_vert_idx and neigh[1] < smallest_cap and not neigh[2]:
                    smallest_cap = neigh[1]
            current_vert_idx = parent_idx
            
    return smallest_cap            

def bfs(lista: neighList):
    size = lista.order()
    visited = [0 for i in range(size)]
    parent = [-1 for i in range(size)]
    queue = []
    start_id = 0
    
    queue.append(lista.getVertex(start_id))
    visited[start_id] = 1
        
    while len(queue) > 0:
        start_id = lista.getVertexIdx(node(queue.pop(0)))
        neighbours = lista.neighbours(start_id)
        for neigh in neighbours:    
            if visited[neigh[0]] == 0 and neigh[1] > 0 and not neigh[2]:
                visited[neigh[0]] = 1
                queue.append(lista.getVertex(neigh[0]))
                parent[neigh[0]] = start_id        
    
    return parent


def augmentacja(lista: neighList, first_vert: node, last_vert: node, parent, smallest_cap):
    first_vert_idx = lista.getVertexIdx(first_vert)
    last_vert_idx = lista.getVertexIdx(last_vert)
    current_vert_idx = lista.getVertexIdx(last_vert)
    
    if parent[last_vert_idx] == -1:
        return 0
    else:
        while current_vert_idx != first_vert_idx:
            parent_idx = parent[current_vert_idx]

            neighbours_parent = lista.neighbours(parent_idx)
            for neigh in neighbours_parent:
                if neigh[0] == current_vert_idx and not neigh[2]:
                    neigh[3] += smallest_cap
                    neigh[1] -= smallest_cap
                    
            neighbours_current = lista.neighbours(current_vert_idx)
            for neigh in neighbours_current:
                if neigh[0] == parent_idx and neigh[2]:
                    neigh[1] += smallest_cap
            
            current_vert_idx = parent_idx

def ford_fulkerson_alg(lista: neighList):
    parent = bfs(lista)
    nodes = []
    flow = 0
    for key in lista.dict:
        nodes.append(node(key))
        
    last_idx = lista.getVertexIdx(node('t'))
    if parent[last_idx] == -1:
        return 0
    
    smallest_cap = smallest_capacity(lista, nodes[0], nodes[-1], parent)
    while smallest_cap > 0:
        augmentacja(lista, nodes[0], nodes[-1], parent, smallest_cap)
        parent = bfs(lista)
        smallest_cap = smallest_capacity(lista, nodes[0], nodes[-1], parent)

 
    neighbours = lista.neighbours(last_idx)
    
    for neigh in neighbours:
        flow += neigh[1]
        
    return lista, flow
                           
def printGraph(g):
    n = g.order()
    print("------GRAPH------",n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end = " -> ")
        nbrs = g.neighbours(i)
        for (target,residual , isresidual, flow, capacity) in nbrs:
            if isresidual:
                print(g.getVertex(target) + " " + str(capacity) + " " + str(residual) + " " + str(flow) + " " + str(isresidual), end=";")
            else:
                print(g.getVertex(target) + " " + str(capacity) + " " + str(flow) + " " + str(residual) + " " + str(isresidual), end=";")
        print()
    print("-------------------")
    
def test0():
    graf = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
    nodes = ['s', 'u', 'v', 't']
    test = neighList()
    for i in nodes:
        test.insertVertex(node(i))
    for i in graf:
        test.insertEdge(edge(i[0], i[1], i[2]))
    graph, flow = ford_fulkerson_alg(test)
    print(flow)    
    printGraph(graph)
  
def test1():
    graf = [ ('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]
    nodes = ['s', 'a', 'b', 'c', 'd', 't']
    test = neighList()
    for i in nodes:
        test.insertVertex(node(i))
    for i in graf:
        test.insertEdge(edge(i[0], i[1], i[2]))
    graph, flow = ford_fulkerson_alg(test)
    print(flow)    
    printGraph(graph)  
    
def test2():
    graf = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    nodes = ['s', 'a', 'b', 'c', 'd', 'e', 't']
    test = neighList()
    for i in nodes:
        test.insertVertex(node(i))
    for i in graf:
        test.insertEdge(edge(i[0], i[1], i[2]))
    graph, flow = ford_fulkerson_alg(test)
    print(flow)    
    printGraph(graph)

def test3():
    graf = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7), ('d', 'c', 4)]
    nodes = ['s', 'a', 'b', 'c', 'd', 't']
    test = neighList()
    for i in nodes:
        test.insertVertex(node(i))
    for i in graf:
        test.insertEdge(edge(i[0], i[1], i[2]))
    graph, flow = ford_fulkerson_alg(test)
    print(flow)    
    printGraph(graph)      
        
def main():
    test0()
    test1()
    test2()
    test3()

if __name__ == "__main__":
    main()
    
    
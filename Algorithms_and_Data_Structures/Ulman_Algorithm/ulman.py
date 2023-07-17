from copy import deepcopy
import numpy as np

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
    def __init__(self):
        self.dict = {}
        self.list = []
    
    def insertVertex(self, node: node):
        if self.list == None:
            self.list.append([0])
            self.dict[node.key] = len(self.list) - 1
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
        return list(self.dict.keys())[node_idx]
    
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
    
def ullman_01(used_columns, current_row, G, P, M):
    if current_row == len(M):
        if np.array_equal(P, np.dot(M, np.transpose(np.dot(M,G)))): #czy jest izomorfizmem
            ullman_01.num_iso += 1
            return True
        
    M_ = deepcopy(M)
    
    for i in range(len(used_columns)):
        if used_columns[i] == 0 and current_row < M.shape[0]:
            for j in range(M.shape[1]):
                if used_columns[j] == 0:
                    M_[current_row, j] = 0
            M_[current_row, i] = 1
            used_columns[i] = 1
            ullman_01.no_recursion += 1
            ullman_01(used_columns, current_row+1, G, P, M_) 
            used_columns[i] = 0
    return False

def ullman_02(used_columns, current_row, G, P, M):
    if current_row == len(M):
        if np.array_equal(P, np.dot(M, np.transpose(np.dot(M,G)))): #czy jest izomorfizmem
            ullman_02.num_iso += 1
            return True
    
    M_ = deepcopy(M)
    M0 = deepcopy(M)
    
    for i in range(P.shape[0]):
        for j in range(G.shape[0]):
            if sum(G[j]) >= sum(P[i]):
                M0[i, j] = 1
                

    for i in range(len(used_columns)):
        if used_columns[i] == 0 and current_row < M.shape[0] and M0[current_row, i] == 1:
            for j in range(M.shape[1]):
                if used_columns[j] == 0:
                    M_[current_row, j] = 0
            M_[current_row, i] = 1
            used_columns[i] = 1
            ullman_02.no_recursion += 1
            ullman_02(used_columns, current_row+1, G, P, M_)
            used_columns[i] = 0
    return False

def prune(current_row, G, P, M):
    term = False
    
    while term == False:
        is_changed = False
        
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                if M[i, j] == 1:
                    for p_i in range(P.shape[0]):
                        if P[i, p_i] >= 1:
                            for g_i in range(G.shape[0]):
                                if G[j, g_i] == 0 and M[p_i, g_i] == 1:
                                   M[i, j] = 0
                                   is_changed = True 
        if not is_changed:
            term = True
    
    for i in M[:current_row]:
        if (i == 0).all():
            return False
    return True

def ullman_03(used_columns, current_row, G, P, M):
    if current_row == len(M):
        if np.array_equal(P, np.dot(M, np.transpose(np.dot(M,G)))): #czy jest izomorfizmem
            ullman_03.num_iso += 1
            return True
    
    M_ = deepcopy(M)
    M0 = deepcopy(M)
    
    for i in range(P.shape[0]):
        for j in range(G.shape[0]):
            if sum(G[j]) >= sum(P[i]):
                M0[i, j] = 1
                
    switch = prune(current_row, G, P, M_)
    
    if not switch:
        return False

    for i in range(len(used_columns)):
        if used_columns[i] == 0 and current_row < M.shape[0] and M0[current_row, i] == 1:
            for j in range(M.shape[1]):
                if used_columns[j] == 0:
                    M_[current_row, j] = 0
            M_[current_row, i] = 1
            used_columns[i] = 1
            ullman_03.no_recursion += 1
            ullman_03(used_columns, current_row+1, G, P, M_)
            used_columns[i] = 0
    return False

def main():
    P = neighMatrice()
    G = neighMatrice()
    graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
    graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]
    nodes_G = ['A', 'B', 'C', 'D', 'E', 'F']
    nodes_P = ['A', 'B', 'C']
    
    for i in nodes_G:
        G.insertVertex(node(i))
    for i in graph_G:
        G.insertEdge(node(i[0]), node(i[1]), i[2])
    
    for i in nodes_P:
        P.insertVertex(node(i))
    for i in graph_P:
        P.insertEdge(node(i[0]), node(i[1]), i[2])    

    edges_P = P.edges()
    edges_G = G.edges()
    array_P = np.array(P.list)
    array_G = np.array(G.list)

    M = np.zeros((len(array_P[0]), len(array_G[0])))
    used_columns = [0 for i in range(np.shape(array_G)[0])]

    ullman_01.num_iso = 0
    ullman_01.no_recursion = 0
    ullman_01(used_columns, 0, array_G, array_P, M)
    print(ullman_01.num_iso, ullman_01.no_recursion)
    
    ullman_02.num_iso = 0
    ullman_02.no_recursion = 0    
    ullman_02(used_columns, 0, array_G, array_P, M)
    print(ullman_02.num_iso, ullman_02.no_recursion)
    
    ullman_03.num_iso = 0
    ullman_03.no_recursion = 0    
    ullman_03(used_columns, 0, array_G, array_P, M)
    print(ullman_03.num_iso, ullman_03.no_recursion)
    
    
if __name__ == "__main__":
    main()
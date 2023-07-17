import random
import time

class node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        
    def  __lt__(self, val):
        if self.priority < val:
            return True
        else:
            return False
    
    def  __gt__(self, val):
        if self.priority > val:
            return True
        else:
            return False
            
    def __str__(self):
        return str(self.priority) + ":" + str(self.data)
        
class queue:
    def __init__(self, size = 0):
        self.size = size
        self.len = size
        self.tab = [None for i in range(self.size-1)]
    
    def is_empty(self):
        if self.size == 0:
            return True
        
    def peek(self):
        return self.tab[0].data
    
    def parent(self, node: node):
        return (self.tab.index(node)-1)//2
    
    def left(self, node: node):
        return self.tab.index(node)*2+1
    
    def right(self, node: node):
        return self.tab.index(node)*2+2
        
    def swap(self, node1: node, node2: node):
        self.tab[self.tab.index(node1)], self.tab[self.tab.index(node2)] = self.tab[self.tab.index(node2)], self.tab[self.tab.index(node1)]
        
    def enqueue(self, node: node):
        self.size += 1
        self.len += 1
        self.tab.append(node)
        i = self.size-1
        
        while True:
            if self.tab[i].priority < self.tab[self.parent(self.tab[i])].priority:
                break
            if self.tab[i].priority > self.tab[self.parent(self.tab[i])].priority: 
                self.swap(self.tab[i], self.tab[self.parent(self.tab[i])])
            else:  
                break
            
    def dequeue(self):
        if self.is_empty():
            return None
        deleted = self.tab[0]
        self.tab[self.len-1], self.tab[0] = self.tab[0], self.tab[self.len-1]
        self.len -= 1
        self.down(0)
        return deleted.data
    
    def down(self, i):
        id = i
        
        left = self.left(self.tab[i])
        right = self.right(self.tab[i])
        
        if i < self.len:
            if right <= self.len and self.tab[right].priority > self.tab[id].priority:
                id = right
                
            if left <= self.len and self.tab[left].priority > self.tab[id].priority:
                id = left
                
            if i != id:
                self.tab[i], self.tab[id] = self.tab[id], self.tab[i]
                self.down(id)     
                
    def heapify(self):
        for i in range(self.size):
            self.dequeue()
    
    def print_tab(self):
        if self.is_empty():
            print("{ }")
            return
        print ('{', end=' ')
        for i in range(self.size-1):
            print(self.tab[i], end = ', ')
        if self.tab[self.size-1]: print(self.tab[self.size-1] , end = ' ')
        print( '}')

    def print_tree(self, idx, lvl):
        if idx<self.size:           
            self.print_tree(self.right(self.tab[idx]), lvl+1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)           
            self.print_tree(self.left(self.tab[idx]), lvl+1)
            
class element:
    def __init__(self, priority, data):
        self.priority = priority
        self.data = data
        
    def  __lt__(self, priority_n):
        if self.priority < priority_n:
            return True
        else:
            return False
    
    def  __gt__(self, priority_n):
        if self.priority > priority_n:
            return True
        else:
            return False   
    
    def __str__(self):
        pr = "(" + str(self.priority) + "," + self.data + ")"
        return pr
        
        
class selection_table:
    def __init__(self):
        self.list = []
    
    def append(self, element: element):
        self.list.append(element)
        
    def insert(self, id:int, element:element):
        self.list.insert(id, element)
    
    def pop(self, id:int):
        self.list.pop(id)
    
    def __len__(self):
        return len(self.list)
    
    def __getitem__(self, id):
        return self.list[id]
 
    def __setitem__(self, id, value):
        self.list[id] = value
            
    def index_min(self, m):
        list_id = []
        for i in self.list:
            list_id.append(i.priority)
        end_list = list_id[m: ]
        min_id = end_list.index(min(end_list)) + m
        return min_id    
   
    def swap(self, id1:int, id2:int):
        self.list[id1], self.list[id2] = self.list[id2], self.list[id1]
    
    def __str__(self):
        pr = "["
        for i in range(len(self.list)):
            pr += str(self.list[i]) + ","
        pr_ = pr[:-1]
        pr_ += "]"
        return pr_
        
def selection_sort_swap(list:selection_table):
    for i in range(0, len(list)-1):
        m = list.index_min(i)
        list.swap(i, m)
    return list

def selection_sort_shift(list:selection_table):
    for i in range(0, len(list)-1):
        m = list.index_min(i)
        first_el = list[i]
        second_el = list[m]
        list.pop(i)
        list.insert(i, second_el)
        list.pop(m)
        list.insert(m, first_el)
    return list


def first_test_selection():
    dane = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    test_sw = selection_table()
    test_sh = selection_table()
    for i in dane:
        test_sw.append(element(i[0], i[1]))
        test_sh.append(element(i[0], i[1]))
    
    t_start_sw = time.perf_counter()
    print(test_sw)
    print(selection_sort_swap(test_sw))
    t_stop_sw = time.perf_counter()
    
    t_start_sh = time.perf_counter()
    print(test_sh)
    print(selection_sort_shift(test_sh))
    t_stop_sh = time.perf_counter()
    
    print("Czas obliczeń dla swap:", "{:.7f}".format(t_stop_sw - t_start_sw))
    print("Czas obliczeń dla shift:", "{:.7f}".format(t_stop_sh - t_start_sh))
    
def second_test_selection():
    test_sh = selection_table()
    test_sw = selection_table()
    
    for i in range(0, 10000):
        test_sh.append(element(int(random.random() * 1000), None))
        test_sw.append(element(int(random.random() * 1000), None))

        
    t_start_sw = time.perf_counter()
    selection_sort_swap(test_sw)
    t_stop_sw = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop_sw - t_start_sw))

    t_start_sh = time.perf_counter()
    selection_sort_shift(test_sh)
    t_stop_sh = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop_sh - t_start_sh))    

def first_test_heapify():
    dane = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    test = queue()
    
    for i in range(0, len(dane)):
        test.enqueue(node(dane[i][1], dane[i][0]))
        
    test.print_tree(0, 0)
    test.print_tab()
    
    t_start = time.perf_counter()
    test.heapify()
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    test.print_tree(0, 0)
    test.print_tab()
    
def second_test_heapify():
    test = queue()
    
    for i in range(10000):
        test.enqueue(node(None, int(random.random() * 1000)))

    t_start = time.perf_counter()
    test.heapify()
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    

def main():

    first_test_selection()
    second_test_selection()
    first_test_heapify()
    second_test_heapify()
if __name__ == "__main__":
    main()
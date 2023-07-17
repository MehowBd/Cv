class element:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __lt__(self, val):
        if self.data < val:
            return True
        else:
            return False

    def __gt__(self, val):
        if self.data > val:
            return True
        else:
            return False

    def __str__(self):
        return str(self.priority) + ":" + str(self.data)


class queue:
    def __init__(self, size=0):
        self.size = size
        self.tab = [None for i in range(self.size - 1)]

    def is_empty(self):
        if self.size == 0:
            return True

    def peek(self):
        return self.tab[0].data

    def parent(self, node: element):
        return (self.tab.index(node) - 1) // 2

    def left(self, node: element):
        return self.tab.index(node) * 2 + 1

    def right(self, node: element):
        return self.tab.index(node) * 2 + 2

    def swap(self, node1: element, node2: element):
        self.tab[self.tab.index(node1)], self.tab[self.tab.index(node2)] = self.tab[self.tab.index(node2)], self.tab[self.tab.index(node1)]

    def enqueue(self, node: element):
        self.size += 1
        self.tab.append(node)
        i = self.size - 1
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
        self.tab[0] = self.tab[self.size-1]
        self.size -= 1
        self.down(0)
        return deleted.data

    def down(self, i):
        id = i

        left = self.left(self.tab[i])
        right = self.right(self.tab[i])

        if right < self.size and self.tab[right].priority > self.tab[id].priority:
            id = right
        if left < self.size and self.tab[left].priority > self.tab[id].priority:
            id = left

        if i != id:
            self.tab[i], self.tab[id] = self.tab[id], self.tab[i]
            self.down(id)

    def print_tab(self):
        if self.is_empty():
            print("{ }")
            return
        print('{', end=' ')
        for i in range(self.size - 1):
            print(self.tab[i], end=', ')
        if self.tab[self.size - 1]: print(self.tab[self.size - 1], end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.size:
            self.print_tree(self.right(self.tab[idx]), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(self.tab[idx]), lvl + 1)


if __name__ == "__main__":
    algorytm = "ALGORYTM"
    tab = [4, 7, 6, 7, 5, 2, 2, 1]
    test = queue()
    for i in range(len(tab)):
        test.enqueue(element(algorytm[i], tab[i]))
    test.print_tree(0, 0)
    test.print_tab()

    print(test.dequeue())
    print(test.peek())

    test.print_tab()

    while not test.is_empty():
        print(test.dequeue())

    test.print_tab()
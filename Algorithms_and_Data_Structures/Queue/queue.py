#skończone



class queue:
    def __init__(self, size = 5, recordID = 0, readID = 0):
        self.size = size
        self.recordID = recordID
        self.readID = readID
        self.tab = [None for i in range(self.size)]

    def is_empty(self):
        if self.recordID == self.readID:
            return True
        else:
            return False


    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[self.readID]

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            deq = self.tab[self.readID]
            self.readID += 1
            if self.readID == self.size:
                self.readID = 0
                return deq
            else:
                return deq

    def enqueue(self, data):
        self.tab[self.recordID] = data
        self.recordID += 1
        
        if self.recordID == self.size:
            self.recordID = 0

        if self.recordID == self.readID:
            old_size = self.size
            self.size *= 2
            self.tab = realloc(self.tab, self.size)

            for i in range(self.recordID):
                self.tab[old_size+i] = self.tab[i]

            self.recordID += old_size

    def print_queue(self):
        pr = "["
        for i in range(self.readID, self.recordID):
            if i < self.recordID-1:
                pr += str(self.tab[i]) + " "
            if i == self.recordID-1:
                pr += str(self.tab[i])
        pr += "]"
        print(pr)

    def print_tab(self):
        pr = "["
        for i in range(self.size):
            if i < self.size-1:
                pr += str(self.tab[i]) + ", "
            if i == self.size-1:
                pr += str(self.tab[i]) + "]"
        print(pr)


def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i < oldSize else None for i in range(size)]


def main():

    example = queue()
    for i in range(1, 5):
        example.enqueue(i)
    example.print_tab()
    example.print_queue()
    print(example.dequeue())
    print(example.peek())
    
    example.print_queue()

    for i in range(5, 9):
        example.enqueue(i)
    
    example.print_tab()
    
    while example.is_empty() == False:
        print(example.dequeue())
    
    example.print_queue()
    
if __name__ == "__main__":
    main()
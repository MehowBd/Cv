#skonczone
class Single_linked_list:

    def __init__(self, head = None):
        self.head = head

    def add(self, data):
        new_data = element(data)
        new_data.next = self.head
        self.head = new_data

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def destroy(self):
        self.head = None

    def remove(self):
        self.head = self.head.next

    def is_empty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False

    def length(self):
        counter = 0
        current = self.head
        while current:
            counter += 1
            current = current.next
        return counter

    def get(self):
        return self.head.data

    def add_tail(self, new_element):
        new_node = element(new_element)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_tail(self):
        current = self.head
        while current.next:
            previous = current
            current = current.next
        previous.next = None
            
    def take(self, n):
        current = self.head
        counter = 0
        New_Single_linked_list = Single_linked_list()
        while counter < n:
            counter += 1
            New_Single_linked_list.add_tail(current.data)
            current = current.next 
        return New_Single_linked_list

    def drop(self, n):
        if n > self.length():
            return Single_linked_list()
        else:
            counter = 0
            current = self.head
            New_Single_linked_list = Single_linked_list()
            while current.next:
                counter += 1
                current = current.next
                if counter >= n:
                    New_Single_linked_list.add_tail(current.data)
            return New_Single_linked_list

class element:

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


def main():

    dane = [('AGH', 'Kraków', 1919),
    ('UJ', 'Kraków', 1364),
    ('PW', 'Warszawa', 1915),
    ('UW', 'Warszawa', 1915),
    ('UP', 'Poznań', 1919),
    ('PG', 'Gdańsk', 1945)]

    list = Single_linked_list()

    for data in dane[::-1]:
       list.add(data)

    list.print_list()
    print("\n")

    print("Metoda lenght: ")
    print(list.length(), "\n")

    print("Metoda get:  ")
    print(list.get(), "\n")

    print("Metoda add_tail: ")
    list.add_tail(("AWF", "Kraków", 1951))
    list.print_list()
    print("\n")

    print("Metoda remove_tail: ")
    list.remove_tail()
    list.print_list()
    print("\n")

    new_take = list.take(3)
    new_drop = list.drop(4)

    print("Metoda take(3) i drop(4): ")

    new_take.print_list()
  
    print("\n")

    new_drop.print_list()

    print("\n")

    print("Metoda destroy i is_empty:")
    list.destroy()
    list.print_list()
    print(list.is_empty())

    print("\n")

if __name__ == '__main__':
    main()
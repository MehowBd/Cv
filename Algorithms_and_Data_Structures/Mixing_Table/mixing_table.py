import string

class element:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
class hash_table:
    def __init__(self, size, c1=1, c2=0):
        self.c1 = c1
        self.c2 = c2
        self.size = size
        self.tab = [None for i in range(self.size)]
        
    def hashing(self, key):
        if isinstance(key, int):
            return key % self.size
        if isinstance(key, str):
            hashsum = 0
            for i, letter in enumerate(key):
                hashsum += ord(letter)
            return hashsum % self.size
        
    def search(self, key):
        found = False
        hash_key = self.hashing(key)
        
        for i in range(self.size):
            if self.tab[hash_key] != None:
                if self.tab[hash_key].key == key:
                    found = True
                    break
            hash_key = (hash_key + self.c1*i + self.c2*i**2) % self.size
        
        if self.tab[hash_key] != None:
                if self.tab[hash_key].key == key:
                    found = True
        
        if found == True:
            return self.tab[hash_key].value
        else:
            return None

    def insert(self, data: element):
        hash_key = self.hashing(data.key)
        counter = 0
        if self.tab[hash_key] == None:
            self.tab[hash_key] = data
            return

        if self.search(data.key) == None:
            new_hash = hash_key
            while self.tab[new_hash] != None and self.tab[new_hash].key != data.key:
                new_hash = (hash_key + self.c1*counter + self.c2*counter**2) % self.size
                counter += 1
                if counter > self.size+1:
                    print("Brak miejsca")
                    break
            self.tab[new_hash] = data
            return

        if counter > self.size+1:
            return None
    

        for i in range(self.size):
            if self.tab[i] != None:
                if self.tab[i].key == data.key:
                    self.tab[i].value = data.value
                    break

        if not None in self.tab:
            print("Brak miejsca")
            return
        
    def remove(self, key):
        hash_key = self.hashing(key)
        if self.search(hash_key) == None:
            print("Brak danej")
            return
        for i in range(self.size):
            if self.tab[i] != None:
                if self.tab[i].key == key:
                    self.tab[i] = None
                    return
         

    def __str__(self):
        pr = "{"
        for i in range(self.size):
            if self.tab[i] == None:
                pr += "None, "
            else:
                pr += str(self.tab[i].key) + ":\"" + str(self.tab[i].value) + "\", "
        pr_new = pr[:-2]
        pr_new += "}"
        return pr_new

def test1(size = 13, c1 = 1, c2 = 0):
    alphabet = list(string.ascii_uppercase)
    test = hash_table(size, c1, c2)
    for i in range(1, 16):
        if i == 6:
            test.insert(element(18, alphabet[i-1]))
        elif i == 7:
            test.insert(element(31, alphabet[i-1]))
        else:
            test.insert(element(i, alphabet[i-1]))
            
    print(test)
    print(test.search(5))
    print(test.search(14))
    test.insert(element(5, "Z"))
    print(test.search(5))
    test.remove(5)
    print(test)
    print(test.search(31))
    test.insert(element("test", "W"))
    print(test)

def test2(size = 13, c1 = 1, c2 = 0):
    alphabet = list(string.ascii_uppercase)
    test = hash_table(size, c1, c2)
    for i in range(1, 16):
        test.insert(element(i*13, alphabet[i-1]))
    print(test)

def test3(size = 13, c1 = 0, c2 = 1):
    alphabet = list(string.ascii_uppercase)
    test = hash_table(size, c1, c2)
    for i in range(1, 16):
        test.insert(element(i*13, alphabet[i-1]))
    print(test)

def main():
    test1()
    test2()
    test3()
if __name__ == "__main__":
    main()
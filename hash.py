class HashTable(object) :
    #Initialize the hash table
    def __init__(self) :
        self.size = 10
        self.keys = [None]*self.size
        self.values = [None]*self.size
    #Define a hash fucntion to map keys
    def hashFunction(self,key) :
        sum = 0
        for pos in range(len(key)) :
            sum = sum + ord(key[pos])
        return sum%self.size
    #Insert value into hash table o(1)
    def put(self, key, data) :
        index = self.hashFunction(key)
        while self.keys[index] is not None :
            if self.keys[index] == key :
                self.values[index] = data
                return
            index = ( index + 1 ) % self.size
        self.keys[index] = key
        self.values[index] = data
    #Get a value for the particular key o(1)
    def get(self, key) :
        index = self.hashFucntion(key)
        while self.keys[index] is not None :
            if self.keys[index] == key :
                return self.values[index]
            index = ( index + 1 ) % self.size
        return None

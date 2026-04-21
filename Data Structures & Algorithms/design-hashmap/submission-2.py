class MyHashMap:
    def __init__(self):
        # A common practice is to use a prime number for size
        self.size = 2069 
        # Initialize the main array with empty lists (buckets/chains)
        self.map = [[] for _ in range(self.size)] 

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        bucket = self.map[index]
        
        # Search for the key within the bucket to update it
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i][1] = value
                return
        
        # If not found, append the new pair to the bucket
        bucket.append([key, value])

    def get(self, key: int) -> int:
        index = self._hash(key)
        bucket = self.map[index]
        
        # Search for the key within the bucket
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        
        # Key not found
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.map[index]
        
        # Search for the key within the bucket by index for safe removal
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
class MyHashSet:

    def __init__(self):
        self.size = 2069
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        bucket = self.buckets[key%2069]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.buckets[key%2069]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        bucket = self.buckets[key%2069]

        return key in bucket


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
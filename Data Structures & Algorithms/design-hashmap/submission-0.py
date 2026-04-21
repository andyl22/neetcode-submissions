class MyHashMap:
    def __init__(self):
        self.list = []

    def put(self, key: int, value: int) -> None:
        for v in self.list:
            if v[0] == key:
                v[1] = value
                return
        self.list.append([key, value])

    def get(self, key: int) -> int:
        for v in self.list:
            if v[0] == key:
                return v[1]
        return -1


    def remove(self, key: int) -> None:
        for i in range(len(self.list)):
            if self.list[i][0] == key:
                self.list.pop(i)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
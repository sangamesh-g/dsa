class MyHashSet:

    def __init__(self):
        self.bucket=[[] for _ in range(10000)]
        

    def add(self, key: int) -> None:
        index=key%10000
        if key not in self.bucket[index]:
            self.bucket[index].append(key)

    def remove(self, key: int) -> None:
        index=key%10000
        if key in self.bucket[index]:
            self.bucket[index].remove(key)        

    def contains(self, key: int) -> bool:
        index=key%10000
        return True if key in self.bucket[index] else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
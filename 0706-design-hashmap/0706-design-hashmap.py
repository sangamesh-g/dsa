class MyHashMap:

    def __init__(self):
        self.bucket=[[] for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        index=key%1000
        flag=True
        for k in range(len(self.bucket[index])):
            if self.bucket[index][k][0]==key:
                self.bucket[index][k][1]=value
                flag=False
                break
        if flag:
            self.bucket[index].append([key,value])
        print(self.bucket[index])

    def get(self, key: int) -> int:
        index=key%1000
        for k in self.bucket[index]:
            if k[0]==key:
                return k[1]
        return -1       

    def remove(self, key: int) -> None:
        index=key%1000
        for k in self.bucket[index]:
            if k[0]==key:
                self.bucket[index].remove(k)
                break    
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
class MyHashSet:

    def __init__(self):
        # Initialize an empty set
        self.hash_set = set()       

    def add(self, key: int) -> None:
        # Sets use .add()
        self.hash_set.add(key)

    def remove(self, key: int) -> None:
        # .discard() prevents an error if the key isn't present
        self.hash_set.discard(key)

    def contains(self, key: int) -> bool:
        # This part was already correct!
        return key in self.hash_set
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
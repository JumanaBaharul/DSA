class Node:
    def __init__(self, key:int, value: int):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.map={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def get(self, key: int) -> int:
        if key in self.map:
            node=self.map[key]
            self._remove(node)
            self._insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._remove(self.map[key])
        if len(self.map)==self.capacity:
            self._remove(self.tail.prev)
        self._insert(Node(key,value))

    def _remove(self, node:Node):
        del self.map[node.key]
        node.prev.next=node.next
        node.next.prev=node.prev
    
    def _insert(self, node:Node):
        self.map[node.key]=node
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class ListNode:
    def __init__(self, value, key):
        self.next = None
        self.prev = None
        self.val = value
        self.key = key

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.cap = capacity
        self.map = dict()
        self.head = ListNode(None, None) # a two-way linked list in which head.next is the LRU and tail.prev is MRU.
        self.tail = ListNode(None, None) #
        self.head.next = self.tail
        self.tail.prev = self.head

    # @return an integer
    def get(self, key):
        if key not in self.map:
            return -1
        else:
            node = self.map[key]
            self._remove(node) # remove from its current place
            self._add(node) # add it back to the tail as MRU
            return node.val
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.map: # Change the value of an existing node, no need to check capacity violation
            node_old = self.map[key]
            self._remove(node_old)
        elif self.cap <= len(self.map): # This is a new key and the capacity is reached, need to remove LRU before adding new
            node_LRU = self.head.next
            self._remove(node_LRU)
            del self.map[node_LRU.key] # delete the key from the memory map
        node_new = ListNode(value, key)
        self._add(node_new)
        self.map[key] = node_new
                
    # Add a new node to the linked list (at the end)
    def _add(self, node):
        node_prev = self.tail.prev
        node_prev.next = node
        node.next = self.tail
        node.prev = node_prev
        self.tail.prev = node        
    
    # Remove any node from the linked list
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

if __name__ == "__main__":
    c = LRUCache(4)
    

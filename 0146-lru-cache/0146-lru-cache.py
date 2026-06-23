class Node:
    def __init__(self,key=0, val=0, left_ptr= None, right_ptr=None):
        self.key= key
        self.val = val
        self.prev= left_ptr
        self.next = right_ptr
#we r building a doubly linked list with both side ptrs
#head will always point to the recently used
#tail least recently used

#get is just checking hashmap
#put:
"""
two scenarios
s1: If key exists, just go to that particluar node, remove the node, attach it to head
scenario 2: while adding check:
            1. if there is space, create the node and attach it to head
            2. No space: remove the node to the left of tail, create and attach it to head
"""

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail= Node()
        self.head.next = self.tail
        self.tail.prev= self.head
        self.lookup= {} #lookup is a key: node_address

    def get(self, key: int) -> int:
        #a simple hashmap can do o(1) 
        if key in self.lookup:

            self.remove(self.lookup[key])
            self.add(self.lookup[key]) #always next to head
            return self.lookup[key].val
        else:
            return -1

    def add(self,node):
        #always add the node next to head
        """
        head node1
        head node node1
        """
        old_node = self.head.next
        self.head.next = node
        node.next = old_node
        node.prev = self.head
        old_node.prev = node
    
    def remove(self, node):
        #this node can be anywhere
        #remove this node
        # node1 node node2
        #node1 -> <- node2
        node1=node.prev
        node2 = node.next
        node1.next= node2
        node2.prev = node1

    def put(self, key: int, value: int) -> None:
        #whenevr we update it becomes the recently used
        #we need a structure that can give us freq and less freq used key in O(1) 
        new_node = Node(key, value)
        if key in self.lookup:
            #remove the node
            self.remove(self.lookup[key])
           
            self.add(new_node)
            self.lookup[key]= new_node
        
        else:
            #if there is capacity
            if len(self.lookup)< self.capacity:
         
                self.add(new_node)
                self.lookup[key] = new_node
            else:
                del self.lookup[self.tail.prev.key]
                self.remove(self.tail.prev) #remove the least fre ues
                self.add(new_node)
                self.lookup[key]= new_node
    



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
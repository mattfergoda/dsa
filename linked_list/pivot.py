class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f'Node with value {self.value}'


class LinkedList:

    def __init__(self, head: Node = None):
        self.head = head
        self.length = 1

    def append(self, node: Node):
        current = self.head

        while current.next:
            current = current.next

        current.next = node
        self.length += 1

    def delete(self, val):
        if self.head.value == val:
            self.head = self.head.next
            self.length -= 1
            return
        
        current = self.head.next
        previous = self.head
        while current:
            if current.value == val:
                previous.next = current.next
                self.length -= 1
                return
            else:
                previous = current
                current = current.next


    def to_array(self):
        vals = []
        current = self.head
        while current:
            vals.append(current.value)
            current = current.next

        return vals
    
    def pivot(self, val):

        current = self.head
        i = 0
        while i < self.length:
            if current.value >= val:
                self.delete(current.value)
                self.append(Node(current.value))
            current = current.next
            i += 1


if __name__ == "__main__":
    ll = LinkedList(Node(1))
    ll.append(Node(3))
    ll.append(Node(5))


    print(f"Testing delete with LL {ll.to_array()}")
    ll.delete(3)
    if ll.to_array() == [1,5]:
        print("Success!!")
    else:
        print(f"ERROR with delete! Array should be [1,5] but got {ll.to_array()}")

    ll.append(Node(2))
    ll.append(Node(3))
    ll.append(Node(9))
    ll.append(Node(1))
    ll.append(Node(1))

    print(f"Testing pivot with LL {ll.to_array()}")
    ll.pivot(5)
    if ll.to_array() == [1,2,3,1,1,5,9]:
        print("Success!!")
    else:
        print(f"ERROR with delete! Array should be [1,2,3,1,1,5,9] but got {ll.to_array()}")
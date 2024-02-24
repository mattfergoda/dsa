class Node:

        def __init__(self, value, next=None):

            self.value = value
            self.next = next

class LinkedList:
        
    def __init__(self, head: Node):
        self.head = head
        self.length = 0

    def append(self, val):
        current = self.head

        while current.next:
            current = current.next

        current.next = Node(val)
        self.length += 1

    def to_array(self):
        vals = []
        current = self.head

        while current:
            vals.append(current.value)
            current = current.next

        return vals

    def reverse(self):

        previous = None
        current = self.head


        while current:
            next = current.next # Store next value
            current.next = previous # Reverse this link
            previous = current # Update the previous value for next round
            current = next # Move ahead in the link

        # Current is null.
        self.head = previous


if __name__ == "__main__":
    ll = LinkedList(Node(1))
    ll.append(2)
    ll.append(3)
    ll.reverse()

    if ll.to_array() == [3,2,1]:
        print("SUCCESS!")
    else:
        print("ERROR!")
        print(f"Linked list is {ll.to_array()} but should be [3,2,1]")


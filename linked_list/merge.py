class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f'Node with value {self.value}'


class LinkedList:

    def __init__(self, head: Node = None):
        self.head = head
        self.length = 0

    def append(self, node: Node):
        current = self.head

        while current.next:
            current = current.next

        current.next = node
        self.length += 1

    def to_array(self):
        vals = []
        current = self.head
        while current:
            vals.append(current.value)
            current = current.next

        return vals

    @classmethod
    def merge(self, ll1: 'LinkedList', ll2: 'LinkedList'):
        ll1_current = ll1.head
        ll2_current = ll2.head
        if ll1_current.value > ll2_current.value:
            head = ll2_current
            ll2_current = ll2_current.next
        else:
            head = ll1_current
            ll1_current = ll1_current.next

        new_ll = LinkedList(Node(head.value))

        while ll1_current and ll2_current:
            if ll1_current.value > ll2_current.value:
                new_ll.append(Node(ll2_current.value))
                ll2_current = ll2_current.next
            else:
                new_ll.append(Node(ll1_current.value))
                ll1_current = ll1_current.next

        if ll1_current:
            new_ll.append(ll1_current)
        else:
            new_ll.append(ll2_current)

        return new_ll


if __name__ == "__main__":
    ll_1 = LinkedList(Node(1))
    ll_1.append(Node(3))
    ll_1.append(Node(5))

    ll_2 = LinkedList(Node(2))
    ll_2.append(Node(4))
    ll_2.append(Node(6))

    merged_ll = LinkedList.merge(ll_1, ll_2)
    merged_arr = merged_ll.to_array()

    if merged_arr == [1,2,3,4,5,6]:
        print("Success!!")
    else:
        print(f"ERROR! Array should be [1,2,3,4,5,6] but got {merged_arr}")
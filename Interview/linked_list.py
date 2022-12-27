class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Create Singly Linked List
class LinkedList:
    def __init__(self, val):
        self.head = ListNode(val)
        self.tail = self.head

    # Add one node
    def insertEnd(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    # Remove specific node
    def remove(self, num):
        i = 0
        curr = self.head
        while i < num and curr != None:
            i += 1
            curr = curr.next
            
        if curr:
            curr.next = curr.next.next

    def iterate(self):
        curr = self.head
        while curr:
            print(curr.val, '->', end='')
            curr = curr.next
        print()

test = LinkedList(7)
test.insertEnd(4)
test.insertEnd(5)
test.insertEnd(6)
test.iterate()

temp = test.head
val = 7
while temp and temp.next:
    print(temp.val)
    if temp.next.val == val:
        temp.next = temp.next.next
    else:
        temp = temp.next

test.iterate()


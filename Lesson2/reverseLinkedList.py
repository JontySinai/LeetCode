"""
Reverse a linked list
"""

class Node:
    """
    Base class for linked lists
    """

    def __init__(self,val):
        self.val = val
        self.next = None # the pointer initially points to nothing

"""Test case
1 -> 2 -> 3 -> 4 -> None
"""

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

test = node1

short1 = Node(1)
short2 = Node(2)

short1.next = short2
short = short1

def printList(head):
    """
    prints values in order of a linked list
    """
    node = head
    s = str(node.val)
    while node:
        if node.next:
            s = s + ' -> ' + str(node.next.val)
        node = node.next

    print(s)



def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    prev = None
    node = head
    nxt = None

    while node:
        nxt = node.next # forward look
        node.next = prev # reverse
        # move forward one iteration
        prev = node
        node = nxt

    return prev


printList(test)
reverse = reverseList(test)
printList(reverse)

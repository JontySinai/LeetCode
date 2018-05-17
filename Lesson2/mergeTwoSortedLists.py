"""
Merge two sorted linked lists.None

Eg.

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""

class Node:
    """
    Base class for linked lists
    """

    def __init__(self,val):
        self.val = val
        self.next = None # the pointer initially points to nothing



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



"""Test cases
1 -> 2 -> 4
1 -> 3 -> 4

"""

node11 = Node(1)
node12 = Node(2)
node13 = Node(4)

node11.next = node12
node12.next = node13

list1 = node11

node21 = Node(1)
node22 = Node(3)
node23 = Node(4)

node21.next = node22
node22.next = node23

list2 = node21

printList(list1)
printList(list2)


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    if not l1:
        return l2
    if not l2:
        return l1

    node1 = l1
    node2 = l2

    # create two dummy node
    # Note: merged will be linked to the head of temp
    head = merged = Node(None)

    while not (node1 is None or node2 is None):

        if node1.val < node2.val:
            mem = node1 # remember current min
            node1 = node1.next # only move current smallest list at a time
        else:
            mem = node2
            node2 = node2.next
        
        # only increase the merged list after moving forward
        # Rmbr: the merged list is initialised to None
        merged.next = mem
        # and make sure to advance the merged list
        # Else merged will be stuck on None
        merged = merged.next

    merged.next = node1 or node2 #whichever is not none

    # return head of temp
    return head.next


            

mergedList = mergeTwoLists(list1, list2)
printList(mergedList)

            



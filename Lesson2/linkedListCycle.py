"""
Given a linked list, detect if it has a cycle
"""

class Node:
    """
    Base class for linked lists
    """

    def __init__(self,val):
        self.val = val
        self.next = None # the pointer initially points to nothing


"""Test case 1:

1 -> 2 -> 3 -> 4
          ^    |
          |    v
          6 <- 5

"""

cycle1 = Node(1)
cycle2 = Node(2)
cycle3 = Node(3)
cycle4 = Node(4)
cycle5 = Node(5)
cycle6 = Node(6)

cycle1.next = cycle2
cycle2.next = cycle3
cycle3.next = cycle4
cycle4.next = cycle5
cycle5.next = cycle6
cycle6.next = cycle3

cycle = cycle1

"""Test case 2:

1 -> 2 -> 3 -> 4 -> 5

"""

straight1 = Node(1)
straight2 = Node(2)
straight3 = Node(3)
straight4 = Node(4)
straight5 = Node(5)

straight1.next = straight2
straight2.next = straight3
straight3.next = straight4
straight4.next = straight5

straight = straight1


def hasCycle(head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        visits = {}
        step = head
        
        while step != None:
            
            if step in visits:
                return True
            
            visits.update({step: step.val})
            
            step = step.next
            
        return False

ans = hasCycle(cycle)
print(ans)

ans2 = hasCycle(straight)
print(ans2)

def TortoiseHare(head):
    """
    :type head: ListNode
    :rtype: bool

    Implements Floyd's cycle-finding algorithm using the Tortoise and Hare analogy:

    - Fast and Slow both start at the head.
    - Fast jumps two hops at every iteration while Slow jumpst one hop
    - Fast will catch up with Slow if there is cycle eventually
    - Else Fast and Slow will both reach the end
    """

    fast = slow = head

    while fast and fast.next:
        slow = slow.next # one hop
        fast = fast.next.next # two hops

        if slow == fast:
            return True

    return False



ans3 = TortoiseHare(cycle)
ans4 = TortoiseHare(straight)

print(ans3)
print(ans4)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        p1 = A
        p2 = A
        set1 = set()
        while (p2!=None):            
            p1 = p1.next
            p2 = p2.next
            if ( p2 == None):
                break
            p2 = p2.next

            if ( p1 == p2 ):
                p = A
                if ( p1 == p):
                    return p1

                set1.add(p1)

                while (p != p1):
                    set1.add(p)
                    p = p.next          
                

                while (True):
                    p2 = p2.next
                    if (p2 in set1):
                        return p2
        
        return None
# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def isListPalindrome(l):
    if l == None or l.next == None:
        return True
    
    # advance until we had the node in the middle
    head = l
    slow = l
    fast = l
    
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        
    if fast != None:
        slow = slow.next
        
    # now we have the middle in slow, we need to reverse it and compare it to head
    slow = reverseList(slow)
    
    while slow != None:
        if slow.value != head.value:
            return False
        slow = slow.next
        head = head.next
        
    return True

def reverseList(l):
    current = l
    prev = None
    next = None
    while current != None:
        next = current.next
        current.next = prev        
        prev = current    
        current = next        
    return prev
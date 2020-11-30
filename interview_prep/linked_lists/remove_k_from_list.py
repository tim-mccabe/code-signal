#Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def removeKFromList(l, k):
    helper = ListNode(0)
    helper.next = l
    p = helper

    while p.next != None:
        if p.next.value == k:
            p.next = p.next.next
        else:
            p = p.next
    
    return helper.next
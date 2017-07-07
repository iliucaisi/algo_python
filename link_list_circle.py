class Node(object):
    def __init__(self, val, p=0):
        self.val = val
        self.next = p

def create_list():
    tail = Node(10, None)
    
    i = 9
    cur = tail
    while i > 0:
       node = Node(i, cur)
       cur = node
       if i == 3:
           tail.next = cur
       i -= 1
    return cur

def has_cycle(head):
    p1 = head
    p2 = head

    count = 0
    while p1 != None and p2 != None:
        if p1 == p2 and p1 != head:
            return count
        p1 = p1.next
        p2 = p2.next.next
        count = count + 1
    else:
        count = 0
    return count

def find_entry(head):
    count = has_cycle(head)
    print "DEBUG count=", count

    if count != 0:
        p1 = head
        p2 = head
        while count > 0:
            p2 = p2.next
            count -= 1
        print "DEBUG p2.val=", p2.val
        while p1 != None and p2 != None:
            if p1 == p2:
                break
            p1 = p1.next
            p2 = p2.next
    print "Entry is: ", p1.val 

##################################################
#					main						 #
##################################################

find_entry(create_list())


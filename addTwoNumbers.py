class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

def add(self,x):
    node=ListNode(x)
    self.next=node
    self=self.next
    return self

def Out(node):
    while node:
        print(node.val)
        node=node.next

def addTwoNumbers(l1,l2):
    sum=l1.val+l2.val
    r=ListNode(sum%10)
    t=r
    carry=int(sum/10)
    #print(sum, " ", carry)
    l1=l1.next
    l2=l2.next
    while l1!=None or l2!=None or carry >0:
        if l1!=None and l2!=None:
            sum=l1.val+l2.val+carry
        elif l1==None and l2==None:
            sum =carry
        elif l2==None:
            sum = l1.val + carry
        else:
            sum =l2.val+carry
        carry = int(sum / 10)
        #print(sum," ",carry)
        node=ListNode(sum%10)
        r.next=node
        r=r.next
        try:
            l1 = l1.next
        except:
            l1=None
        try:
            l2 = l2.next
        except:
            l2=None
    return t

l1=ListNode(2)
t1=l1
l1=add(l1,4)
l1=add(l1,3)
Out(t1)
print("------")
l2=ListNode(5)
t2=l2
l2=add(l2,6)
l2=add(l2,4)
Out(t2)
print("------")
t=addTwoNumbers(t1,t2)
Out(t)

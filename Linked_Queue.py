class Node:
    def __init__(self, item, n=None):
        self.item = item
        self.next = n

def enQueue(item):
    global front, rear
    newNode = Node(item)
    if front == None:
        front = newNode
    else:
        rear.next = newNode
    rear = newNode

def isEmpty():
    return front == None

def deQueue():
    global front, rear
    if isEmpty():
        print("Queue_Empty")
        return Node

    item = front.item
    front = front.next
    if front == None:
        rear = None
    return item

def Qpeek():
    return front.item

def printQ():
    f = front
    s = ""
    while f:
        s +=  f.item + " "
        f = f.next
    print(s)

front = None
rear = None

enQueue('A')
enQueue('B')
enQueue('C')
printQ()
print(deQueue())
print(deQueue())
print(deQueue())

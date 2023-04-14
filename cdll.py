class node:
    def __init__(self, key=None):
        self.key = key
        self.next = self
        self.prev = self

    def __str__(self):
        return str(self.key)


class doublyLinkedList:
    def __init__(self):
        self.head = node()
        self.size = 0

    def splice(self, nodeA, nodeB, nodeT):
        temp = nodeA
        boolHead = False
        boolTarget = False
        while (temp != nodeB):
            temp = temp.next
            if (temp.key == None):
                print("There is a head between nodeA and nodeB!")
                boolHead = True
                return None
            elif (temp.key == nodeT):
                print("There is a target between nodeA and nodeB!")
                boolHead = True
                return None
            else:
                continue
        if (boolHead == False and boolTarget == False):
            prevA = nodeA.prev
            nextB = nodeB.next
            nextT = nodeT.next

            prevA.next = nextB
            nextB.prev = prevA

            nodeT.next = nodeA
            nodeA.prev = nodeT

            nodeB.next = nextT
            nextT.prev = nodeB

    def moveAfter(self, nodeA, nodeT):
        self.splice(nodeA, nodeA, nodeT)

    def moveBefore(self, nodeA, nodeT):
        self.splice(nodeA, nodeA, nodeT.prev)

    def insertAfter(self, nodeT, key):
        nodeN = node(key)
        self.moveAfter(nodeN, nodeT)
        self.size += 1

    def insertBefore(self, nodeT, key):
        nodeN = node(key)
        self.moveBefore(nodeN, nodeT)
        self.size += 1

    def pushFront(self, key):
        self.insertAfter(self.head, key)

    def pushBack(self, key):
        self.insertBefore(self.head, key)

    def search(self, key):
        temp = self.head
        while (temp.next != self.head):
            if (temp.key == key):
                return temp
            else:
                temp = temp.next
            if (temp.next == self.head):
                if (temp.key == key):
                    return temp
                else:
                    continue
        return None

    def remove(self, nodeT):
        if (nodeT == None or nodeT == self.head):
            print("There is no target node!")
            return None
        nodeT.prev.next = nodeT.next
        nodeT.next.prev = nodeT.prev
        del nodeT
        self.size -= 1

    def popFront(self):
        if (self.size == 0):
            print("There is no target node!")
        else:
            self.remove(self.head.next)

    def popBack(self):
        if (self.size == 0):
            print("There is no target node!")
        else:
            self.remove(self.head.prev)

    def __len__(self):
        return int(self.size)

    def printList(self):
        temp = self.head
        while (temp.next != self.head):
            print(temp)
            temp = temp.next
            if (temp.next == self.head):
                print(temp)
            else:
                continue
        return None


L = doublyLinkedList()
L.pushFront(50)
L.pushFront(40)
L.pushFront(30)
L.pushFront(20)
L.pushFront(10)
L.pushBack(100)
L.remove(L.search(30))
L.printList()
print(len(L))
L.splice(L.search(10), L.search(40), L.search(100))
L.printList()
L.remove(L.search(40))
L.printList()

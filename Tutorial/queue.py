class Queue:
    def __init__(self):
        self.items = []
        self.front_index = 0

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if self.front_index == len(self.items):
            print("Queue is empty!")
        else:
            temp = self.items[self.front_index]
            self.front_index += 1


def josephus(n, k):
    Q = Queue()
    for i in range(1, n+1):
        Q.enqueue(i)
    while (Q.front_index != len(Q.items)):
        if ((Q.front_index + 1) % k != 0):
            Q.enqueue(Q.items[Q.front_index])
            Q.dequeue()
        else:
            Q.dequeue()
    return Q.items[Q.front_index - 1]


print(josephus(50, 22))

class Node:
    
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.runningSum = 0
        self.spaceUsed = 0
        self.head = None
        self.tail = self.head

    def next(self, val: int) -> float:
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        if self.spaceUsed < self.size:
            self.spaceUsed += 1
        elif self.spaceUsed == self.size:
            self.runningSum -= self.head.val
            self.head = self.head.next
        self.runningSum += val
        return self.runningSum / self.spaceUsed
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

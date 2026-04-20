class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.queue = [None] * k
        self.head = 0 
        self.tail = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.queue[self.tail] = value
            self.size += 1
            self.tail = (self.tail+1) % self.capacity
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.queue[self.head] = None
            self.head = (self.head+1) % self.capacity
            self.size -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.head]
        else:
            return -1

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.tail-1]

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.size == self.capacity:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
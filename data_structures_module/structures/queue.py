from linked_list import LinkedList


class Queue(LinkedList):
    def __init__(self):
        super().__init__()

    def enqueue(self, element):
        self.add_last(element)

    def dequeue(self):
        if self.head is None:
            raise Exception("Queue is empty")
        else:
            element = None
            if self.head == self.tail:
                element = self.head.element
                self.head = None
                self.tail = None
            else:
                element = self.head.element
                self.head = self.head.next
            return element

    def peek(self):
        """
        Return last element without deleting
        """
        return self.tail.element

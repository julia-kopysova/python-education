from data_structures_module.structures.linked_list import LinkedList


class Stack(LinkedList):
    def __init__(self):
        super().__init__()

    def push(self, element):
        self.add_first(element)

    def pop(self):
        if self.head is None:
            raise Exception("Stack is empty")
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
        return self.head.element


if __name__ == "__main__":
    stack_1 = Stack()
    stack_1.push("1")
    stack_1.push("2")
    stack_1.display_list()
    print("Pop: ", stack_1.pop())
    print("Peek: ", stack_1.peek())
    stack_1.display_list()

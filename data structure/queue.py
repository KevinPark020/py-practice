import node

class Queue:

    __slots__ = ["__tail", "__head", "__size"]

    def __init__(self):
        
        self.__tail = None
        self.__head = None
        self.__size = 0

    def enqueue(self, value):

        new_node = node.Node(value)

        if self.__size == 0:

            self.__tail = new_node
            self.__head = new_node
        
        else:
            
            self.__head.set_next(new_node)
            self.__head = new_node

        self.__size += 1

    def dequeue(self):

        if self.__size == 0:

            return None
        
        else:

            first = self.__tail
            self.__tail = self.__tail.get_next()
            self.__size -= 1
            return first
    
    def peek(self):

        if self.__size == 0:
        
            return None
        
        else:

            return self.__tail.get_value()
        
    def is_empty(self):

        if self.__size == 0:

            return True
        
        else:

            return False
        
    def size(self):

        return self.__size
    
    def contains(self, value):

        copy = self.__tail

        for i in range(self.__size):

            if value == copy.get_value():

                return i
            
            else:

                copy = copy.get_next()

        return None


    def __str__(self):
        s = "["
        copy_tail = self.__tail
        for i in range(0, self.__size):
            s += str(copy_tail.get_value())
            if i != self.__size - 1:
                s += ", "
            copy_tail = copy_tail.get_next()

        s += "]"

        return s


def main():

    q = Queue()

    # Test is_empty on new queue
    print("Empty?", q.is_empty())          # True
    print("Size:", q.size())               # 0

    # Test enqueue
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("After enqueuing 1, 2, 3:", q)   # [1, 2, 3]
    print("Size:", q.size())               # 3

    # Test peek (should be front = 1)
    print("Peek:", q.peek())               # 1

    # Test dequeue (FIFO - should get 1 first)
    print("Dequeue:", q.dequeue())         # node with value 1
    print("Dequeue:", q.dequeue())         # node with value 2
    print("After 2 dequeues:", q)          # [3]
    print("Size:", q.size())              # 1

    # Test contains
    q.enqueue(4)
    q.enqueue(5)
    print("Queue:", q)                     # [3, 4, 5]
    print("Contains 4:", q.contains(4))   # 1
    print("Contains 9:", q.contains(9))   # None

    # Test is_empty after dequeues
    print("Empty?", q.is_empty())         # False

    # Dequeue everything
    q.dequeue()
    q.dequeue()
    q.dequeue()
    print("Empty?", q.is_empty())         # True
    print("Size:", q.size())              # 0

    # Test dequeue on empty
    print("Dequeue empty:", q.dequeue())  # None




if __name__ == "__main__":
    main()
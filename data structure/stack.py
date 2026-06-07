import node

class Stack:

    __slots__ = ["__size", "__tail", "__head"]

    def __init__(self):
        
        self.__tail = None
        self.__head = None
        self.__size = 0

    def push(self, value):

        new_node = node.Node(value)

        if self.__size <= 0:
            
            self.__tail = new_node
            self.__head = new_node
        
        else: 

            temp = self.__head
            self.__head = new_node
            temp.set_next(self.__head)

        self.__size += 1

    def pop(self):

        temp = self.__tail
        last = 0

        if self.is_empty():

            return None

        if self.__size == 1:

            self.__size = 0
            return self.__head.get_value()

        for _ in range(self.__size):
            
            if temp.get_next() is self.__head:

                last = self.__head.get_value()
                self.__head = temp
                self.__head.set_next(None)
                self.__size -= 1
                return last
            
            else:
                
                temp = temp.get_next()

    def peek(self):

        if self.is_empty():

            return None

        return self.__head.get_value()
    
    def is_empty(self):

        if self.__size == 0:

            return True
        
        else:

            return False

    def __len__(self):
        
        return self.__size

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

    s = Stack()

    # Test is_empty on new stack
    print("Empty?", s.is_empty())       # True
    print("Size:", len(s))              # 0

    # Test push
    s.push(1)
    s.push(2)
    s.push(3)
    print("After pushing 1, 2, 3:", s)  # [1, 2, 3]
    print("Size:", len(s))              # 3

    # Test peek
    print("Peek:", s.peek())            # 3

    # Test pop
    print("Pop:", s.pop())              # 3
    print("Pop:", s.pop())              # 2
    print("After 2 pops:", s)          # [1]
    print("Size:", len(s))             # 1

    # Test is_empty after pops
    print("Empty?", s.is_empty())      # False

    # Pop last element
    print("Pop:", s.pop())             # 1
    print("Empty?", s.is_empty())      # True
    print("Size:", len(s))             # 0



if __name__ == "__main__":
    main()
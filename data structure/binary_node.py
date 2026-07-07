class BinaryNode:

    __slots__ = ["__value", "__left", "__right"]

    def __init__(self, value):
        
        self.__value = value
        self.__left = None
        self.__right = None

    def get_value(self):

        return self.__value
    
    def set_value(self, value):

        self.__value = value

    def get_left(self):

        return self.__left
    
    def set_left(self, left):

        self.__left = left

    def get_right(self): 

        return self.__right
    
    def set_right(self, right):

        self.__right = right

    def __str__(self):
        if self.__left != None:
            left = self.__left.get_value() 
        if self.__right != None:
            right = self.__right.get_value() 

        return f"BinaryNode(value={self.__value}, left={left}, right={right})"
    
    def infix_traversal(self):

        if self.__left != None:
            
    

def main():

    node1 = BinaryNode(5)
    node2 = BinaryNode(3)
    node3 = BinaryNode(7)

    node1.set_left(node2)
    node1.set_right(node3)
    print(node1)


if __name__ == "__main__":
    main()
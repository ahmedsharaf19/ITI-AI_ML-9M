from student import Student

class Node:
    def __init__(self, data: Student):
        self.data = data
        self.prev = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, item: Student) -> None:
        """
        push function to add a student to the top of the stack

        Args:
            item (Student): The student to be added
        """
        nd = Node(item)
        if self.top is not None:
            nd.prev = self.top    
        self.top = nd
    
    def pop(self) -> Student | None:
        """
        pop function to remove a student from the top of the stack

        Returns:
            Student | None: The student removed from the top of the stack, or None if the stack is empty
        """
        if self.top is None:
            return None
        temp = self.top
        self.top = temp.prev
        temp.prev = None
        return temp.data
    
    def peek(self) -> Student | None:
        """
        peek function to get the student at the top of the stack without removing it

        Returns:
            Student | None: The student at the top of the stack, or None if the stack is empty
        """
        return self.top.data if self.top is not None else None

    def is_empty(self) -> bool:
        """
        is_empty function to check if the stack is empty

        Returns:
            bool: True if the stack is empty, False otherwise
        """
        return self.top is None
    
    def size(self) -> int:
        """
        size function to get the current size of the stack

        Returns:
            int: The number of students in the stack
        """
        count = 0
        temp = self.top
        while temp:
            count += 1
            temp = temp.prev
        return count


        




if __name__ == "__main__":        
    s = Stack()

    st1 = Student(1,"Ahmed",[90,80,70,85,95])
    st2 = Student(2,"Ali",[60,75,70,80,85])
    st3 = Student(3,"Sara",[88,92,90,85,91])

    print("Is empty:", s.is_empty())

    s.push(st1)
    s.push(st2)
    s.push(st3)

    print("Size:", s.size())

    print("Peek:", s.peek().get_name())

    print("Pop:", s.pop().get_name())
    print("Pop:", s.pop().get_name())

    print("Size after pops:", s.size())

    print("Is empty:", s.is_empty())

    print("Pop:", s.pop().get_name())
    print("Pop on empty:", s.pop())

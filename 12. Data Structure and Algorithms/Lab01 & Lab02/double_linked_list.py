from student import Student


class Node:
    def __init__(self, data: Student):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, student: Student) -> None:
        """
        append function to add a student at the end of the list
        
        Args:
            student (Student): The student to be added
        """
        nd = Node(student)
        if self.head is None:
            self.head = self.tail = nd
        else:
            self.tail.next = nd
            nd.prev = self.tail
            self.tail = nd
        
    def prepend(self, student: Student) -> None:
        """
        prepend function to add a student at the beginning of the list

        Args:
            student (Student): The student to be added
        """
        nd = Node(student)
        if self.head is None:
            self.head = self.tail = nd
        else:
            nd.next = self.head
            self.head.prev = nd
            self.head = nd
    
    def delete_by_id(self, student_id: int) -> bool:
        """
        delete_by_id function to delete a student by their ID

        Args:
            student_id (int): The ID of the student to be deleted
        Returns:
            bool: True if deletion was successful, False otherwise
        """
        temp = self.search_by_id(student_id)
        if not temp:
            return False
        
        if self.head == self.tail == temp:
            self.head = self.tail = None
        
        elif temp == self.head:
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        
        elif temp == self.tail:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            temp.prev = temp.next = None
        
        return True

    def search_by_name(self, name: str) -> list[Student]:
        """
        search_by_name function to find students by their name
        Args:
            name (str): The name of the student to search for
        Returns:
            list[Student]: A list of students with the given name
        """
        students = []
        temp = self.head
        while temp:
            if temp.data.get_name() == name:
                students.append(temp.data)
            temp = temp.next
        return students

    def search_by_id(self, id: int) -> Student | bool:
        """
        search_by_id function to find a student by their ID
        Args:
            id (int): The ID of the student to search for   
        Returns:
            Node | bool: The node containing the student if found, False otherwise
        """
        temp = self.head
        while temp:
            if temp.data.get_id() == id:
                return temp
            temp = temp.next
        return False

    def count_nodes(self) -> int:
        """
        count_nodes function to count the number of nodes in the list
        Returns:
            int: The number of nodes in the list
        """
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def display_forward(self) -> None:
        """
        display_forward function to print the list from head to tail
        """
        temp = self.head
        while temp:
            print(temp.data.get_id(), temp.data.get_name(), temp.data.get_average())
            temp = temp.next

    def display_backward(self) -> None:
        """
        display_backward function to print the list from tail to head
        """
        temp = self.tail
        while temp:
            print(temp.data.get_id(), temp.data.get_name(), temp.data.get_average())
            temp = temp.prev

if __name__ == "__main__":
    dll = DoublyLinkedList()

    print("=== Append Students ===")
    s1 = Student(1, "Ahmed", [90, 80, 70, 85, 95])
    s2 = Student(2, "Ali", [60, 75, 70, 80, 85])
    s3 = Student(3, "Sara", [88, 92, 90, 85, 91])

    dll.append(s1)
    dll.append(s2)

    dll.display_forward()

    print("\n=== Prepend Student ===")
    dll.prepend(s3)
    dll.display_forward()

    print("\n=== Display Backward ===")
    dll.display_backward()

    print("\n=== Count Nodes ===")
    print("Total students:", dll.count_nodes())

    print("\n=== Search By ID ===")
    node = dll.search_by_id(2)
    if node:
        print(node.data.get_name(), node.data.get_average())

    print("\n=== Search By Name ===")
    result = dll.search_by_name("Ahmed")
    for s in result:
        print(s.get_name(), s.get_average())

    print("\n=== Delete By ID ===")
    dll.delete_by_id(1)
    dll.display_forward()

    print("\n=== Delete Head ===")
    dll.delete_by_id(3)
    dll.display_forward()

    print("\n=== Delete Tail ===")
    dll.delete_by_id(2)
    dll.display_forward()

    print("\n=== Final Count ===")
    print(dll.count_nodes())

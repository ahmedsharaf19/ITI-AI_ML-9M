from student import Student

class Queue:
    def __init__(self, size = None):
        self.items = []
        self.max_size = size
    
    def enqueue(self, item: Student) -> bool:
        """
        enqueue function to add a student to the end of the queue

        Args:
            item (Student): The student to be added

        Returns:
            bool: True if the student was added, False if the queue is full
        """
        if self.max_size is not None and len(self.items) == self.max_size:
                return False        
        self.items.append(item)
        return True
    
    def dequeue(self) -> Student | None:
        """
        dequeue function to remove a student from the front of the queue

        Returns:
            Student | None: The student removed from the front of the queue, or None if the queue is empty
        """
        if not len(self.items):
            return None
        return self.items.pop(0)
    
    def front(self) -> Student | None:
        """
        front function to get the student at the front of the queue without removing it

        Returns:
            Student | None: The student at the front of the queue, or None if the queue is empty
        """
        if len(self.items) == 0:
            return None
        return self.items[0]

    def is_empty(self) -> bool:
        """
        is_empty function to check if the queue is empty

        Returns:
            bool: True if the queue is empty, False otherwise
        """
        return len(self.items) == 0
    
    def is_full(self) -> bool:
        """
        is_full function to check if the queue is full

        Returns:
            bool: True if the queue is full, False otherwise
        """
        if self.max_size is None:
            return False
        return self.max_size == len(self.items)
    
    def size(self) -> int:
        """
        size function to get the current size of the queue
        
        Returns:
            int: The number of students in the queue
        """
        return len(self.items)
        

if __name__ == "__main__":
    q = Queue(3)

    s1 = Student(1,"Ahmed",[90,80,70,85,95])
    s2 = Student(2,"Ali",[60,75,70,80,85])
    s3 = Student(3,"Sara",[88,92,90,85,91])
    s4 = Student(4,"Omar",[70,75,80,85,90])

    print("Enqueue Ahmed:", q.enqueue(s1))
    print("Enqueue Ali:", q.enqueue(s2))
    print("Enqueue Sara:", q.enqueue(s3))
    print("Enqueue Omar (full):", q.enqueue(s4))

    print("Size:", q.size())
    print("Front:", q.front().get_name())

    print("Dequeue:", q.dequeue().get_name())
    print("Dequeue:", q.dequeue().get_name())

    print("Size:", q.size())
    print("Is Empty:", q.is_empty())
    print("Is Full:", q.is_full())

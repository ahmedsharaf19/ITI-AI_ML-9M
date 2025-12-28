class Queue:
    def __init__(self):
        self.data = []

    def insert(self, value):
        """
            Inser Value at end of Queue
            parameters:
                value -> represent value need to add                
        """
        self.data.append(value)

    def pop(self):
        """
            remove the first element in qeueu
            return:
                value that removed
        """
        if self.is_empty():
            return None
        return self.data.pop(0)
        

    def is_empty(self):
        """
            Check if qeue is empty or not
            return :
                Bool True empty and false not empty
        """
        return len(self.data) == 0
        


if __name__ == "__main__":

    print("=== Test Cases for Queue ===\n")

    # Test Case 1 — Insert One Element
    print("TC1: Insert 10")
    q = Queue()
    q.insert(10)
    print("Expected: [10]")
    print("Actual:  ", q.data, "\n")

    # Test Case 2 — Insert Multiple Elements
    print("TC2: Insert 10, 20, 30")
    q = Queue()
    q.insert(10)
    q.insert(20)
    q.insert(30)
    print("Expected: [10, 20, 30]")
    print("Actual:  ", q.data, "\n")

    # Test Case 3 — Pop from non-empty queue
    print("TC3: Pop from [10, 20, 30]")
    q = Queue()
    q.insert(10)
    q.insert(20)
    q.insert(30)
    result = q.pop()
    print("Expected pop return: 10")
    print("Actual:             ", result)
    print("Expected queue: [20, 30]")
    print("Actual queue:  ", q.data, "\n")

    # Test Case 4 — Pop from empty queue
    print("TC4: Pop from empty queue")
    q = Queue()
    result = q.pop()
    print("Expected: None")
    print("Actual:  ", result, "\n")

    # Test Case 5 — is_empty on empty queue
    print("TC5: is_empty() on empty")
    q = Queue()
    print("Expected: True")
    print("Actual:  ", q.is_empty(), "\n")

    # Test Case 6 — is_empty on non-empty queue
    print("TC6: is_empty() on non-empty")
    q.insert(5)
    print("Expected: False")
    print("Actual:  ", q.is_empty(), "\n")

    # Test Case 7 — Mixed Operations
    print("TC7: Insert 1, 2, 3 → Pop → Insert 4 → Pop")
    q = Queue()
    q.insert(1)
    q.insert(2)
    q.insert(3)
    print("Pop returned:", q.pop())  # expect 1
    q.insert(4)
    print("Pop returned:", q.pop())  # expect 2
    print("Expected final queue: [3, 4]")
    print("Actual final queue:  ", q.data, "\n")
    
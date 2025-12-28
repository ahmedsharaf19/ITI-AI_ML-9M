from BoundedQueue import BoundedQueue
from exception import QueueOutOfRangeException

if __name__ == "__main__":

    print("\n=====  Test Cases =====\n")
    # Load Queue From File Not Exists
    flag = BoundedQueue.load('queues.json')
    if flag :
        print('Loadded Succifily')
    else :
        print('File Not Found')

    # Create Queue and Insert Values Normally
    print("Create queue 'Q1' size=3 and insert 10, 20")
    q1 = BoundedQueue("Q1", 3)
    q1.insert(10)
    q1.insert(20)
    print("Expected items: [10, 20]")
    print("Actual items:  ", q1.data, "\n")
        
    # Insert Until Full → Expect Exception
    print("Insert into FULL queue (expect QueueOutOfRangeException)")

    try:
        q1.insert(30)   # ok
        q1.insert(40)   # overflow
        print("Actual: No exception (WRONG)")
    except QueueOutOfRangeException:
        print("Expected: QueueOutOfRangeException")
        print("Actual:   QueueOutOfRangeException\n")

    # get_by_name (Success Case)
    print("get_by_name('Q1')")
    found = BoundedQueue.get_by_name("Q1")

    print("Expected: Queue object with name='Q1'")
    print("Actual:  ", found.name if found else None, "\n")

    # get_by_name (Not Found)
    print("get_by_name('Unknown')")
    found = BoundedQueue.get_by_name("Unknown")

    print("Expected: None")
    print("Actual:  ", found, "\n")

    # Save Queues to File
    print("Save queues to file 'queues.json'")
    saved = BoundedQueue.save("queues.json")

    print("Expected: True")
    print("Actual:  ", saved, "\n")

    # Load Queues from File
    print("Load queues from file 'queues.json'")
    loaded = BoundedQueue.load("queues.json")

    print("Expected: True")
    print("Actual:  ", loaded)

    print("Expected loaded Q1 items: [10, 20, 30] OR according to file")
    loaded_q1 = BoundedQueue.get_by_name("Q1")
    print("Actual loaded items:      ", loaded_q1.data if loaded_q1 else None, "\n")

    # Insert into loaded queue until full
    print("Insert into loaded queue and test size limit")

    try:
        loaded_q1.insert(999)
        print("Insert success (if still not full)")
    except QueueOutOfRangeException:
        print("Expected: QueueOutOfRangeException (queue is full)")
        print("Actual:   QueueOutOfRangeException\n")


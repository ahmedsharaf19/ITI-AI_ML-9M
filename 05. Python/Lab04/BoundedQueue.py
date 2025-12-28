from qeue_class import Queue
from typing import override
import json
from exception import QueueOutOfRangeException


class BoundedQueue(Queue):
    _instances = dict()
    def __init__(self, name, size):
        super().__init__()
        self.name = name
        self.size = size
        BoundedQueue._instances[self.name] = self

    @override 
    def insert(self, value):
        """
            Method to insert element if queue has enough size
            parameters :
                Value need to add
            return :
                raise error if size full
                true if success
        """
        if len(self.data) == self.size:
            raise QueueOutOfRangeException
        self.data.append(value)
        return True
    
    @classmethod
    def get_by_name(cls, name):
        """
            Method to get object queue by name
            return :
                return this queue instance
        """
        if name not in cls._instances.keys():
            return None
        return cls._instances[name]


    @classmethod
    def load(cls, filename):
        """
            Function to load Queues instance from DB
            returns :
                True -> if success
                False -> if Not Success
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for k, v in data.items():
                    current_q = BoundedQueue(k, v['size'])
                    cls._instances[k] = current_q
                    value = v['items']
                    for _ in value:
                        current_q.insert(_)
            return True
        except FileNotFoundError:
            return False
        
    @classmethod
    def save(cls, filename):
        """
            Method to save Queue object in DB
            parameters : 
                filename -> Path of file
            return :
                True -> if success
        """
        with open(filename, 'w') as f:
            info = dict()
            for name, q in cls._instances.items():        
                info[name]= {
                        'size': q.size,
                        'items': q.data
                    }
            json.dump(info, f, indent=4)
        return True
    
    
    

import json
from typing import List, Dict


def load_db(PATH: str) -> List:
    """
        Function To Get DB 
        parameters : 
            USER_ID : Path of DB
        returns :
            List of Recored
    """
    # open data base
    db = open(PATH, 'r+')
    return json.load(db) # return all data in json

def save_db(PATH: str, data: Dict) -> bool :
    """
        Function to Save DB
        parameters:
            PATH : Path of db
        return 
            Bool indicate success or faild
    """
    # first load db
    db = load_db(PATH)
    # append data to old data
    db.append(data)
    # open file to write
    file =  open(PATH, 'w')
    # write data in json format
    data = json.dump(db, file, indent=4)
    # close connection with file
    file.close()

    return True

def update_db(PATH: str, data: List) -> bool:
    """
        Function to update entire DB with new data
        parameters:
            PATH : Path of db
            data : List of all records
        return 
            Bool indicate success or faild
    """
    try:
        file = open(PATH, 'w')
        json.dump(data, file, indent=4)
        file.close()
        return True
    except Exception as e:
        print(f"Error updating database: {e}")
        return False
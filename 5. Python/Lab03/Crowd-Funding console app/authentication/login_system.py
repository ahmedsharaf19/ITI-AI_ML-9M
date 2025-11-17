import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_system.db_ops import load_db, save_db

USER_PATH = r'data\users.json'

def get_users():
    """
        function return data of all users
    """
    return load_db(USER_PATH)

def login(email: str, password: str) -> bool:
    """
        Function to authentication login
    """
    users = get_users()
    for user in users:
        if email == user['email'] and password == user['password']:
            return True, email
    else :
        return False, None
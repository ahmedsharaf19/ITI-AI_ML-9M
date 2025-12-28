import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from .login_system import get_users

PATH = r'data\users.json'

from db_system.db_ops import load_db, save_db


def register(first_name: str, last_name: str, email: str, password: str, phone: str) -> bool:
    """
        Function to recored new user in db
        parameters : 
            first_name, last_name, email, password, phone
        return:
            return true if success
    """
    new_user = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'phone': phone
    }
    save_db(PATH, new_user)
    return True






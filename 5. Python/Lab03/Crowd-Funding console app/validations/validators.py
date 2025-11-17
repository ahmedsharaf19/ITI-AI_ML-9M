import re
from .config import *


def email_validator(email: str) -> bool:
    """
        Function to check valid email
        Parameters:
            Take Email
        return:
            return true or false
    """
    if re.fullmatch(EMAIL_PATTERN, email):
        return True
    return False

def password_validator(password: str) -> bool:
    """
        Function to check valid password
        Parameters:
            Take password
        return:
            return true or false
    """
    if re.fullmatch(PASSWORD_PATTERN, password):
        return True
    return False


def phone_validator(phone: str) -> bool:
    """
        Function to check valid phone
        Parameters:
            Take phone
        return:
            return true or false
    """
    if re.fullmatch(PHONE_PATTERN, phone):
        return True
    return False


def name_validator(name: str) -> bool:
    """
        Function to valid name
        parameters:
            Take name
        returns:
            True or false
    """
    if len(name.strip()) < 2 or isinstance(name.strip()[0], int):
        return False
    return True


def date_validator(date_str: str) -> bool:
    """
        Validate date string in YYYY-MM-DD format and check it's a real date.
    """
    from datetime import datetime
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except Exception:
        return False
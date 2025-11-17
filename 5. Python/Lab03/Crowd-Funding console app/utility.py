from db_system import load_db

PATH = r'data\users.json'
def email_exist(email: str) -> bool:
    """
        Function to check if email exist
    """
    users = load_db(PATH)
    for user in users:
        if email == user['email']:
            return True
    return False
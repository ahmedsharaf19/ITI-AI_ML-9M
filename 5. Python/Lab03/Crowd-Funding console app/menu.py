from authentication import *
from db_system import *
from validations import *
import os, time
from getpass import getpass
from utility import *
from projects import *
from pyfiglet import figlet_format

CURR_EMAIL = ""

def main_menu():
    global CURR_EMAIL
    os.system('cls')
    text = "Crowd Funding"
    ascii_art = figlet_format(text, font="standard")
    print(ascii_art)
    print('\t\tBy: Sharaf')
    items = ['Login', 'Signup', 'Exit']
    for idx, item in enumerate(items):
        print(f'\t\t\t{idx+1}. {item}')
    choice = input('Enter Your Choice From (1 to 3) : ')
    if choice == '1':
        CURR_EMAIL = login_menu()
        project_menu()
    elif choice == '2':
        flag = registration_menu()
        if flag:
            print('Success...')
            time.sleep(1)
        else : 
            print('Falid...')
            time.sleep(1)
        main_menu()
    else:
        os.system('cls')
        print('Good Bye')
        time.sleep(1)
        exit(0)

def login_menu() -> str:
    """
        Function Login_menu 
        return email
    """
    while True:
        os.system('cls')
        print('\t\t ############### Login ###############')
        email = input('Enter Your Email: ')   
        password = getpass('Enter Your Password: ')
        if not login(email, password)[0]:
            print("Email Or Password Incorrect")
            time.sleep(1)
            continue
        print('Success Login')
        time.sleep(1)
        return email
    


def registration_menu():
    os.system('cls')
    print('\t\t ############### Sign Up ###############')
    first_name = input('Enter Your First Name : ')
    while not name_validator(first_name):
        first_name = input('Enter Valid First Name (#char > 2 and not start with number) : ')

    last_name = input('Enter Your Lasr Name : ')
    while not name_validator(last_name):
        last_name = input('Enter Valid Last Name (#char > 2 and not start with number) : ')
    

    email = input('Enter Your Email : ')
    while not email_validator(email) and email_exist(email):
        email = input('Enter Valid Email : ')
    
    password = getpass('Enter Your password : ')
    while not password_validator(password) :
        password = getpass('Enter Valid password : ')
    
    conf_password = getpass('conformed password : ')
    while conf_password != password :
        conf_password = getpass('Enter Matched Password: ')
    
    phone = input('Enter Your phone (eg: format 01x): ')
    while not phone_validator(phone) :
        phone = input('Enter Valid phone : ')

    return register(first_name, last_name, email, password, phone)
    


def project_menu():
    os.system('cls')
    print(f"\t\t\t############ Welcom ############")
    list = """
        			1. View All Project
        			2. Edit Project
        			3. Delete Project
        			4. Search Projects
        			5. Add Project
        			6. Exit
    """
    print(list)
    ch = input('Choise : ')
    if ch == '1':
        os.system('cls')
        view_project(CURR_EMAIL)        
        input('Press any Button To Retuen Menu...')
        project_menu()
    elif ch == '2':
        os.system('cls')
        edit_project_menu()
        input('Press any Button To Retuen Menu...')
        project_menu()
    elif ch == '3':
        os.system('cls')
        delete_project_menu()
        input('Press any Button To Retuen Menu...')
        project_menu()
    elif ch == '4':
        os.system('cls')
        search_project_menu()
        input('Press any Button To Retuen Menu...')
        project_menu()
    elif ch == '5':
        os.system('cls')
        add_menu()
        project_menu()
    elif ch == '6':
        os.system('cls')
        return
    else :
        print('invalid number')
    
def edit_project_menu():
    """
        Function to show projects and let user select one to edit
    """
    projects = get_projects(CURR_EMAIL)
    
    if not projects:
        print("No projects found!")
        return
    
    print('\t\t ############### Select Project to Edit ###############')
    for idx, proj in enumerate(projects):
        print(f"\t\t\t{idx+1}. {proj['title']}")
    
    choice = input('Select Project Number : ')
    try:
        project_idx = int(choice) - 1
        if 0 <= project_idx < len(projects):
            selected_project = projects[project_idx]
            edit_project_details(selected_project)
        else:
            print("Invalid selection!")
    except ValueError:
        print("Please enter a valid number!")


def edit_project_details(project: dict):
    """
        Function to take new values from user and edit the project
    """
    os.system('cls')
    print('\t\t ############### Edit Project ###############')
    print(f"Current Project: {project['title']}")
    
    # Get new values from user
    title = input(f"Enter new title (current: {project['title']}), press Enter to skip: ").strip()
    details = input(f"Enter new description (current: {project['details']}), press Enter to skip: ").strip()
    target = input(f"Enter new target (current: {project['target']}), press Enter to skip: ").strip()
    start_date = input(f"Enter new start date (current: {project['start_date']}), press Enter to skip: ").strip()
    end_date = input(f"Enter new end date (current: {project['end_date']}), press Enter to skip: ").strip()
    
    # Build kwargs with only non-empty values
    update_data = {}
    if title:
        update_data['title'] = title
    if details:
        update_data['details'] = details
    if target:
        try:
            update_data['target'] = float(target)
        except ValueError:
            print("Invalid target value!")
            return
    if start_date:
        if not date_validator(start_date):
            print("\n\tInvalid start date format. Use YYYY-MM-DD")
            return
        update_data['start_date'] = start_date
    if end_date:
        if not date_validator(end_date):
            print("\n\tInvalid end date format. Use YYYY-MM-DD")
            return
        update_data['end_date'] = end_date
    
    if update_data:
        if edit_project(CURR_EMAIL, project['title'], **update_data):
            print("Project updated successfully!")
            time.sleep(1)
        else:
            print("Failed to update project!")
            time.sleep(1)
    else:
        print("No changes made!")


def delete_project_menu():
    """
        Show user's projects and allow deleting one by selecting its number
    """
    projects = get_projects(CURR_EMAIL)
    if not projects:
        print("No projects to delete.")
        return

    print('\t\t ############### Select Project to Delete ###############')
    for idx, proj in enumerate(projects):
        print(f"\t\t\t{idx+1}. {proj.get('title')}")

    choice = input('Select Project Number to delete: ')
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(projects):
            proj = projects[idx]
            confirm = input(f"Are you sure you want to delete '{proj.get('title')}'? (y/N): ")
            if confirm.lower() == 'y':
                if delete_project(CURR_EMAIL, proj.get('title')):
                    print('Project deleted successfully.')
                else:
                    print('Failed to delete project.')
            else:
                print('Delete cancelled.')
        else:
            print('Invalid selection')
    except ValueError:
        print('Please enter a valid number')


def search_project_menu():
    """
        Ask user for search criteria and display matching projects
    """
    print('\t\t ############### Search Projects ###############')
    title = input('Search by title (partial match, press Enter to skip): ').strip()
    start_date = input('Search by start date (YYYY-MM-DD, press Enter to skip): ').strip()
    end_date = input('Search by end date (YYYY-MM-DD, press Enter to skip): ').strip()

    # validate dates if provided
    if start_date and not date_validator(start_date):
        print('Invalid start date format. Use YYYY-MM-DD')
        return
    if end_date and not date_validator(end_date):
        print('Invalid end date format. Use YYYY-MM-DD')
        return

    results = search_projects(CURR_EMAIL, title=title if title else None,
                              start_date=start_date if start_date else None,
                              end_date=end_date if end_date else None)

    if not results:
        print('No matching projects found.')
        return

    print('\nMatching projects:')
    for idx, proj in enumerate(results):
        print(f"\n{idx+1}. {proj.get('title')}")
        print(f"   Details: {proj.get('details')}")
        print(f"   Target: {proj.get('target')}")
        print(f"   Start: {proj.get('start_date')}, End: {proj.get('end_date')}")



def add_menu():
    print('\t\t ############### Add Project ###############')
    
    title = input('Title : ')
    details = input('Details : ')
    target = input('Target : ')
    while not target.isdigit():
        target = input('Enter Valid Traget : ')
    target = float(target)
    start_date = input('Start Date Use YYYY-MM-DD: ')
    while not date_validator(start_date):
        start_date = input("\nInvalid start date format. Use YYYY-MM-DD: ")
    end_date = input('End Date YYYY-MM-DD: ')
    while not date_validator(end_date):
        end_date = input('\nInvalid end date format. use YYYY-MM-DD: ')

    if add_project(CURR_EMAIL, title, details, target, start_date, end_date):
        print("Project Added Successfly")
    else :
        print("Project Can't Add")
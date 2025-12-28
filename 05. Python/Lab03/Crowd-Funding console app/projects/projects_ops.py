import sys
import os
from tabulate import tabulate
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db_system.db_ops import load_db, save_db, update_db
from datetime import date

PATH = r'data\projects.json'



def get_projects(email: str) -> bool:
    """
        Function to get projects
    """
    projects = load_db(PATH)
    user_project = []
    for proj in projects:
        if proj['email'] == email:
            user_project.append(proj.copy())
    return user_project
    
def view_project(email: str):
    """
        Function to view all project
    """
    projects = get_projects(email)
    if not projects:
        print('No projects found!')
        return

    display_projects = []
    for proj in projects:
        display_projects.append({
            'Title': proj.get('title', ''),
            'Details': proj.get('details', ''),
            'Target': proj.get('target', ''),
            'Start': proj.get('start_date', ''),
            'End': proj.get('end_date', ''),
        })

    print(tabulate(display_projects, headers='keys', tablefmt='fancy_grid'))


def edit_project(email: str, curr_title: str, **kwargs) -> bool:
    all_projects = load_db(PATH)
    for proj in all_projects:
        if proj['email'] == email and proj['title'] == curr_title:
            for key, val in kwargs.items():
                if val:
                    proj[key] = val
            update_db(PATH, all_projects)
            return True
    return False


def delete_project(email: str, title: str) -> bool:
    """
        Delete a specific project matching owner email and title.
        Returns True if deleted, False if not found or on error.
    """
    all_projects = load_db(PATH)
    new_projects = []
    deleted = False
    for proj in all_projects:
        # keep projects that don't match the target
        if not (proj.get('email') == email and proj.get('title') == title):
            new_projects.append(proj)
        else:
            deleted = True

    if deleted:
        # write updated list back to file
        return update_db(PATH, new_projects)
    return False


def search_projects(email: str, title: str = None, start_date: str = None, end_date: str = None):
    """
        Search user's projects by title, start_date or end_date.
        Any non-None parameter is used as a filter (AND semantics).
        Returns list of matching project dictionaries (copies).
    """
    projects = get_projects(email)
    results = []
    for proj in projects:
        match = True
        if title:
            if title.lower() not in str(proj.get('title', '')).lower():
                match = False
        if start_date and match:
            if str(start_date) != str(proj.get('start_date')):
                match = False
        if end_date and match:
            if str(end_date) != str(proj.get('end_date')):
                match = False
        if match:
            results.append(proj.copy())
    return results


def add_project(email: str, title: str, details: str, target: str, start_date: str, end_date: str) -> bool:
    """
        Add new project in db
    """
    data = {
        'email': email,
        'title': title,
        'details': details,
        'target': target,
        'start_date': start_date,
        'end_date': end_date
    }
    save_db(PATH, data)
    return True
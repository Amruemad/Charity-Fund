import validate_inputs
import re
import validate_data
import validate_project
import tabulate


def validate_date(date):
    pattern = "^\\d{4}-\\d{2}-\\d{2}$"
    if re.fullmatch(pattern, date):
        return True
    else:
        return False


def get_date():
    while True:
        date = validate_inputs.ask_for_string('enter date format YYYY-MM-DD')
        if validate_date(date):
            return date
        else:
            print('invalid date enter it again ')


def create_project():
    email = validate_inputs.ask_for_string('enter your email again please')
    password = validate_inputs.ask_for_string('enter your password again please')
    if validate_data.check_login_port(email, password):
        title = validate_inputs.ask_for_string('enter project title')
        details = validate_inputs.ask_for_string('enter project details')
        total_target = validate_inputs.askforInt('enter total target')
        project_date = get_date()
        project_id = validate_data.get_login_id(email)
        project_info = {
        'ID': f'{project_id}',
        'title': f'{title}',
        'details': f'{details}',
        'total_target': f'{total_target}',
        'project_date': f'{project_date}'}
        save = validate_project.store_project(project_info)
        if save:
            print(f'Congratulations you project created successfully\n'
              f'your project title: {title}\n'
              f'your project description: {details}\n'
              f'your project total target: {total_target}\n'
              f'your project date: {project_date}\n'
              f'your project id: {project_id}\n')
    else:
        print('invalid')


def view_projects():
    books = validate_project.read_project()
    headers = {"ID": "ID",
               "title": "Title",
               "details": "Details",
               "total_target": "Total Target",
               "project_date": "Project Date"}
    print(tabulate.tabulate(books, headers, tablefmt="rounded_grid"))
    # for book in books:
    #     print(book)    '''if tabulate not working use this one '''


def delete_projects(project):
    all_projects = validate_project.read_project()
    print(all_projects)
    if all_projects:
        all_projects.remove(project)
        print(all_projects)
        deleted = validate_project.write_project(all_projects)
        return deleted
        # here we printed projects before deletion and after deletion while deleting project if exists


def delete_project():

    iddd = validate_inputs.ask_for_string("please enter the id of the project you want to delete: ")
    # search using this id if project exists  -->
    found = search_project_by_id_title(iddd)
    if found:
        print(found)
        delete_projects(found)
        print('deleted successfully!')
    else:
        print("--- project not found --- or its not yours.")


def search_project_by_id_title(project_id_title):
    all_projects = validate_project.read_project()
    email = validate_inputs.ask_for_string('enter your email again please')
    password = validate_inputs.ask_for_string('enter your password again please')
    for project in all_projects:
        if project['ID'] == project_id_title:
            needed = validate_data.get_login_id_toedit(email, password)
            '''id of who logged in '''
            if validate_project.get_user_project(needed):
                return project
        else:
            return False


def edit_project(project_id, updated_data):
    all_projects = validate_project.read_project()
    email = validate_inputs.ask_for_string('enter your email again please')
    password = validate_inputs.ask_for_string('enter your password again please')
    userid = validate_data.get_login_id_toedit(email, password)
    if userid == project_id:
        for project in all_projects:
            if project['ID'] == project_id:
                project.update(updated_data)
                saved = validate_project.write_project(all_projects)
                if saved:
                    print("Project edited successfully.")
                else:
                    print("Error editing project. Please try again.")
                    return False
    else:
        print("--- project not found --- or its not yours.")


def search_project(date):
    all_projects = validate_project.read_project()
    for project in all_projects:
        if project['project_date'] == date:
            print(project)
            break
    else:
        print('--- project not found ---')
        return False

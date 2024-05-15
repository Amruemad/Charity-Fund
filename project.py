import project_func


def projectmenu():
    while True:
        print('\n\n')
        print('--------------------------------\n')
        print("Welcome to Crowd-Funding console app")
        print('------------------------------------')
        choice = input("please enter your choice:\n"
                        "c to create project\n"
                       "v to view all projects\n"
                       "e to edit project\n"
                       "d to delete project\n"
                       "s to search projects using date BONUS\n"
                       "q to quit\n").lower()
        #to lower case the character.....

        if choice == "c":
            project_func.create_project()
        elif choice == 'v':
            project_func.view_projects()
        elif choice == 'e':
            id = input("please enter project id you want to edit")
            project_info = {
                'ID': f'{id}',
                'title': f'{input('please enter new title')}',
                'details': f'{input('enter new details')}',
                'total_target': f'{input('please enter total target')}',
                'project_date': f'{input('enter new project date')}'}
            project_func.edit_project(id, project_info)
        elif choice == 'd':
            project_func.delete_project()
        elif choice == 's':
            date = project_func.get_date()
            project_func.search_project(date)
        elif choice == 'q':
            exit()
        else:
            print("-------------- please enter valid choice------------------")
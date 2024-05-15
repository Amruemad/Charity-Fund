import json
def read_project():
    try:
        fileobject = open("projects.json", 'r')
    except Exception as ex:
        print(f"Error{ex} while registration --> try again ")
        return False
    else:
        try:
            data = json.load(fileobject)
        except Exception as ex:
            return []
        else:
            return data


def write_project(listt: list):
    try:
        fileobject = open("projects.json", 'w')
    except Exception as ex:
        print(f"Error {ex} while creation --> try again ")
        return False
    else:
        json.dump(listt, fileobject, indent=2)
        return True


def store_project(dataa):
    old_data = read_project()
    old_data.append(dataa)
    saved = write_project(old_data)
    return saved


def get_user_project(id):
    all_projects = read_project()
    for project in all_projects:
        if project['ID'] == id:
            return True
    else:
        return False
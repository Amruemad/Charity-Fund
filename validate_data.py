import json,project


def read_data():
    try:
        fileobject = open("users.json", 'r')
    except Exception as ex:
        print(f"Error{ex} while registration --> try again ")
        return False
    else:
        try:
            data = json.load(fileobject)
        except Exception:
            return []
        else:
            return data


def write_data(listt: list):
    try:
        fileobject = open("users.json", 'w')
    except Exception as ex:
        print(f"Error {ex} while registration --> try again ")
        return False
    else:
        json.dump(listt, fileobject, indent=2)
        return True


def store_data(dataa):
    old_data = read_data()
    old_data.append(dataa)
    saved = write_data(old_data)
    return saved


def check_for_login(emaill,passwordd):
    all_users = read_data()
    flag = False
    for user in all_users:
        if user['email'] == emaill and user['password'] == passwordd:
            print(f'Logged in successfully!, Welcome {user["firstname"]}.')
            flag = True
            if flag:
                project.projectmenu()
            break
    if not flag:
        print('Wrong email or password')

def check_login_port(emaill,passwordd):
    all_users = read_data()
    flag = False
    for user in all_users:
        if user['email'] == emaill and user['password'] == passwordd:
            flag = True
            return flag
    if not flag:
        print('Wrong email or password')
def get_login_id(emaill):
    all_users = read_data()
    for user in all_users:
        if user['email'] == emaill:
            return user['ID']

def get_login_id_toedit(emaill,password):
    all_users = read_data()
    for user in all_users:
        if user['email'] == emaill and user['password'] == password:
            return user['ID']


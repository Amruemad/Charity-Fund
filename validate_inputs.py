import random,validate_data
import re

def ask_for_string(message):
    while True:
        inputstring = input(message)
        if inputstring and not inputstring.isspace():
            inputstring=inputstring.strip()
            return inputstring
        else:
            print("--- please enter valid string ")


def askforInt(message):
    try:
        num = int(input(message))
    except Exception as ex:
        print(f" error{ex} --- please enter an integer")
        return askforInt(message)
    else:
        return num


def generateID():
    userid  = random.randint(1, 9999999)
    return userid


def f_name():
    fname = ask_for_string("Enter your first name: ")
    return fname


def l_name():
    lname = ask_for_string("Enter your last name: ")
    return lname


def y_email():
    email = ask_for_string("Enter your email address")
    return email


def password():
    while True:
        passwordd = input("Enter your password")
        confirm_password = input("Enter your confirmation password")
        if passwordd == confirm_password:
            return passwordd

        else:
            print('Wrong password re-enter your password')


def mob_no():
    while True:
        mob_noo = input("enter your phone number 11 digits only")
        if len(mob_noo) == 11:
            return mob_noo
        else:
            print('Wrong phone number re-enter your phone number again')




def register():
    fname = f_name()
    lname = l_name()
    yemail = y_email()
    passcode = password()
    mob_num = mob_no()
    userid = generateID()
    userinfo = {
                'ID': f'{userid}',
                'firstname': f'{fname}',
                'lastname': f'{lname}',
                'email': f'{yemail}',
                'password': f'{passcode}',
                'number': f'{mob_num}'}
    save = validate_data.store_data(userinfo)
    if save:
        print(f'Congratulations you registered successfully\n'
              f'your first name: {fname}\n'
              f'your last name: {lname}\n'
              f'your email: {yemail}\n'
              f'your phone: {mob_num}\n'
              f'your id number: {userid}\n')


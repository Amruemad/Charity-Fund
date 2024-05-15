import validate_inputs,validate_data,project


def mainmenu():
    while True:
        choice = input("please enter your choice: \n"
                       "r for register:\nl for login:\nq for quit: \n").lower()
        if choice == "r":
            validate_inputs.register()
        elif choice=='l':
            email_address = input('Enter your email address to login: ')
            password = input('Enter your password: ')
            validate_data.check_for_login(email_address, password)

        elif choice=='q':
            print('you have successfully logged out.')
            exit()
        else:
            print("-------------- please enter valid choice--------------")


if __name__ == "__main__":
    mainmenu()
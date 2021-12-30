from user_functions import *
import logging

logging.basicConfig(filename='user_app.log', level=logging.DEBUG)

while True:
    print("1. Add New User\n"
           + "2. Get All Users\n"
           + "3. Search\n"
           + "4. Update User By Id"
          )
    try:
        menu_flag = int(input("Type your choose: "))
    except ValueError:
        print("You can't type letters")
        logging.warning('somebody want to choose a letter!')
        continue
    if menu_flag == 1:
        logging.info("User Add")
        user_add()
    elif menu_flag == 2:
        logging.info("Get All!")
        try:
            get_all()
        except FileNotFoundError:
            logging.error('File Not Found!!!')
            create_file()
            get_all()
    elif menu_flag == 3:
        logging.info("Search")
        what_to_search = input('By Which Parametr you want to search: ')
        search_str = input('Search: ')
        try:
            search_by(search_str, what_to_search)
        except FileNotFoundError:
            logging.error('File Not Found!!!')
            create_file()
            search_by(search_str, what_to_search)

    elif menu_flag == 4:
        logging.info("Update!")
        try:
            update_user()
        except FileNotFoundError:
            logging.error('File Not Found!!!')
            create_file()
            update_user()



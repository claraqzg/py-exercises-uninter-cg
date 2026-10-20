def validate_choice(choice):
    '''
    Validates if the user's choice is valid.
    '''
    return choice == '1' or choice == '2' or choice == '3'


def file_exists(filename):
    '''
    Checks if a file exists.
    '''
    try:
        a = open(filename, 'rt')
        a.close()
        return True
    except FileNotFoundError:
        return False

def create_file(filename):
    '''
    Creates a new file.
    '''
    try:
        a = open(filename, 'wt+')
        a.close()
        print(f"File '{filename}' created successfully.")
    except:
        print(f"An error occurred while trying to create the file '{filename}'.")
        return False

def log_game(filename, game_name, console_name):
    '''
    Logs the game and console information to a file.
    '''
    try:
        a = open(filename, 'at')
    except:
        print(f"An error occurred while trying to open the file '{filename}'.")
    else:
        a.write(f"{game_name} - {console_name}\n")
    finally:
        a.close()

def list_files(filename):
    '''
    Lists the contents of a file.
    '''
    try:
        a = open(filename, 'rt')
    except:
        print(f"An error occurred while trying to open the file '{filename}'.")
    else:
        print(a.read())
    finally:
        a.close()

#####
newFile = "games.txt"
if file_exists(newFile):
    print(f"The file '{newFile}' exists.")
else:
    print(f"The file '{newFile}' does not exist.")
    create_file(newFile)

while True:
    print ("MENU")
    print ("1. Add Item")
    print ("2. List Itens")
    print ("3. Exit")

    choice = input("Choose an option: ")
    if validate_choice(choice):
        if choice == '1':
            print("You chose to add an item.")
            game_name = input("Enter the name of the game: ")
            console_name = input("Enter the console name: ")
            log_game(newFile, game_name, console_name)
        elif choice == '2':
            print("You chose to list items.")
            list_files(newFile)
        elif choice == '3':
            print("Exiting the program.")
            break
    else:
        print("Invalid choice. Please select a valid option.")



menu = {'AdminLogin': ['Create Account', 'Delete Account', 'Search Account',
                        'Edit Account', 'Show list of all accounts', 'To main menu'],
        'Searchby': ['Name', 'Address', 'Phone']
        }


def show_menu(menu_key):
    menu_items = menu[menu_key]
    while True:
        for index,item in enumerate(menu_items,1):
            print(f'{index}. {item}')
        choice = input('Enter your choice: ')
        if not choice.isnumeric() or int(choice) not in range(1,len(menu_items)+1):
            print(f'Invalid choice, try again')
            continue
        else:
            return choice
            

def get_phone():
    while True:
        phone = input('Phone NO(eg: 5022222222): ')
        if len(phone) != 10:
            print('Invalid phone number, try again')
        else:
            return phone


def get_gender():
    while True:
        gender = input('Gender(M or F): ')
        if gender not in('M','F','m','f'):
            print('Invalid input, try again')
        else:
            return gender.upper()


def get_acctype():
    while True:
        acc_type = input('Account Type:(s for saving or c for checking): ')
        if acc_type not in('s','c','S','C'):
            print('Invalid input, try again')
        else:
            return acc_type.upper()


def get_balance():
    while True:
        balance = input('Balance: ')
        if float(balance) <500:
            print('Minimum balance is 500, try again')
        else:
            return float(balance)

def get_customer():
    name = input('Name:')
    gender = get_gender()
    address = input('Address:')
    return name,gender,address


def get_info():
    customer = get_customer()
    acc_type = get_acctype()
    phone = get_phone()
    balance = get_balance()
    return customer[0],customer[1],customer[2],acc_type,phone,balance


def get_search():
    print('*************Search Account By:***************')
    choice = show_menu('Searchby')
    search_type = menu['Searchby'][int(choice)-1]
    search_words = input(f'Enter the information: ')
    return search_type,search_words
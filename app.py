from models import initialize,cur,Customer


menu = {'LoginPanel': ['Admin Login', 'Staff Login', 'Exit'],
        'AdminLogin': ['Create Account', 'Delete Account', 'Search Account',
                        'Edit Account', 'Show list of all accounts', 'To main menu'],
        'StaffLogin': ['Search Account', 'Deposit Cash', 'Withdraw Cash', 'To main menu'],
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


def get_name_address(title):
    while True:
        enter = input(f'{title}: ')
        if not enter:
            print(f"Please enter {title.lower()}, try again.")
            continue
        else:
            return enter


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
        try:
            float(balance)
        except ValueError:
            print ('You need to enter a number')
            continue
        if float(balance) <500:
            print('Minimum balance is 500, try again')
        else:
            return float(balance)


def get_info():
    name = get_name_address('Name')
    gender = get_gender()
    address = get_name_address('Address')
    acc_type = get_acctype()
    phone = get_phone()
    balance = get_balance()
    return name,gender,address,acc_type,phone,balance


def create_acc():
    new_info =get_info()
    Customer.add(new_info)


def search_acc():
    print('*************Search Account By:***************')
    choice = show_menu('Searchby')
    search_type = menu['Searchby'][int(choice)-1]
    search_words = input(f'Enter the information: ')
    search_info = (search_type.lower(),search_words)
    search_ids = Customer.search_customer(search_info)
    if not search_ids :
        print('The account is not exist!')
    else:
        for search_id in search_ids:
            print(Customer(search_id))
    return search_ids


def get_search_id():
    search_ids = search_acc()
    if search_ids != None:
        while True:
            id_choice = input(f'Enter the account ID:{search_ids}: ')
            if not id_choice.isnumeric() or int(id_choice) not in search_ids: 
                print('Choose an id in the list,try again')
                continue
            return int(id_choice)


def delete_acc():
    delete_id = get_search_id()
    Customer(delete_id).delete()


def edit_acc():    
    edit_id = get_search_id()
    edit_info = get_info()
    Customer(edit_id).update(edit_info)    


def all_acc():
    search_ids = Customer.search_customer(('name',''))
    print('*************ALL CUSTOMERS*************')
    for search_id in search_ids:
        print(Customer(search_id))


def admin():
    admin_running = True
    while admin_running:
        print('\n****************Admin PANEL****************\n')
        choice = show_menu('AdminLogin')
        if choice == '1':
            create_acc()
            print('Account created successfully!')
        elif choice == '2':
            print('***Search for the account you want to delete***')
            delete_acc()
            print('Account deleted successfully!')
        elif choice == '3':
            search_acc()
        elif choice == '4':
            print('***Search for the account you want to edit***')
            edit_acc()
            print('Account updated successfully!')
        elif choice == '5':
            all_acc()
        else:
            admin_running = False


def deposit_withdraw(d_or_w):
    acc_id = get_search_id()
    acc = Customer(acc_id)
    balance = float(acc.banlance)
    while True:
        amount = input(f'Enter the amount you want to {d_or_w}: ')
        try:
            float(amount)
        except ValueError:
            print ('You need to enter a number')
            continue
        if float(amount) <0:
            print('Deposit amount has to be greater than 0.')
            continue
        if d_or_w == 'withdraw':
            if float(amount)>balance:
                print(f'The account only has ${balance} left')
                continue
            else:
                amount = -float(amount)
                break
        else:
            amount = float(amount)
            break
    balance += amount
    print(balance)
    acc.update((acc.name,acc.gender,acc.address,acc.acc_type,acc.phone,balance))
    print(Customer(acc_id))


def staff():
    staff_running = True
    while staff_running:
        print('\n****************Staff PANEL****************\n')
        choice = show_menu('StaffLogin')
        if choice == '1':
            search_acc()
        elif choice == '2':
            print('***Search for the account you want to deposit***')
            deposit_withdraw('deposit')
            print('Account deposited successfully!')
        elif choice == '3':
            print('***Search for the account you want to withdraw***')
            deposit_withdraw('withdraw')
            print('Account withdrawed successfully!')
        else:
            staff_running = False
    

def app():
    app_running = True
    while app_running:
        print('\n****************LOGIN PANEL****************\n')
        choice = show_menu('LoginPanel')
        if choice == '1':
            admin()
        elif choice == '2':
            staff()
        else:
            app_running = False


if __name__ == "__main__":
    initialize()
    app()
    cur.close()
from unicodedata import decimal
from models import initialize,cur,Customer
from get_input import menu,show_menu,get_info,get_search


def create_acc():
    new_info = get_info()
    Customer.add(new_info)

def search_acc():
    search_info = get_search()
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
    
    
if __name__ == "__main__":
    initialize()
    admin()
    cur.close()
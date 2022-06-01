from models import initialize,cur,Customer
from get_input import menu,show_menu,get_info,get_customer,get_search


def create_acc():
    new_info = get_info()
    Customer.add(new_info)
    print('Account created successfully!')


def delete_acc():
    customer_info = get_customer()
    acc_ids = Customer.get_id(customer_info)
    if acc_ids == None:
        print('The account is not exist!')
    else:
        ids = []
        for acc_id in acc_ids:
            [print(Customer(id)) for id in acc_id]
            ids += list(acc_id)
        while True:
            id_choice = input(f'Enter the ID you want to delete{ids}: ')
            if int(id_choice) not in ids:
                print('Choose an id in the list,try again')
                continue
            Customer(int(id_choice)).delete()
            print('Account deleted successfully!')
            break


def search_acc():
    search_info = get_search()
    search_ids = Customer.search_customer(search_info)
    for search_id in search_ids:
        [print(Customer(id)) for id in search_id]
    

def admin():
    choice = show_menu('AdminLogin')
    if choice == '1':
        create_acc()
    elif choice == '2':
        delete_acc()
    elif choice == '3':
        search_acc()
    
if __name__ == "__main__":
    initialize()
    admin()
    cur.close()
import os
os.system('clear')


store_objects_dict = {}
store_names = ['fiesta', 'walmart', 'sams', 'cosco', 'randalls']
shopping_list =[]
user_dict = { 
    'Fiesta' : ['Milk', 'Soda', 'Fish'],
    'Walmart' : ['Paper', 'Napkins', 'Plate', 'Chips'],
    'Sams' : ['Chicken', 'Beef', 'Eggs', 'Sugar', 'Salt', 'Pepper', 'Honey'],
    'Costco' : ['tofu','pizza','grapes'],
    'Randalls' : ['string cheese','beer'] }


class Store:
    def __init__(self,store_name):
        self.store_name = store_name
        self.grocery_list =[]

    def __repr__(self):
        return (f" shopping list:  {self.grocery_list}\n")

def generate_list():
    for store in user_dict:        
        store_objects_dict[store] = Store(store)

def add_store():
    store_name = input("What store would you like to create a list for? ")
    store_objects_dict[store_name] = Store(store_name)
            
def import_list():
    for store_id in user_dict :
        items_array = user_dict[store_id]
        for item in items_array :
            store_objects_dict[store_id].grocery_list.append(item)

def add_item_to_list():
    os.system('clear')
    i = 0
    for store_id in store_objects_dict :
        print(f"{i}: {store_id}")
        i+=1
    update = input("Which list to you want to add to? : ")
    new_item = input("What do you want to add? ")
    store_objects_dict[update].grocery_list.append(new_item)
    print(input("Hit return to continue"))    

def print_shoppinglist():
    os.system('clear')
    for store_id in store_objects_dict :
        print(store_id)
        print("~" * 20)
        for item in store_objects_dict[store_id].grocery_list:
            print(f"     {item}")
        print(" \n ")
    input("Press Enter to continue")
    action_list()

def print_individual_shoppinglist():
    os.system('clear')
    i = 0
    for store_id in store_objects_dict :
        print(f"{i}: {store_id}")
        i+=1
    update = input("Which list to you want to add to? : ")
    os.system('clear')
    print(update)
    print("~" * 20)
    for item in store_objects_dict[update].grocery_list:
        print(f"     {item}")
    print(" \n ")
    input("Press Enter to continue")
    action_list()
    
def action_list():
    os.system('clear')
    print(" ")
    print("What action would you like to preform?")
    print(' 1) Create New Shopping list')
    print(' 2) Add Item to existing list')
    print(' 3) Print All lists')
    print(' 4) Print Individual list')
    print(' Q) EXIT')
    action = input()

      
    if action == '1':
        add_store()
        action_list()
    elif action == '2':
        add_item_to_list()
        action_list()
    elif action == '3':
        print_shoppinglist()
    elif action == '4':
        print_individual_shoppinglist()
    elif action.casefold() == 'q':
        exit
    else:
        action_list()
        

generate_list()
import_list()
action_list()
#generate_list()
#add_item_to_list()
#print_shoppinglist()
#print(store_objects_dict)
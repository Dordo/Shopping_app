# Greet user
print("Hello user")

# Empty list
shopping_list = []

# Ask the user to enter items into the shopping list
while True:
    message = input("""
Type add to enter items in the shopping list: \n
Type delete  to delete an item from the list: \n
Type quit to quit the program: \n
""")

    if message == 'add':
        add_meaasage = input("Type the item you want to be added to the list: \n")
        shopping_list.append(add_meaasage)
        print(shopping_list)

    elif message == 'delete':
        delete_message = input("What do you want to delete from the list: \n")
        shopping_list.remove(delete_message)
        print(shopping_list)

    elif message == 'quit':
        break


# Work on edge cases
    

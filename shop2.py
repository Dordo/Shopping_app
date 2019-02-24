# Greet User
character_name = "Jane"
print("Hello " + character_name + ", ")
# Ask user to enter items into shopping list
shopping_list = []

while True :
    # add new items
    new_item = input("Enter shopping list items: ")

# Add items to shopping list
shopping_list.append(new_item)
if new_item == 'Delete':
    # Remove item from shopping list
    shopping_list.remove(item)
    print(shopping_list)
elif new_item == 'quit':
    break
    


# Write your solution here!
from classes.DataManager import DataManager
#this app was very fun to make, it starts with uploading all customer and inventory data
#but can be modified if needed to upload multiple files or by a specific file name
user_input = ''
print('...starting application...')
dm = DataManager()
dm.upload_customers('customers.csv')
dm.upload_inventory('inventory.csv')
while user_input != '7':
    print("\n\n\n== Welcome to Code Platoon Video! ==")
    user_input = input("1. View store video inventory\n2. View store customers\n3. View customer rented videos\n4. Add new customer\n5. Rent video\n6. Return video\n7. Exit\n>> ")
    if user_input == '1':
        print("Here is the state of our inventory:")
        dm.show_inventory()
    elif user_input == '2':
        print('Here are our current customers')
        dm.show_customers()
    elif user_input == '3':
        dm.show_customer_videos()
    elif user_input == '4':
        dm.add_customer()
    elif user_input == '5':
        dm.rent_a_video()
    elif user_input == '6':
        dm.return_video()
    elif user_input == '7':
        print("Exiting application. Have a nice day!")

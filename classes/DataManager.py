#class for the Data Manager, it will track _customers and other items like videos
from .Customer import Customer
from .Inventory import Inventory
from csv import DictReader

#this data manager class is basically two lists of customer and inventory data
#with many methods to manipulate the data in both of those lists
class DataManager:
    def __init__(self):
        self._customers = []
        self._inventory = []

    #returns a customer object to access it's data or manipulate it in some way
    def get_customer(self, cust_id):
        for x in self._customers:
            if x.get_id == cust_id:
                return x
        return -1

    #uploads customer objects from the appropriately named csv file in to the customer list
    def upload_customers(self, customer_csv_file):
        print('...loading customers...')
        try:
            file_name = f'data/{customer_csv_file}'
            customer_data = open(file_name, 'r')
            
            with customer_data:
                dict_reader = DictReader(customer_data)
                list_dict_reader = list(dict_reader)
            
                for x in list_dict_reader:
                    self._customers.append(Customer(**x))

        except:
            print('File not found')

#uploads inventory objects from the appropriately named csv file in to the inventory list
    def upload_inventory(self, inventory_csv_file):
        file_name = f'data/{inventory_csv_file}'
        inventory_data = open(file_name, 'r')
        print('...loading inventory...')
        with inventory_data:
            dict_reader = DictReader(inventory_data)
            list_dict_reader = list(dict_reader)
            for x in list_dict_reader:
                self._inventory.append(Inventory(**x))
      
        print('...sorting inventory...')

        #this neat function sorts the inventory objects by title
        sorted_inventory = sorted(self._inventory, key=lambda d: d.get_title)
        self._inventory = sorted_inventory
       
    #builds a customer object with the necessary information in specifications
    def add_customer(self):
        id = ''
        account_type = ''
        first_name = ''
        last_name = ''
        user_input = input('Please enter your first name: \n>> ')
        first_name = user_input
        user_input = input('Please enter your last name: \n>> ')
        last_name = user_input
        valid = False
        while valid == False:
            print('Please select account type')
            print('1. Standard Account: max 1 rental out at a time')
            print('2. Premium Account: max 3 rentals out at a time')
            print("3. Standard Family Account: max 1 rental out at a time AND can not rent any 'R' rated movies")
            print("4. Premium Family Account: max 1 rental out at a time AND can not rent any 'R' rated movies")
            user_input = input('>> ')
            if user_input == '1':
                account_type = 'sx'
                valid = True
            elif user_input == '2':
                account_type = 'px'
                valid = True
            elif user_input == '3':
                account_type = 'sf'
                valid = True
            elif user_input == '4':
                account_type = 'pf'
                valid = True
            else:
                print("That's not an option, please try again")
        valid = True
        while valid == True:
            id = input("Please enter an ID number: \n>> ")
            valid = self.verify_customer_id(id)
            if valid == True:
                print('ID already taken, please select another')
        print('Thank you, creating account now...')

        self._customers.append(Customer(id, account_type, first_name, last_name))

    #prints the title and available copies of every inventory object in the inventory list
    def show_inventory(self):
        for x in self._inventory:
            print(f'Title: {x.get_title}\n\tAvailable Copies: {x.get_available_copies}\n')
    
    #prints the customer ID and First and Last name of every customer in the customer list
    def show_customers(self):
        for x in self._customers:
            print(f'Customer ID: {x.get_id}\n\tName: {x.get_first_name} {x.get_last_name}')
    
    #prints every video a customer has currently rented, or returns no rentals at this time 
    def show_customer_videos(self):
        user_input = input('Please enter the Customer ID you would like to view: \n>> ')
        while self.verify_customer_id(user_input) != True:
            user_input = input("Not a valid Customer ID, please try again or type exit to return to main menu: \n>> ")
        cust = self.get_customer(user_input)
        if cust.get_num_current_rentals() == 0:
            print("No Rentals At This Time")
        else:
            print("\nCurrently Rented Movies:")
            for x in cust.get_current_video_rentals:
                print(f'\t- {x}')

    #helper function, used in other functions to verify a user has entered a valid customer ID
    def verify_customer_id(self, id):
        for x in self._customers:
            if x.get_id == id:
                return True
        return False

    #helper function, used in other methods to see if an inventory object has more than 0 copies
    def check_stock(self, inventory_object):
        if int(inventory_object.get_available_copies) > 0:
            return True
        return False

    #helper function, determines if a video exists in our inventory within other methods    
    def find_video(self, inventory_title):
        lower_title = inventory_title.lower()
        found = False
        for x in self._inventory:
            lower_inventory = x.get_title.lower()
            if lower_title == lower_inventory:
                found = True
                in_stock = self.check_stock(x)
                if in_stock:
                    return True
                elif in_stock == False:
                    print("Currently out of stock")
                    return False
        if found == False:
            print('We do not carry this film')
            return False

    #returns an inventory object to either access its data or manipulate it in some way
    def get_video(self, title):
        for x in self._inventory:
            if x.get_title.lower() == title.lower():
                return x

    #facilitates the transaction of renting a video
    #verifies the customer can rent a movie based on the rules for their account type
    #updates both the customers current video list and the inventory list to reflect the rental occured
    def rent_a_video(self):
        valid = False
        while valid == False:
            user_input = input('Please enter customer ID: \n>> ')
            valid = self.verify_customer_id(user_input)
            if valid == False:
                print("Invalid Customer ID, please try again")
        customer = self.get_customer(user_input)
        max = customer.max_movies()
        num_rentals = customer.get_num_current_rentals()
        if num_rentals >= max:
            print(f'You already have reach the rental limit for your account, which is {customer.max_movies()}.')
        else:
            valid = False
            user_input = input('Please enter title of movie you would like to rent: \n>> ')
            while valid == False:
                valid = self.find_video(user_input)
                if valid == True:
                    film = self.get_video(user_input)                             
                    if film.get_rating == 'R':
                        if customer.r_movies() == False:
                            valid = False
                            user_input = input("This is a family account and cannot rent R rated movies, try another movie: \n>> ")
                        else:
                            customer.add_rental(film.get_title)
                            film.rented()
                            print("Movie succesfully rented. Enjoy!")
                    else:
                        print("Movie succesfully rented. Enjoy!")
                        customer.add_rental(film.get_title)
                        film.rented()

                elif valid == False:
                    user_input = input("Try entering a different movie title if you'd like or, type 'exit' to stop renting: \n>> ")
                    if user_input == 'exit':
                        valid = True
    #verfies both customer and movie are correct and then updates both the customer and inventory to reflect their return
    #kicks user back to main menu if they do not have anything rented out at this time
    def return_video(self):
        user_input = input('Enter Customer ID: \n>> ')
        while self.verify_customer_id(user_input) != True:
            user_input = ("Not a valid ID: Please try again.")
        cust = self.get_customer(user_input)
        if cust.get_num_current_rentals() == 0:
            print("You do not have any rentals checked out. Returning to main menu.")
        else:
            user_input = input('Please enter the movie title you would like to return: \n>> ')
            while self.find_video(user_input) != True:
                user_input = input('Please try another movie or type exit to quit: \n>> ')
                if user_input == 'exit':
                    return -1
            film = self.get_video(user_input)
            cust.returning(film.get_title)
            film.returned()

        



            








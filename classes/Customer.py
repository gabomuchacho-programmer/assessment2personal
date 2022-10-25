#Customer class keeps track of customer objects and their video renting capabilities/limitations based on account type

class Customer:

    def __init__(self, id, account_type, first_name, last_name, current_video_rentals = ''):
        self._id = id
        self._account_type = account_type
        self._first_name = first_name
        self._last_name = last_name

        #the current_video_rentals argument should be a list, if no current rentals it will be empty
        #during Customer object creation, it will append every movie title once it hits the delimiter '/'
        if current_video_rentals == '':
            self._current_video_rentals = []
        else:
            self._current_video_rentals = []    
            concat_movie = ''
            for x in current_video_rentals:
                if x != '/':
                    concat_movie += x
                else:
                    self._current_video_rentals.append(concat_movie)
                    concat_movie = ''
            self._current_video_rentals.append(concat_movie)



    #getters and setters
    @property
    def get_id(self):
        return self._id

    @property
    def set_id(self, new_id):
        self._id = new_id
        print("Name updated")

    @property
    def get_account_type(self):
        return self._account_type

    @property
    def set_account_type(self, new_account_type):
        self._account_type = new_account_type
        print('Account type updated')

    @property
    def get_first_name(self):
        return self._first_name

    @property
    def set_first_name(self, new_first_name):
        self._first_name = new_first_name
        print('First name updated')

    @property
    def get_last_name(self):
        return self._last_name

    @property
    def set_last_name(self, new_last_name):
        self._first_name = new_last_name
        print('Last name updated')

    @property
    def get_current_video_rentals(self):
        return self._current_video_rentals

    #adds a movie to a customers current movies list
    def add_rental(self, title):
        self._current_video_rentals.append(title)

    #removes a movie by title, from the customers current movies list
    def returning(self, title):
        self._current_video_rentals.remove(title)

    #returns the number of rentals a customer has
    def get_num_current_rentals(self):
        return len(self._current_video_rentals)

    #keep track of the maximum amount of movies an account can have depending on the account type
    def max_movies(self):
        if self._account_type == 'sx':
            return 1
        elif self._account_type == 'sf':
            return 1
        elif self._account_type == 'px':
            return 3
        elif self._account_type == 'pf':
            return 3

    #determines whether an account can rent 'R' rated movies or not based on account type
    def r_movies(self):
            if self._account_type == 'sx':
                return False
            elif self._account_type == 'sf':
                return False
            elif self._account_type == 'px':
                return True
            elif self._account_type == 'pf':
                return True
    
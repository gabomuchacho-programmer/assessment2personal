#Inventory class, for this assignment, will contain data on movies in a movie store, with the amount of available copies for rent

class Inventory:
    
    def __init__(self, id, title, rating, release_year, copies_available):
        self._id = id
        self._title = title
        self._rating = rating
        self._release_year = release_year
        self._copies_available = copies_available

    @property
    def get_video_id(self):
        return self._id
    @property
    def set_video_id(self, new_video_id):
        self._id = new_video_id
        print('Video ID updated')

    @property
    def get_title(self):
        return self._title

    @property
    def set_title(self, new_title):
        self._title = new_title
        print('Title updated')

    @property
    def get_rating(self):
        return self._rating

    @property
    def set_rating(self, new_rating):
        self._rating = new_rating
        print('Rating updated.')

    @property
    def get_release_year(self):
        return self._release_year

    @property
    def set_release_year(self, new_release_year):
        self._release_year = new_release_year
        print('Release year updated')

    @property
    def get_available_copies(self):
        return self._copies_available

    @property
    def set_available_copies(self, new_amount):
        self._copies_available = new_amount
        print('Available copies updated')

    #this method updates decrements the inventory of a film if it is in stock
    def rented(self):
        curr_copies = int(self._copies_available)
        curr_copies -= 1
        self._copies_available = str(curr_copies)
    #this method increments the amount of available copies of a film after being returned
    def returned(self):
        curr_copies = int(self._copies_available)
        curr_copies += 1
        self._copies_available = str(curr_copies)

          



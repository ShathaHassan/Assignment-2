from enum import Enum
from datetime import date

# Enum for ExhibitionType
class ExhibitionType(Enum):
    PERMANENT = "Permanent"
    TEMPORARY = "Temporary"

# The Exhibition class
class Exhibition:
    def __init__(self, name, start_date, end_date, location, exhibition_type):
        self.__name = name
        self.__start_date = start_date
        self.__end_date = end_date
        self.__location = location  #instance for location
        self.__exhibition_type = ExhibitionType(exhibition_type)


    # Methods to get and set name of the exhibition
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Methods to get and set start date of the exhibition
    def get_start_date(self):
        return self.__start_date

    def set_start_date(self, start_date):
        self.__start_date = start_date

    # Methods to get and set end date of the exhibition
    def get_end_date(self):
        return self.__end_date

    def set_end_date(self, end_date):
        self.__end_date = end_date

    # Methods to get and set location of the exhibition
    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    # Methods to get and set exhibition type of the exhibition
    def get_exhibition_type(self):
        return self.__exhibition_type

    def set_exhibition_type(self, exhibition_type):
        self.__exhibition_type = ExhibitionType(exhibition_type)

    # Method to add an artwork to the exhibition
    def add_artwork(self, artwork):
        if isinstance(artwork, Artwork):
            self.__artworks.append(artwork)
            return True
        return False

    # Method to remove an artwork from the exhibition
    def remove_artwork(self, artwork_id):
        for artwork in self.__artworks:
            if artwork.get_item_id() == artwork_id:
                self.__artworks.remove(artwork)
                return True
        return False

    # Method to get a list of all artworks in the exhibition
    def get_artworks(self):
        return self.__artworks

    # Method to check if the exhibition is current
    def is_exhibition_current(self):
        current_date = date.today()
        return self.__start_date <= current_date <= self.__end_date

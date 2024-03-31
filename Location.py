from enum import Enum

# Define the enum for LocationType
class LocationType(Enum):
    GALLERY = "Gallery"
    HALL = "Hall"
    OUTDOOR = "Outdoor"

# Define the Location class
class Location:
    def __init__(self, name, location_type, capacity):
        self.__name = name
        self.__location_type = LocationType[location_type.upper()]
        self.__capacity = capacity
        self.__is_available = True

    # Getter and setter for name
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    # Getter for location_type
    def get_location_type(self):
        return self.__location_type.value

    # Getter and setter for capacity
    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, new_capacity):
        self.__capacity = new_capacity

    # Getter and setter for is_available
    def is_available(self):
        return self.__is_available

    def set_available(self, availability):
        self.__is_available = availability


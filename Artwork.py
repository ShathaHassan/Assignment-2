class Artwork:
    def __init__(self, artist, style, item_id, title, date_of_creation, historical_significance, current_location):
        self.__artist = artist
        self.__style = style
        self.__item_id = item_id
        self.__title = title
        self.__date_of_creation = date_of_creation
        self.__historical_significance = historical_significance
        self.__current_location = current_location  # Assuming current_location is a Location object
        self.__exhibition_history = []  # This will be a list of Exhibition objects
# creating the getters and setters
    def get_artist(self):
        return self.__artist

    def set_artist(self, artist):
        self.__artist = artist

    def get_style(self):
        return self.__style

    def set_style(self, style):
        self.__style = style

    def get_item_id(self):
        return self.__item_id

    def set_item_id(self, item_id):
        self.__item_id = item_id

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_date_of_creation(self):
        return self.__date_of_creation

    def set_date_of_creation(self, date_of_creation):
        self.__date_of_creation = date_of_creation

    def get_historical_significance(self):
        return self.__historical_significance

    def set_historical_significance(self, historical_significance):
        self.__historical_significance = historical_significance

    def get_current_location(self):
        return self.__current_location

    def set_current_location(self, current_location):
        self.__current_location = current_location

    def get_exhibition_history(self):
        return self.__exhibition_history

    def add_to_exhibition_history(self, exhibition):
        self.__exhibition_history.append(exhibition)

    def move_to_location(self, new_location):
        self.__current_location = new_location

    def update_item_details(self, updated_details):
        for key, value in updated_details.items():
            if key == "artist":
                self.set_artist(value)
            elif key == "style":
                self.set_style(value)
            elif key == "item_id":
                self.set_item_id(value)
            elif key == "title":
                self.set_title(value)
            elif key == "date_of_creation":
                self.set_date_of_creation(value)
            elif key == "historical_significance":
                self.set_historical_significance(value)
            elif key == "current_location":
                self.set_current_location(value)


    def display_information(self):
        info = f"Artwork Title: {self.get_title()}, Artist: {self.get_artist()}, Style: {self.get_style()}"
        info += f", Created on: {self.get_date_of_creation()}, Significance: {self.get_historical_significance()}"
        return info

    def add_to_exhibition(self, exhibition):
        if exhibition not in self.__exhibition_history:
            self.__exhibition_history.append(exhibition)
            return True
        return False


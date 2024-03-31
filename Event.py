class Event:
    def __init__(self, event_id, name, start_date, end_date, location):
        self.__event_id = event_id
        self.__name = name
        self.__start_date = start_date
        self.__end_date = end_date
        self.__location = location  # is an instance of the Location class

    def get_event_id(self):
        return self.__event_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_start_date(self):
        return self.__start_date

    def set_start_date(self, start_date):
        self.__start_date = start_date

    def get_end_date(self):
        return self.__end_date

    def set_end_date(self, end_date):
        self.__end_date = end_date

    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    def get_details(self):
        details = f"Event ID: {self.__event_id}, Name: {self.__name}"
        details += f", Starts on: {self.__start_date}, Ends on: {self.__end_date}"
        details += f", Location: {self.__location.get_name()}"  # Assuming Location has a get_name() method
        return details

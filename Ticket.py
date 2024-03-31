from enum import Enum
from datetime import datetime

# Define the enum for TicketType
class TicketType(Enum):
    ADULT = "Adult"
    CHILD = "Child"
    STUDENT = "Student"
    SENIOR = "Senior"
    GROUP = "Group"

# Define the Ticket class
class Ticket:
    def __init__(self, ticket_id, visitor_id, ticket_price, date_of_issue, valid_date, exhibition_id, number_of_participants, ticket_type):
        self.__ticket_id = ticket_id
        self.__visitor_id = visitor_id
        self.__ticket_price = ticket_price
        self.__date_of_issue = datetime.strptime(date_of_issue, '%Y-%m-%d')
        self.__valid_date = datetime.strptime(valid_date, '%Y-%m-%d')
        self.__exhibition_id = exhibition_id
        self.__number_of_participants = number_of_participants
        self.__ticket_type = TicketType[ticket_type.upper()]

    def get_ticket_id(self):
        return self.__ticket_id

    def set_ticket_id(self, ticket_id):
        self.__ticket_id = ticket_id

    def get_visitor_id(self):
        return self.__visitor_id

    def set_visitor_id(self, visitor_id):
        self.__visitor_id = visitor_id

    def get_ticket_price(self):
        return self.__ticket_price

    def set_ticket_price(self, ticket_price):
        self.__ticket_price = ticket_price

    def get_date_of_issue(self):
        return self.__date_of_issue.strftime('%Y-%m-%d')

    def set_date_of_issue(self, date_of_issue):
        self.__date_of_issue = datetime.strptime(date_of_issue, '%Y-%m-%d')

    def get_valid_date(self):
        return self.__valid_date.strftime('%Y-%m-%d')

    def set_valid_date(self, valid_date):
        self.__valid_date = datetime.strptime(valid_date, '%Y-%m-%d')

    def get_exhibition_id(self):
        return self.__exhibition_id

    def set_exhibition_id(self, exhibition_id):
        self.__exhibition_id = exhibition_id

    def get_number_of_participants(self):
        return self.__number_of_participants

    def set_number_of_participants(self, number_of_participants):
        self.__number_of_participants = number_of_participants

    def get_ticket_type(self):
        return self.__ticket_type.value

    def set_ticket_type(self, ticket_type):
        self.__ticket_type = TicketType[ticket_type.upper()]

    def is_valid(self):
        return self.__valid_date >= datetime.now()

    def calculate_final_price(self):
        # assuming tax or service rate  is 10%
        tax_rate = 0.10
        return self.__ticket_price * (1 + tax_rate)

    def get_ticket_details(self):
        details = f"Ticket ID: {self.__ticket_id}, Visitor ID: {self.__visitor_id}, "
        details += f"Ticket Type: {self.get_ticket_type()}, Price: {self.__ticket_price}, "
        details += f"Valid Date: {self.get_valid_date()}, Exhibition ID: {self.__exhibition_id}"
        return details



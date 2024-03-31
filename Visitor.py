class Visitor:
    def __init__(self, visitor_id, name, demographic_details):
        self.__visitor_id = visitor_id
        self.__name = name
        self.__demographic_details = demographic_details
        self.__tickets = []

    def get_visitor_id(self):
        return self.__visitor_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_demographic_details(self):
        return self.__demographic_details

    def set_demographic_details(self, demographic_details):
        self.__demographic_details = demographic_details

    def purchase_ticket(self, event, ticket_type, ticket_price, date_of_issue, valid_date, exhibition_id, number_of_participants):

        new_ticket = Ticket(
            ticket_id=123,  # This should be generated uniquely
            visitor_id=self.__visitor_id,
            ticket_price=ticket_price,
            date_of_issue=date_of_issue,
            valid_date=valid_date,
            exhibition_id=exhibition_id,
            number_of_participants=number_of_participants,
            ticket_type=ticket_type
        )
        self.__tickets.append(new_ticket)
        return new_ticket

    def get_tickets(self):
        return self.__tickets

    def add_ticket(self, ticket):
        if ticket not in self.__tickets:
            self.__tickets.append(ticket)

from Artwork import Artwork
from Exhibition import Exhibition, ExhibitionType
from Location import Location, LocationType
from Ticket import Ticket, TicketType
from Visitor import Visitor
from Event import Event

def main():
    # Setting up a location for exhibitions
    main_gallery = Location("Main Gallery", LocationType.GALLERY.value, 250)

    # Test case for adding new artwork
    starry_night = Artwork("Vincent van Gogh", "Post-Impressionism", "001", "Starry Night", "1889",
                           "A masterpiece of post-impressionist art", main_gallery)
    print(f"New Artwork Added: {starry_night.display_information()}")

    # Test case for opening a new exhibition
    impressionist_exhibition = Exhibition("Impressionist Masterpieces", "2024-04-01", "2024-06-30", main_gallery,
                                          ExhibitionType.TEMPORARY.value)
    impressionist_exhibition.add_artwork(starry_night)
    print(f"Exhibition Opened: {impressionist_exhibition.get_name()}, featuring artworks like {starry_night.get_title()}")

    # Test case for purchasing tickets
    ticket1 = Ticket("T001", "V001", 20.0, "2024-03-01", "2024-04-15", "E001", 1,
                     TicketType.ADULT.value)
    visitor1 = Visitor("V001", "Shatha Hassan", {"age": 19, "gender": "female"})
    visitor1.add_ticket(ticket1)
    print(f"Ticket Purchased: {ticket1.get_ticket_details()} by {visitor1.get_name()}")

    # Displaying payment receipts (Assuming calculate_final_price includes taxes/fees)
    print(f"Payment Receipt: {ticket1.calculate_final_price()} for {visitor1.get_name()}")

    # Assuming an Event class for broader activities
    spring_art_fair = Event("E001", "Spring Art Fair", "2024-03-15", "2024-03-20", main_gallery)
    print(f"Event Planned: {spring_art_fair.get_details()}")

if __name__ == '__main__':
    main()

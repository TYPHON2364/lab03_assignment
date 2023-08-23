class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_flight_id(self, flight_id):
        for flight in self.flights:
            if flight.flight_id == flight_id:
                return flight
        return None

    def search_by_source(self, source):
        result = []
        for flight in self.flights:
            if flight.source == source:
                result.append(flight)
        return result

    def search_by_destination(self, destination):
        result = []
        for flight in self.flights:
            if flight.destination == destination:
                result.append(flight)
        return result

def main():
    flight_table = FlightTable()

    flight_table.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
    flight_table.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
    flight_table.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
    flight_table.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
    flight_table.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
    flight_table.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))

    user_input = input("Enter 1 to search by Flight ID, 2 to search by source city, 3 to search by destination city: ")

    if user_input == "1":
        flight_id = input("Enter Flight ID: ")
        result = flight_table.search_by_flight_id(flight_id)
        if result:
            print("Flight found:")
            print("Flight ID:", result.flight_id)
            print("From:", result.source)
            print("To:", result.destination)
            print("Price:", result.price)
        else:
            print("Flight not found.")

    elif user_input == "2":
        source = input("Enter source city: ")
        result = flight_table.search_by_source(source)
        if result:
            print("Flights found:")
            for flight in result:
                print("Flight ID:", flight.flight_id)
                print("From:", flight.source)
                print("To:", flight.destination)
                print("Price:", flight.price)
        else:
            print("No flights found.")

    elif user_input == "3":
        destination = input("Enter destination city: ")
        result = flight_table.search_by_destination(destination)
        if result:
            print("Flights found:")
            for flight in result:
                print("Flight ID:", flight.flight_id)
                print("From:", flight.source)
                print("To:", flight.destination)
                print("Price:", flight.price)
        else:
            print("No flights found.")

    else:
        print("Invalid input.")

if __name__ == "__main__":
    main()

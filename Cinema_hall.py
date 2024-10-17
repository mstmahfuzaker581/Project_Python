class Star_Cinema:
    hall_list = []
    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {} 
        self.__show_list = [] 
        self.__rows = rows  
        self.__cols = cols 
        self.__hall_no = hall_no  
        super().entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.__show_list.append(show_info)
        seats = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[show_id] = seats

    def book_seats(self, show_id, seat_list):
        if show_id not in self.__seats:
            print(f"Error: Show ID {show_id} does not exist.")
            return
        for seat in seat_list:
            row, col = seat
            if row >= self.__rows or col >= self.__cols:
                print(f"Error: Seat ({row}, {col}) is invalid.")
                continue
            if self.__seats[show_id][row][col] == 1:
                print(f"Error: Seat ({row}, {col}) is already booked.")
            else:
                self.__seats[show_id][row][col] = 1
                print(f"Seat ({row}, {col}) booked successfully.")

    def view_show_list(self):
        if not self.__show_list:
            print("No shows available.")
        else:
            print("Show List:")
            for show in self.__show_list:
                print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            print(f"Error: Show ID {show_id} does not exist.")
            return
        print(f"Available seats for Show ID {show_id}:")
        seats = self.__seats[show_id]
        for row in range(self.__rows):
            for col in range(self.__cols):
                if seats[row][col] == 0:
                    print(f"Seat ({row}, {col}) is available.")
                else:
                    print(f"Seat ({row}, {col}) is booked.")
def cinema_system():
    hall1 = Hall(5, 5, 1)
    hall1.entry_show(111, "Jawan Maji", "25/10/2023 11:00 AM")
    hall1.entry_show(333, "Sujon Maji", "25/10/2023 02:00 PM")

    while True:
        print("\n1. VIEW ALL SHOW TODAY")
        print("2. VIEW AVAILABLE SEATS")
        print("3. BOOK TICKET")
        print("4. Exit")
        option = int(input("ENTER OPTION: "))
        if option == 1:
            hall1.view_show_list()

        elif option == 2:
            show_id = int(input("ENTER SHOW ID: "))
            hall1.view_available_seats(show_id)

        elif option == 3:
            show_id = int(input("ENTER SHOW ID: "))
            num_seats = int(input("HOW MANY SEATS TO BOOK? "))

            seat_list = []
            for i in range(num_seats):
                row = int(input(f"Enter Row for seat {i+1}: "))
                col = int(input(f"Enter Column for seat {i+1}: "))
                seat_list.append((row, col))

            hall1.book_seats(show_id, seat_list)

        elif option == 4:
            print("Exiting system...")
            break

        else:
            print("Invalid option, please try again.")

cinema_system()                    

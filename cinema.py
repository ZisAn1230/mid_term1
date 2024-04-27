class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = [['free' for _ in range(cols)] for _ in range(rows)]
        self.show_list = []
        self.allocate_seats()

    def allocate_seats(self):
        for i in range(1, self.rows + 1):
            for j in range(1, self.cols + 1):
                self.seats[i-1][j-1] = 'free'

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)

    def book_seats(self, id, seat_list):
        show_movie = None
        for show in self.show_list:
            if show[0] == id:
                show_movie = show[1]
                break

        if show_movie is None:
            print("Invalid show ID.")
            return

        for seat in seat_list:
            if seat < 0 or seat >= self.rows * self.cols:
                print(f"Invalid seat number {seat}.")
                continue
            row = seat // self.cols
            col = seat % self.cols
            if self.seats[row][col] == 'booked':
                print(f"Seat {seat} is already booked.")
            else:
                self.seats[row][col] = 'booked'
                print(f"Seat {seat} booked successfully for {show_movie}!")

    def view_show_list(self):
        print("Shows running:")
        for show in self.show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, id):
        for show in self.show_list:
            if show[0] == id:
                print(f"Available seats for show {id}:")
                for i in range(self.rows):
                    for j in range(self.cols):
                        seat_num = i * self.cols + j
                        if self.seats[i][j] == 'free':
                            print(f"Seat {seat_num}")




star_cinema = Star_Cinema()

hall1 = Hall(rows=5, cols=10, hall_no=1)
hall2 = Hall(rows=6, cols=12, hall_no=2)

star_cinema.entry_hall(hall1)
star_cinema.entry_hall(hall2)

hall1.entry_show(id=112, movie_name="Spiderman", time="3:00 PM")
hall1.entry_show(id=223, movie_name="3 Idiots", time="6:00 PM")
hall1.entry_show(id=334, movie_name="Jawan", time="9:00 PM")

hall1.book_seats(id=1, seat_list=[1, 2, 3, 4])
hall1.view_available_seats(id=1)
hall1.view_show_list()


while True:
    print("\n1. View show list")
    print("2. View available seats for a show")
    print("3. Book seats")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        for hall in star_cinema.hall_list:
            hall.view_show_list()
    elif choice == "2":
        show_id = int(input("Enter the ID of the show: "))
        for hall in star_cinema.hall_list:
            hall.view_available_seats(show_id)
    elif choice == "3":
        show_id = int(input("Enter the ID of the show you want to book seats for: "))
        seats_input = input("Enter the seats you want to book: ")
        seat_list = [int(seat) for seat in seats_input.split()]
        for hall in star_cinema.hall_list:
            hall.book_seats(show_id, seat_list)
            break  
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

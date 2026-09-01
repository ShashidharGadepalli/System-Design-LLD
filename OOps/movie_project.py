class Movie:

    def __init__(self, movie_name:str, total_seats:int, ticket_price:int) -> None:

        self.movie_name = movie_name
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.booked_seats = 0

    def book_ticket(self, num_tickets:int) -> None:
            if self.booked_seats + num_tickets <= self.total_seats:
                self.booked_seats += num_tickets
                print(f"{num_tickets} tickets booked successfully for {self.movie_name}.")
                print(f"Total amount: ${num_tickets * self.ticket_price} ")
            else:
                 print("Sorry , not enough seats available.")

    def show_status(self) -> None:
        seats_available = self.total_seats - self.booked_seats
        print(f"Movie: {self.movie_name}")
        print(f"Seats Available: {seats_available}")
        print(f"Total Booked Seats: {self.booked_seats}")

m1 = Movie("Inception", 100, 500)
m1.show_status()
m1.book_ticket(70)
m1.show_status()
m1.book_ticket(40)
'''Write a Class ‘Trainʼ which has methods to book a ticket, get status (no of seats) and get
fare information of train running under Indian Railways'''
import random


class Train:
    def __init__(self, name, source, destination, seats, fare):
        self.train_no = random.randint(100000, 999999)   # random 6-digit number
        self.name = name
        self.source = source
        self.destination = destination
        self.seats = seats                                # available seats
        self.fare = fare                                  # fare per ticket (Rs)

    def book_ticket(self, passengers):
        if passengers > self.seats:
            print(f"Only {self.seats} seats available. Booking failed.")
            return False

        status = random.choice([True, False])             # random booking status

        if status:
            self.seats -= passengers
            print(f"Booking CONFIRMED: {status}")
            print(f"Train No: {self.train_no}, Tickets: {passengers}")
            print(f"Total fare: Rs {self.fare * passengers}")
        else:
            print(f"Booking FAILED: {status}")
        return status

    def get_status(self):
        print(f"Train No {self.train_no} has {self.seats} seats available.")

    def get_fare(self):
        print(f"Fare from {self.source} to {self.destination} "
              f"is Rs {self.fare} per ticket.")


# user input
name = input("Enter train name: ")
source = input("Enter source station: ")
destination = input("Enter destination station: ")

t1 = Train(name, source, destination, seats=100, fare=750)

print("\nTrain No:", t1.train_no)
t1.get_fare()
t1.get_status()

n = int(input("\nHow many tickets to book? "))
t1.book_ticket(n)
t1.get_status()

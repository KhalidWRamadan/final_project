class bus():
    busDestination = ["1- Nusirat To Gaza", "2- Rafah To Deir-Al balah", "3- Jabalia To Khan Younis",
                      "4- Zahra To Gaza"]
    bus_seats1 = ["a1", "a2", "b1", "b2", "c1", "c2", "d1", "d2", "e1", "e2", "f1", "f2", "g1", "g2", "h1", "h2", "i1",
                 "i2", "j1", "j2"]
    bus_seats2 = ["a1", "a2", "b1", "b2", "c1", "c2", "d1", "d2", "e1", "e2", "f1", "f2", "g1", "g2", "h1", "h2", "i1",
                  "i2", "j1", "j2"]
    bus_seats3 = ["a1", "a2", "b1", "b2", "c1", "c2", "d1", "d2", "e1", "e2", "f1", "f2", "g1", "g2", "h1", "h2", "i1",
                  "i2", "j1", "j2"]
    bus_seats4 = ["a1", "a2", "b1", "b2", "c1", "c2", "d1", "d2", "e1", "e2", "f1", "f2", "g1", "g2", "h1", "h2", "i1",
                  "i2", "j1", "j2"]

    def view_destination(self):
        for i in self.busDestination:
            print(i, "\n")

    def view_seats(self,destination):
        if destination == 1:
            print("---------------------------------------------------------------------")
            print("-------- available seats in Nusirat To Gaza bus --------")
            print(*self.bus_seats1)
        elif destination == 2:
            print("---------------------------------------------------------------------")
            print("-------- available seats in Rafah To Deir-Al balah bus --------")
            print(*self.bus_seats2)
        elif destination == 3:
            print("---------------------------------------------------------------------")
            print("-------- available seats in Jabalia To Khan Younis bus --------")
            print(*self.bus_seats3)

        elif destination == 4:
            print("---------------------------------------------------------------------")
            print("-------- available seats in Zahra To Gaza bus --------")
            print(*self.bus_seats4)

    def book_seat(self, destination, seat):
        if destination == 1:

            nusirat_seats = any(seat in sublist for sublist in self.bus_seats1)
            if nusirat_seats == True:
                self.bus_seats1.remove(seat)
                print("Thank You for booking seat number ", seat)
            else:
                print("Sorry this seat is not available ")
        elif destination == 2:

            Rafah_seats = any(seat in sublist for sublist in self.bus_seats2)
            if Rafah_seats == True:
                self.bus_seats2.remove(seat)
                print("Thank You for booking seat number ", seat)
            else:
                print("Sorry this seat is not available ")
        elif destination == 3:

            Jabalia_seats = any(seat in sublist for sublist in self.bus_seats3)
            if Jabalia_seats == True:
                self.bus_seats3.remove(seat)
                print("Thank You for booking seat number ", seat)
            else:
                print("Sorry this seat is not available ")
        elif destination == 4:

            Zahra_seats = any(seat in sublist for sublist in self.bus_seats4)
            if Zahra_seats == True:
                self.bus_seats4.remove(seat)
                print("Thank You for booking seat number ", seat)
            else:
                print("Sorry this seat is not available ")
        else:
            print("invalid destination number")

obj = bus()



def menu():
    global available_seat, seat
    print("Welcome to Khalid bus station\n")
    print("1- view bus destinations\n"
          "2- view available seats in each bus\n"
          "3- book a seat\n"
          "4- quit")
    command = int(input("choose command number: "))
    if command == 1:
        obj.view_destination()
    elif command == 2:
        obj.view_destination()
        des = int(input("Please, Enter destination number: "))
        obj.view_seats(des)
    elif command == 3:
        obj.view_destination()
        des = int(input("Please, Enter destination number: "))
        if des == 1:
            available_seat = obj.bus_seats1
            print("Available seats in this bus : ", *available_seat)
            seat = input("Enter seat number: ")
        elif des == 2:
            available_seat = obj.bus_seats2
            print("Available seats in this bus : ", *available_seat)
            seat = input("Enter seat number: ")
        elif des == 3:
            available_seat = obj.bus_seats3
            print("Available seats in this bus : ", *available_seat)
            seat = input("Enter seat number: ")
        elif des == 4:
            available_seat = obj.bus_seats4
            print("Available seats in this bus : ", *available_seat)
            seat = input("Enter seat number: ")
        else:
            print("Destination number not available")
            quit()


        obj.book_seat(des,seat)
    elif command == 4:
       print("Thank you for choosing us :)")
    else: print("invalid command number, try again")

menu()
while True:

    check = input("Do you want to choose again ? ")

    if check == "yes":
        menu()
    elif check == "no":
        print("Thank you for choosing us :)")
        break
    else:
        print("invalid command number, try again")


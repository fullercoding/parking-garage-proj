from IPython.display import clear_output
spots = {1:"Open", 2:"Open", 3:"Open", 4:"Open", 5:"Open", }
pay_status = {1: True, 2: True, 3: True, 4: True, 5: True}

class garage():
    def __init__(self, spots, count):
        self.spots = spots
        self.count = count
    
    def take_ticket():
        count = 1
        while True:
            if count == 6:
                print("All spots are filled at max capacity, please come back later")
                break
            elif spots[count] == "Taken":
                count += 1
            elif spots[count] == "Open":
                spots[count] = "Taken"
                print(f"You have taken spot {count}")
                break

    def pay_for_parking():
        while True:
            result = input("Please input the parking spot you would like to pay for. Spots 1-6: ")
            if int(result) > 0 and int(result) < 6:
                if spots[int(result)] == "Open":
                    clear_output()
                    print("That spot is currently open, would you like to try again?")
                else:
                    clear_output()
                    spots[int(result)] = "Open"
                    pay_status[int(result)] = True
                    print("Thanks for paying")
                    break
            else:
                clear_output()
                print("Invalid parking spot, try again")
                break
    
    def leave_garage():
        while True:
            result = input("Please input your parking spot number: ")
            if int(result) > 0 and int(result) < 6:
                if pay_status[int(result)] == True:
                    clear_output()
                    pay_status[int(result)] = False
                    print("You are free to leave!")
                    break
                else:
                    clear_output()
                    print("Slow down, you must pay before leaving")
                    garage.pay_for_parking()
            else:
                print("That spot is invalid, try again")
                clear_output()

    def run_garage():
        while True:
            
            print(spots)
            result = input("Would you like to Park, Pay, Leave, Or Quit?: ")
            if result.lower() == "quit":
                exit()
            elif result.lower() == "park":
                garage.take_ticket()
            elif result.lower() == "pay":
                garage.pay_for_parking()
            elif result.lower() == "leave":
                garage.leave_garage()
            else: 
                print("Option not avaliable")

garage.run_garage()

class Cafe:
    def __init__(self):
        self.menu()
        pass
    
    def menu (self):
        print(f"""Please choose an option:
            1. Order Food/Drink
            2. View Menu
            3. Check Order Status
            4. Get Bill
            5. Exit""")
        options = { 1: self.order_food_drink,
                    2: self.view_menu,
                    3: self.check_order_status,
                    4: self.get_bill,
                    5: self.exit_cafe,
                   }
        try:
            user_input = int()
        except ValueError:
            print("Please choose the valid option")
            
        user_input = int(input("Enter your choice: "))

        func = options.get(user_input, self.invalid_option)
        func()

    def order_food_drink(self):
        print("Ordering food/drink...")

    def view_menu(self):
        print("Viewing menu...")

    def check_order_status(self):
        print("Checking order status...")

    def get_bill(self):
        print("Getting bill...")

    def exit_cafe(self):
        print("Exiting the cafe.")

    def invalid_option(self):
        print("Invalid option, please try again.")

    def new_feature(self):
        print("New feature called.")

if __name__ == "__main__":
    cafe = Cafe()
            
cafe = Cafe()
        
      
            
        
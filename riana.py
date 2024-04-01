import tkinter as tk  # Importing the tkinter library and aliasing it as tk
from tkinter import *  # Importing all classes from tkinter module
from tkinter import messagebox  # Importing messagebox class from tkinter module


class RentGUI2:
    def __init__(self, return_to_home, rent_riana, properties1, properties2, properties3):
        """
        Initialize the RentGUI2 class.

        Parameters:
            return_to_home (function): Function to return to the home screen.
            rent_riana (function): Function to handle renting Riana South property.
            properties1 (list): List of properties.
            properties2 (list): List of properties.
            properties3 (list): List of properties.
        """
        self.return_to_home = return_to_home  # Assigning return_to_home parameter to instance variable
        self.rent_riana = rent_riana  # Assigning rent_riana parameter to instance variable
        self.properties1 = properties1  # Assigning properties1 parameter to instance variable
        self.properties2 = properties2  # Assigning properties2 parameter to instance variable
        self.properties3 = properties3  # Assigning properties3 parameter to instance variable
        self.root = tk.Tk()  # Creating a Tkinter window
        self.root.title("Hotel Room Rental")  # Setting window title
        self.root.iconbitmap("144-1444917_white-dollar-sign-png-png-black-and-white.ico")  # Setting window icon
        self.root.geometry("400x600")  # Setting window size
        self.root.resizable(False, False)  # Making window non-resizable
        self.font_style = "Tikiisland"  # Setting font style

        self.rental_duration = tk.StringVar()  # Creating a variable to store rental duration
        self.price_per_unit = {"Hour": 50, "Day": 400, "Week": 2500}  # Dictionary to store price per unit

        self.price_label = tk.Label(self.root, text="Price: RM50", font=("TikiIsland", 25))  # Creating price label
        self.price_label.pack(pady=10)  # Placing price label

        # Rental duration dropdown menu
        self.rental_label = tk.Label(self.root, text="Select Rental Duration:", font=("TikiIsland", 25))  # Creating rental label
        self.rental_label.pack(pady=2)  # Placing rental label
        self.rental_menu = tk.OptionMenu(self.root, self.rental_duration, *self.price_per_unit.keys(),  # Creating rental menu
                                         command=self.update_price)
        self.rental_menu.pack()  # Placing rental menu

        self.duration_label = tk.Label(self.root, text="Enter Duration:", font=("TikiIsland", 20))  # Creating duration label
        self.duration_label.pack(pady=2)  # Placing duration label
        self.duration_entry = tk.Entry(self.root, width=20, font=(self.font_style, 12))  # Creating duration entry field
        self.duration_entry.pack(pady=2)  # Placing duration entry field

        self.family_members_label = tk.Label(self.root, text="Family Members:", font=("TikiIsland", 20))  # Creating family members label
        self.family_members_label.pack(pady=2)  # Placing family members label
        self.family_members_entry = tk.Entry(self.root, width=10, font=(self.font_style, 12))  # Creating family members entry field
        self.family_members_entry.pack(pady=2)  # Placing family members entry field

        self.name_label = tk.Label(self.root, text="Name:", font=("TikiIsland", 20))  # Creating name label
        self.name_label.pack(pady=2)  # Placing name label
        self.name_entry = tk.Entry(self.root, width=30, font=(self.font_style, 12))  # Creating name entry field
        self.name_entry.pack(pady=2)  # Placing name entry field

        self.phone_label = tk.Label(self.root, text="Phone Number:", font=("TikiIsland", 20))  # Creating phone number label
        self.phone_label.pack(pady=2)  # Placing phone number label
        self.phone_entry = tk.Entry(self.root, width=30, font=(self.font_style, 12))  # Creating phone number entry field
        self.phone_entry.pack(pady=2)  # Placing phone number entry field

        self.email_label = tk.Label(self.root, text="Email:", font=("TikiIsland", 20))  # Creating email label
        self.email_label.pack(pady=2)  # Placing email label
        self.email_entry = tk.Entry(self.root, width=30, font=(self.font_style, 12))  # Creating email entry field
        self.email_entry.pack(pady=2)  # Placing email entry field

        self.card_label = tk.Label(self.root, text="Card Info:", font=("TikiIsland", 20))  # Creating card info label
        self.card_label.pack(pady=2)  # Placing card info label
        self.card_entry = tk.Entry(self.root, width=30, font=(self.font_style, 12))  # Creating card info entry field
        self.card_entry.pack(pady=2)  # Placing card info entry field

        self.book_button = tk.Button(self.root, text="Book Room", command=self.book_room, font=("TikiIsland", 20))  # Creating book button
        self.book_button.pack(pady=5)  # Placing book button
        self.riana_booked = False  # Flag to track if Riana South property is booked

    def update_price(self, event=None):
        """
        Update the price label based on selected rental duration.
        """
        duration = self.rental_duration.get()  # Getting selected rental duration
        if duration in self.price_per_unit:  # Checking if selected duration is in price_per_unit dictionary
            self.price_label.config(text=f"Price: RM{self.price_per_unit[duration]}")  # Updating price label

    def book_room(self):
        """
        Book a room based on user input and update property booking status.
        """
        name = self.name_entry.get()  # Getting name from entry field
        phone = self.phone_entry.get()  # Getting phone number from entry field
        email = self.email_entry.get()  # Getting email from entry field
        card_info = self.card_entry.get()  # Getting card info from entry field
        duration = self.duration_entry.get()  # Getting duration from entry field
        rental_type = self.rental_duration.get()  # Getting rental type from dropdown menu
        family_members = self.family_members_entry.get()  # Getting number of family members from entry field

        if name and phone and email and card_info and duration and rental_type and family_members.isdigit():  # Checking if all fields are filled and family members is a number
            try:
                duration = int(duration)  # Converting duration to integer
                total_price = self.price_per_unit.get(rental_type, 0) * duration  # Calculating total price
                if 2 <= int(family_members) <= 4:  # Checking if number of family members is between 2 and 4
                    total_price *= 0.75  # Apply 25% discount for 2-4 family members

                if total_price > 0:  # Checking if total price is valid
                    for prop_list in [self.properties1, self.properties2, self.properties3]:  # Iterating over property lists
                        for property_info in prop_list:  # Iterating over properties in each list
                            if property_info["name"] == "Riana South":  # Checking if property name matches
                                if property_info["booked"]:  # Checking if property is already booked
                                    messagebox.showerror("Error", "This property is already fully booked.")  # Showing error message
                                    return
                                else:
                                    property_info["booked"] = True  # Marking property as booked
                                    print(f"The booking status for {property_info['name']} has been updated to: {property_info['booked']}")  # Printing booking status
                                    break

                    messagebox.showinfo("Booking Confirmation",  # Showing booking confirmation message
                                        f"Room booked successfully for {duration} {rental_type}(s)!\nTotal Price: RM{total_price}")
                    self.root.destroy()  # Destroying the window after successful booking
                else:
                    messagebox.showerror("Error", "Invalid rental type selected.")  # Showing error message
            except ValueError:
                messagebox.showerror("Error", "Invalid input for duration or family members.")  # Showing error message
        else:
            messagebox.showerror("Error",  # Showing error message if any required field is empty or family members is not a number
                                 "Please fill in all the required fields and provide a valid number of family members.")


    def run(self):
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            pass
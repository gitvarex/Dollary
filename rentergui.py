import tkinter as tk  # Importing the tkinter library and aliasing it as tk
from tkinter import *  # Importing all classes from tkinter module


class RenterGUI:
    def __init__(self, return_to_home, rent_puncak, rent_riana, rent_angkasa, properties1, properties2, properties3):
        """
        Initialize the RenterGUI class.

        Parameters:
            return_to_home (function): Function to return to the home screen.
            rent_puncak (function): Function to rent a property.
            rent_riana (function): Function to rent a property.
            rent_angkasa (function): Function to rent a property.
            properties1 (list): List of properties.
            properties2 (list): List of properties.
            properties3 (list): List of properties.
        """
        self.return_to_home = return_to_home  # Assigning return_to_home parameter to instance variable
        self.rent_puncak = rent_puncak  # Assigning rent_puncak parameter to instance variable
        self.properties1 = properties1  # Assigning properties1 parameter to instance variable
        self.properties2 = properties2  # Assigning properties2 parameter to instance variable
        self.properties3 = properties3  # Assigning properties3 parameter to instance variable
        self.rent_riana = rent_riana  # Assigning rent_riana parameter to instance variable
        self.rent_angkasa = rent_angkasa  # Assigning rent_angkasa parameter to instance variable
        self.root = tk.Tk()  # Creating a Tkinter window
        self.root.title("Dollary: All Your Rental Service Needs.")  # Setting window title
        self.root.iconbitmap("144-1444917_white-dollar-sign-png-png-black-and-white.ico")  # Setting window icon
        self.root.geometry("800x600")  # Setting window size
        self.root.resizable(False, False)  # Making window non-resizable

        # Creating labels for welcome message and flat rentals
        welcome_msg = tk.Label(self.root, text="Welcome Renter!", fg="black", font=("TikiIsland", 25))
        welcome_msg.place(relx=0.5, rely=0.06, anchor=tk.CENTER)
        flat_rental_msg = tk.Label(self.root, text="Flat Rentals", fg="black", font=("TikiIsland", 18))
        flat_rental_msg.place(relx=0.5, rely=0.13, anchor=tk.CENTER)

        properties = [self.properties1, self.properties2, self.properties3]  # List of property lists

        y_offset = 0.3  # Initial offset for placing labels

        # Loop through each property list
        for prop_list in properties:
            for i, property_info in enumerate(prop_list):  # Loop through each property info dictionary
                property_height = 0  # Reset property height for each property
                # Loop through property info and calculate label height
                for _ in [f"Property: {property_info['name']}",
                          f"Address: {property_info['address']}",
                          f"City: {property_info['city']}"]:
                    label_height = 0.07  # Height of each label
                    property_height += label_height  # Accumulate total height

                y_offset += property_height  # Adjust y_offset based on total height

                # Create labels for property name, address, and city
                property_name_label = tk.Label(self.root, text=f"Property: {property_info['name']}", fg="black",
                                               font=("TikiIsland", 18))
                property_name_label.place(relx=0.05, rely=y_offset - property_height, anchor=tk.W)

                address_label = tk.Label(self.root, text=f"Address: {property_info['address']}", fg="black",
                                         font=("TikiIsland", 18))
                address_label.place(relx=0.05, rely=y_offset - property_height + 0.05, anchor=tk.W)

                city_label = tk.Label(self.root, text=f"City: {property_info['city']}", fg="black",
                                      font=("TikiIsland", 18))
                city_label.place(relx=0.05, rely=y_offset - property_height + 0.1, anchor=tk.W)

        # Creating a button to return to login screen
        self.go_back = tk.Button(self.root, text="Return to Login", command=return_to_home, bg="White",
                                 fg="Black", font=("TikiIsland", 10))
        self.go_back.place(relx=0.92, rely=0.95, anchor=tk.CENTER)

        # Creating buttons to rent units for each property
        riana_south_rental = Button(self.root, text="Rent Unit", fg="Black",
                                    command=lambda: self.rent_riana(self.properties1, self.properties2,
                                                                    self.properties3),
                                    font=("TikiIsland", 15), width=10, height=1)
        riana_south_rental.place(relx=0.85, rely=0.35, anchor=tk.CENTER)

        puncak_banyan_rental = Button(self.root, text="Rent Unit", fg="Black",
                                      command=lambda: self.rent_puncak(self.properties1, self.properties2,
                                                                       self.properties3),
                                      font=("TikiIsland", 15), width=10, height=1)
        puncak_banyan_rental.place(relx=0.85, rely=0.55, anchor=tk.CENTER)

        angkasa_rental = Button(self.root, text="Rent Unit", fg="Black",
                                command=lambda: self.rent_angkasa(self.properties1, self.properties2,
                                                                  self.properties3),
                                font=("TikiIsland", 15), width=10, height=1)
        angkasa_rental.place(relx=0.85, rely=0.75, anchor=tk.CENTER)

    def run(self):
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            pass

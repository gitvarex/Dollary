import tkinter as tk
from tkinter import *


class RenterGUI:
    def __init__(self, return_to_home, rent_puncak, rent_riana, rent_angkasa, properties1, properties2, properties3):
        self.return_to_home = return_to_home
        self.rent_puncak = rent_puncak
        self.properties1 = properties1
        self.properties2 = properties2
        self.properties3 = properties3
        self.rent_riana = rent_riana
        self.rent_angkasa = rent_angkasa
        self.root = tk.Tk()
        self.root.title("Dollary: All Your Rental Service Needs.")
        self.root.iconbitmap("144-1444917_white-dollar-sign-png-png-black-and-white.ico")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        welcome_msg = tk.Label(self.root, text="Welcome Renter!", fg="black", font=("TikiIsland", 25))
        welcome_msg.place(relx=0.5, rely=0.06, anchor=tk.CENTER)
        flat_rental_msg = tk.Label(self.root, text="Flat Rentals", fg="black", font=("TikiIsland", 18))
        flat_rental_msg.place(relx=0.5, rely=0.13, anchor=tk.CENTER)

        properties = [self.properties1, self.properties2, self.properties3]

        y_offset = 0.3

        for prop_list in properties:
            for i, property_info in enumerate(prop_list):
                property_height = 0
                for _ in [f"Property: {property_info['name']}",
                          f"Address: {property_info['address']}",
                          f"City: {property_info['city']}"]:
                    label_height = 0.07
                    property_height += label_height

                y_offset += property_height

                property_name_label = tk.Label(self.root, text=f"Property: {property_info['name']}", fg="black",
                                               font=("TikiIsland", 18))
                property_name_label.place(relx=0.05, rely=y_offset - property_height, anchor=tk.W)

                address_label = tk.Label(self.root, text=f"Address: {property_info['address']}", fg="black",
                                         font=("TikiIsland", 18))
                address_label.place(relx=0.05, rely=y_offset - property_height + 0.05, anchor=tk.W)

                city_label = tk.Label(self.root, text=f"City: {property_info['city']}", fg="black",
                                      font=("TikiIsland", 18))
                city_label.place(relx=0.05, rely=y_offset - property_height + 0.1, anchor=tk.W)

        self.go_back = tk.Button(self.root, text="Return to Login", command=return_to_home, bg="White",
                                 fg="Black", font=("TikiIsland", 10))
        self.go_back.place(relx=0.92, rely=0.95, anchor=tk.CENTER)

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

import tkinter as tk
from tkinter import *
from tkinter import messagebox


class RentGUI2:
    def __init__(self, return_to_home, rent_riana, properties1, properties2, properties3):
        self.return_to_home = return_to_home
        self.rent_riana = rent_riana
        self.properties1 = properties1
        self.properties2 = properties2
        self.properties3 = properties3
        self.root = tk.Tk()
        self.root.title("Hotel Room Rental")
        self.root.iconbitmap("144-1444917_white-dollar-sign-png-png-black-and-white.ico")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.font_style = "Tikiisland"

        self.rental_duration = tk.StringVar()
        self.price_per_unit = {"Hour": 50, "Day": 400, "Week": 2500}

        self.price_label = tk.Label(self.root, text="Price: RM50", font=("TikiIsland", 25))
        self.price_label.pack(pady=10)

        # Rental duration dropdown menu
        self.rental_label = tk.Label(self.root, text="Select Rental Duration:", font=("TikiIsland", 25))
        self.rental_label.pack(pady=2)
        self.rental_menu = tk.OptionMenu(self.root, self.rental_duration, *self.price_per_unit.keys(),
                                         command=self.update_price)
        self.rental_menu.pack()

        self.duration_label = tk.Label(self.root, text="Enter Duration:", font=("TikiIsland", 20))
        self.duration_label.pack(pady=2)
        self.duration_entry = tk.Entry(self.root, width=20, font=(self.font_style, 12))
        self.duration_entry.pack(pady=2)

        self.family_members_label = tk.Label(self.root, text="Family Members:", font=("TikiIsland", 20))
        self.family_members_label.pack(pady=2)
        self.family_members_entry = tk.Entry(self.root, width=10, font=(self.font_style, 12))
        self.family_members_entry.pack(pady=2)

        self.name_label = tk.Label(self.root, text="Name:", font=("TikiIsland", 20))
        self.name_label.pack(pady=2)
        self.name_entry = tk.Entry(self.root, width=30, font=(self.font_style, 12))
        self.name_entry.pack(pady=2)

        self.phone_label = tk.Label(self.root, text="Phone Number:", font=("TikiIsland", 20))
        self.phone_label.pack(pady=2)
        self.phone_entry = tk.Entry(self.root, width=30, font=(self.font_style, 12))
        self.phone_entry.pack(pady=2)

        self.email_label = tk.Label(self.root, text="Email:", font=("TikiIsland", 20))
        self.email_label.pack(pady=2)
        self.email_entry = tk.Entry(self.root, width=30, font=(self.font_style, 12))
        self.email_entry.pack(pady=2)

        self.card_label = tk.Label(self.root, text="Card Info:", font=("TikiIsland", 20))
        self.card_label.pack(pady=2)
        self.card_entry = tk.Entry(self.root, width=30, font=(self.font_style, 12))
        self.card_entry.pack(pady=2)

        self.book_button = tk.Button(self.root, text="Book Room", command=self.book_room, font=("TikiIsland", 20))
        self.book_button.pack(pady=5)
        self.riana_booked = False

    def update_price(self, event=None):
        duration = self.rental_duration.get()
        if duration in self.price_per_unit:
            self.price_label.config(text=f"Price: RM{self.price_per_unit[duration]}")

    def book_room(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        card_info = self.card_entry.get()
        duration = self.duration_entry.get()
        rental_type = self.rental_duration.get()
        family_members = self.family_members_entry.get()

        if name and phone and email and card_info and duration and rental_type and family_members.isdigit():
            try:
                duration = int(duration)
                total_price = self.price_per_unit.get(rental_type, 0) * duration
                if 2 <= int(family_members) <= 4:
                    total_price *= 0.75  # Apply 25% discount for 2-4 family members

                if total_price > 0:
                    for prop_list in [self.properties1, self.properties2, self.properties3]:
                        for property_info in prop_list:
                            if property_info["name"] == "Riana South":  # Change property name accordingly
                                if property_info["booked"]:
                                    messagebox.showerror("Error", "This property is already fully booked.")
                                    return
                                else:
                                    property_info["booked"] = True
                                    print(
                                        f"The booking status for {property_info['name']} has been updated to: {property_info['booked']}")
                                    break

                    messagebox.showinfo("Booking Confirmation",
                                        f"Room booked successfully for {duration} {rental_type}(s)!\nTotal Price: RM{total_price}")
                    self.root.destroy()
                else:
                    messagebox.showerror("Error", "Invalid rental type selected.")
            except ValueError:
                messagebox.showerror("Error", "Invalid input for duration or family members.")
        else:
            messagebox.showerror("Error",
                                 "Please fill in all the required fields and provide a valid number of family members.")

    def run(self):
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            pass
import tkinter as tk
from tkinter import *
from admingui import AdminGUI
from rentergui import RenterGUI
from puncak import RentGUI
from riana import RentGUI2
from angkasa import RentGUI3


class Dollary:
    def __init__(self, app, properties1, properties2, properties3):
        self.app = app
        self.app.title("Dollary: All Your Rental Service Needs.")
        self.app.geometry("600x500")
        self.app.iconbitmap("144-1444917_white-dollar-sign-png-png-black-and-white.ico")
        self.app.resizable(False, False)
        self.properties1 = properties1
        self.properties2 = properties2
        self.properties3 = properties3
        admin_btn = Button(self.app, command=self.open_admin_gui, text="Admin", bg="White", fg="Black",
                           font=("TikiIsland", 20), width=15, height=1)
        admin_btn.place(relx=0.5, rely=0.41, anchor=tk.CENTER)
        renter_btn = Button(self.app, command=self.open_renter_gui, text="Renter", bg="White", fg="Black",
                            font=("TikiIsland", 20), width=15, height=1)

        renter_btn.place(relx=0.5, rely=0.56, anchor=tk.CENTER)

    def open_admin_gui(self):
        self.app.withdraw()
        admin_gui = AdminGUI(self.return_to_home, self.properties1, self.properties2, self.properties3)
        admin_gui.run()

    def open_renter_gui(self):
        self.app.withdraw()
        renter_gui = RenterGUI(self.return_to_home, self.rent_puncak, self.rent_riana, self.rent_riana, self.properties1, self.properties2,
                               self.properties3)
        renter_gui.run()

    def return_to_home(self):
        self.app.deiconify()

    def rent_puncak(self, properties1, properties2, properties3):
        self.app.withdraw()
        hotel_rental = RentGUI(self.return_to_home, self.rent_puncak, properties1, properties2, properties3)
        hotel_rental.run()

    def rent_riana(self, properties1, properties2, properties3):
        self.app.withdraw()
        hotel_rental2 = RentGUI2(self.return_to_home, self.rent_riana, properties1, properties2, properties3)
        hotel_rental2.run()

    def rent_angkasa(self, properties1, properties2, properties3):
        self.app.withdraw()
        hotel_rental3 = RentGUI3(self.return_to_home, self.rent_angkasa, properties1, properties2, properties3)
        hotel_rental3.run()


if __name__ == "__main__":
    m = tk.Tk()

    app = Dollary(m)
    m.mainloop()

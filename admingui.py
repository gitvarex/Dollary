import tkinter as tk
from tkinter import *
from tkinter import messagebox


class InvoicePopup:
    def __init__(self, root):
        self.root = root
        self.root.title("Send Invoice")
        self.root.geometry("300x200")
        self.root.iconbitmap("144-1444917_white-dollar-sign-png-png-black-and-white.ico")

        self.email_label = tk.Label(self.root, text="Email:", font=("TikiIsland", 20))
        self.email_label.pack(pady=5)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack(pady=5)

        self.amount_label = tk.Label(self.root, text="Amount:", font=("TikiIsland", 20))
        self.amount_label.pack(pady=5)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=5)

        self.send_button = tk.Button(self.root, text="Send Invoice", command=self.send_invoice, font=("TikiIsland", 15))
        self.send_button.pack(pady=10)

    def send_invoice(self):
        email = self.email_entry.get()
        amount = self.amount_entry.get()
        if email and amount:
            messagebox.showinfo("Invoice Sent", f"Invoice sent to {email} for amount {amount}")
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Please enter email and amount.")


class AdminGUI:
    def __init__(self, return_to_home, properties1, properties2, properties3):
        self.return_to_home = return_to_home
        self.properties1 = properties1
        self.properties2 = properties2
        self.properties3 = properties3
        self.root = tk.Tk()
        self.root.title("Dollary: All Your Rental Service Needs.")
        self.root.iconbitmap("144-1444917_white-dollar-sign-png-png-black-and-white.ico")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        welcome_msg1 = Label(self.root, text="Welcome Admin!", fg= 'black', font=("TikiIsland", 20))
        welcome_msg1.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.invoice_button = tk.Button(self.root, text="Send Invoice", command=self.send_invoice,bg= "White",fg = "Black", font=("TikiIsland", 15),width=20, height=2)
        self.invoice_button.pack()
        self.invoice_button.place(relx=0.25, rely=0.41, anchor=tk.CENTER)

        self.availability_button = tk.Button(self.root, text="Show Availability", command=self.show_availability, bg= "White",fg = "Black", font=("TikiIsland", 15),width=20, height=2)
        self.availability_button.place(relx=0.75, rely=0.41, anchor=tk.CENTER)


        self.go_back = tk.Button(self.root, text="Return to Login", command=return_to_home, bg="White",
                                 fg="Black", font=("TikiIsland", 10))
        self.go_back.place(relx=0.92, rely=0.95, anchor=tk.CENTER)

    def send_invoice(self):
        popup = tk.Toplevel()
        invoice_popup = InvoicePopup(popup)

    def show_availability(self):
        availability_window = tk.Toplevel()
        availability_window.title("Property Availability")
        availability_window.geometry("400x300")
        availability_window.iconbitmap("144-1444917_white-dollar-sign-png-png-black-and-white.ico")

        # Display properties and their booked status
        for i, properties_list in enumerate([self.properties1, self.properties2, self.properties3]):
            property_frame = tk.Frame(availability_window, pady=20)
            property_frame.pack()

            property_label = tk.Label(property_frame, text=f"Property {i + 1}:", font=("TikiIsland", 20))
            property_label.grid(row=0, column=0)

            # Check if any property in the list is booked
            status = "Booked" if any(property_info["booked"] for property_info in properties_list) else "Available"
            status_label = tk.Label(property_frame, text=status, font=("TikiIsland", 20))
            status_label.grid(row=0, column=1)


    def run(self):
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            pass
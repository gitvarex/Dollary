import tkinter as tk  # Importing the tkinter library and aliasing it as tk
from tkinter import *  # Importing all classes from tkinter module
from tkinter import messagebox  # Importing messagebox class from tkinter module


class InvoicePopup:
    def __init__(self, root):
        """
        Initialize the InvoicePopup class.

        Parameters:
            root (Tk): The Tkinter root window.
        """
        self.root = root  # Assigning root parameter to instance variable
        self.root.title("Send Invoice")  # Setting window title
        self.root.geometry("300x200")  # Setting window size
        self.root.iconbitmap("144-1444917_white-dollar-sign-png-png-black-and-white.ico")  # Setting window icon

        self.email_label = tk.Label(self.root, text="Email:", font=("TikiIsland", 20))  # Creating email label
        self.email_label.pack(pady=5)  # Placing email label
        self.email_entry = tk.Entry(self.root)  # Creating email entry field
        self.email_entry.pack(pady=5)  # Placing email entry field

        self.amount_label = tk.Label(self.root, text="Amount:", font=("TikiIsland", 20))  # Creating amount label
        self.amount_label.pack(pady=5)  # Placing amount label
        self.amount_entry = tk.Entry(self.root)  # Creating amount entry field
        self.amount_entry.pack(pady=5)  # Placing amount entry field

        self.send_button = tk.Button(self.root, text="Send Invoice", command=self.send_invoice, font=("TikiIsland", 15))  # Creating send button
        self.send_button.pack(pady=10)  # Placing send button

    def send_invoice(self):
        """
        Send invoice based on email and amount provided.
        """
        email = self.email_entry.get()  # Getting email from entry field
        amount = self.amount_entry.get()  # Getting amount from entry field
        if email and amount:  # Checking if both email and amount are provided
            messagebox.showinfo("Invoice Sent", f"Invoice sent to {email} for amount {amount}")  # Showing info message box
            self.root.destroy()  # Destroying the popup window
        else:
            messagebox.showerror("Error", "Please enter email and amount.")  # Showing error message box if email or amount is not provided


class AdminGUI:
    def __init__(self, return_to_home, properties1, properties2, properties3):
        """
        Initialize the AdminGUI class.

        Parameters:
            return_to_home (function): Function to return to the home screen.
            properties1 (list): List of properties.
            properties2 (list): List of properties.
            properties3 (list): List of properties.
        """
        self.return_to_home = return_to_home  # Assigning return_to_home parameter to instance variable
        self.properties1 = properties1  # Assigning properties1 parameter to instance variable
        self.properties2 = properties2  # Assigning properties2 parameter to instance variable
        self.properties3 = properties3  # Assigning properties3 parameter to instance variable
        self.root = tk.Tk()  # Creating a Tkinter window
        self.root.title("Dollary: All Your Rental Service Needs.")  # Setting window title
        self.root.iconbitmap("144-1444917_white-dollar-sign-png-png-black-and-white.ico")  # Setting window icon
        self.root.geometry("800x600")  # Setting window size
        self.root.resizable(False, False)  # Making window non-resizable

        welcome_msg1 = Label(self.root, text="Welcome Admin!", fg= 'black', font=("TikiIsland", 20))  # Creating welcome message label
        welcome_msg1.place(relx=0.5, rely=0.1, anchor=tk.CENTER)  # Placing welcome message label

        # Creating buttons for sending invoice and showing availability
        self.invoice_button = tk.Button(self.root, text="Send Invoice", command=self.send_invoice,bg= "White",fg = "Black", font=("TikiIsland", 15),width=20, height=2)
        self.invoice_button.pack()
        self.invoice_button.place(relx=0.25, rely=0.41, anchor=tk.CENTER)

        self.availability_button = tk.Button(self.root, text="Show Availability", command=self.show_availability, bg= "White",fg = "Black", font=("TikiIsland", 15),width=20, height=2)
        self.availability_button.place(relx=0.75, rely=0.41, anchor=tk.CENTER)

        # Creating a button to return to login screen
        self.go_back = tk.Button(self.root, text="Return to Login", command=return_to_home, bg="White",
                                 fg="Black", font=("TikiIsland", 10))
        self.go_back.place(relx=0.92, rely=0.95, anchor=tk.CENTER)

    def send_invoice(self):
        """
        Open a popup window to send an invoice.
        """
        popup = tk.Toplevel()  # Creating a new popup window
        invoice_popup = InvoicePopup(popup)  # Creating InvoicePopup object in the popup window

    def show_availability(self):
        """
        Display the availability of properties in a new window.
        """
        availability_window = tk.Toplevel()  # Creating a new window for displaying availability
        availability_window.title("Property Availability")  # Setting window title
        availability_window.geometry("400x300")  # Setting window size
        availability_window.iconbitmap("144-1444917_white-dollar-sign-png-png-black-and-white.ico")  # Setting window icon

        # Display properties and their booked status
        for i, properties_list in enumerate([self.properties1, self.properties2, self.properties3]):
            property_frame = tk.Frame(availability_window, pady=20)  # Creating frame for each property
            property_frame.pack()  # Packing property frame

            property_label = tk.Label(property_frame, text=f"Property {i + 1}:", font=("TikiIsland", 20))  # Creating label for property
            property_label.grid(row=0, column=0)  # Placing property label

            # Check if any property in the list is booked
            status = "Booked" if any(property_info["booked"] for property_info in properties_list) else "Available"
            status_label = tk.Label(property_frame, text=status, font=("TikiIsland", 20))  # Creating label for status
            status_label.grid(row=0, column=1)  # Placing status label


    def run(self):
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            pass
from landingpage import Dollary
import tkinter as tk

if __name__ == "__main__":
    m = tk.Tk()
    properties1 = [
        {"name": "Riana South", "address": "Jalan Mandarina Damai 1", "city": "Kuala Lumpur", "booked": False},
    ]

    properties2 = [
        {"name": "Puncak Banyan", "address": "Jalan Puncak Gading", "city": "Kuala Lumpur", "booked": False},
    ]

    properties3 = [
        {"name": "Angkasa Condominiums", "address": "Jalan Puncak Menara Gading", "city": "Kuala Lumpur",
         "booked": True}
    ]

    app = Dollary(m, properties1, properties2, properties3)
    m.mainloop()

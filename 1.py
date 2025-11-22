import tkinter as tk
from tkinter import ttk,messagebox

class RestaurantOrderManagement:
    def __init__(self,root):
        self.root=root
        self.root.title("Restaurant Order Management App")
        self.menu_items={
            "Burger":2,
            "Pizza":2,
            "Pasta":3,
            "Salad":4,
            "Soda":2.0
        }
        self.exchange_rate=80  
        self.setup_background(root)
        frame=ttk.Frame(root)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)


        ttk.Label(frame,
                text="Restaurant Order Management",
                font=("Helvetica",16,"bold")).grid(row=0,columnspan=3,pady=10,padx=10)
        self.menu_labels={}
        self.menu_quantities={}        
        for i,(item,price) in enumerate(self.menu_items.items(),start=1):
            label=ttk.Label(frame,text=f"{item} - ${price:.2f}")
            label.grid(row=i,column=0,pady=5,padx=10,sticky=tk.W)
            self.menu_labels[item]=label
            quantity_entry=ttk.Entry(frame,width=5)
            quantity_entry.grid(row=i,column=1,pady=5,padx=10)
            self.menu_quantities[item]=quantity_entry
        self.currency_var=tk.StringVar()
        ttk.Label(frame,text="Select Currency:").grid(row=len(self.menu_items)+1,column=0,pady=10,padx=10,sticky=tk.W)

        currency_menu=ttk.Combobox(frame,textvariable=self.currency_var,values=["USD","INR"],state="readonly",width=18)
        currency_menu.grid(row=len(self.menu_items)+1,column=1,pady=10,padx=10)
        currency_menu.current(0)
        self.currency_var.trace("w",self.update_prices)
        order_button=ttk.Button(frame,text="Place Order",command=self.place_order)
        order_button.grid(row=len(self.menu_items)+2,columnspan=2,pady=15,padx=10)

    def setup_background(self,root):
        canvas=tk.Canvas(root,width=800,height=600)
        canvas.place(x=0,y=0,relwidth=1,relheight=1)
       
        
        original_image=ttk.PhotoImage(file=r"C:\Users\Shweta Pal\Downloads\Python Folder\Restaurant Management System\background.jpeg")
        bg_width=800
        bg_height=600
        background_image=original_image.subsample(
        max(1, original_image.width() // bg_width),
        max(1,original_image.height() // bg_height))
        canvas.create_image(0,0,anchor="tk.NW",image=background_image)
        canvas.image=background_image
        
    def update_prices(self,*args):
        currency=self.currency_var.get()
        for item,base_price in self.menu_items.items():
            if currency=="INR":
                price=base_price*self.exchange_rate
                symbol="₹"
            else:
                price=base_price
                symbol="$"
            self.menu_labels[item].configure(text=f"{item} - {symbol}{price:.2f}")  
    def place_order(self):
        total_cost=0
        order_summary="Order Summary:\n"
        currency=self.currency_var.get()
        symbol="₹" if currency=="INR" else "$"
        for item,entry in self.menu_quantities.items():
            quantity_text=entry.get()
            if quantity_text.isdigit() and int(quantity_text)>0:
                quantity=int(quantity_text)
                base_price=self.menu_items[item]
                if currency=="INR":
                    price=base_price*self.exchange_rate
                else:
                    price=base_price
                item_cost=price*quantity
                total_cost+=item_cost
                order_summary+=f"{item} x {quantity} = {symbol}{item_cost:.2f}\n"
        if total_cost>0:
            order_summary+=f"\nTotal Cost: {symbol}{total_cost:.2f}"
            messagebox.showinfo("Order Placed",order_summary)
        else:
            messagebox.showerror("No Items","Please enter quantities for at least one item to place an order.")
if __name__=="__main__":
    root=tk.Tk()
    app=RestaurantOrderManagement(root)
    root.geometry("800x600")
    root.mainloop()

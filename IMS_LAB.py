import customtkinter as ctk
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import IMS

app =ctk.CTk()
app.title('Inventory Management System')
app.geometry('800x350')
app.config(bg='black')
app.resizable(False,False)

font1 = ('Arial',25,'bold')
font2 = ('Arial',15,'bold')
font3 = ('Arial',13,'bold')

def display_data(event):
    selected_item=tree.focus()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        id_entry.insert(0,row[0])
        name_entry.insert(0,row[1])
        stock_entry.insert(0,row[2])
        price_entry.insert(0,row[3])
    else:
        pass


def add_to_treeview():
    products=IMS.fetch_product()
    tree.delete(*tree.get_children())
    for product in products:
        tree.insert('',END,values=product)
    

def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
        tree.focus('')
    id_entry.delete(0,END)
    name_entry.delete(0,END)
    stock_entry.delete(0,END)
    price_entry.delete(0,END)

def deleted():
    selected_item=tree.focus()
    if not selected_item:
        messagebox.showerror('Error','Choose a product to delete')
    else:
        id = id_entry.get()
        IMS.delete_Product(id)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success','Data has been deleted')

def update():
    selected_item=tree.focus()
    if not selected_item:
        messagebox.showerror('Error','Choose a product to update')
    else:
        id=id_entry.get()
        name=name_entry.get()
        stock=stock_entry.get()
        price=price_entry.get()
        IMS.update_Product(name, stock, price, id)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success','Item updates successfully')

def insert():
    id=id_entry.get()
    name=name_entry.get()
    stock=stock_entry.get()
    price=price_entry.get()
    if not (id and name and stock and price):
        messagebox.showerror('Error','Enter all fields.')
    elif IMS.id_exists(id):
        messagebox.showerror('Error','ID already exists')
    else:
        try:
            stock_val=int(stock)
            price_val=float(price)
            IMS.insert_Product(id,name,stock_val,price_val)
            add_to_treeview()
            clear()
          
            messagebox.showinfo('Success','Data has been inserted')
        except ValueError:
            messagebox.showerror('Error','stock or price should be an integer')



title_lable=ctk.CTkLabel(app,font=font1,text='Ronin Product Details',text_color='white',bg_color='#0A0B0C')
title_lable.place(x=365/2,y=10, anchor='n')

frame=ctk.CTkFrame(app,bg_color='#0A0B0C',fg_color='#1B1B21', corner_radius=10,border_color='#fff', width=315,height=300)
frame.place(x=25,y=45)

id_label=ctk.CTkLabel(frame, font=font2, text='Product ID:',text_color='white')
id_label.place(x=10,y=50)
id_entry=ctk.CTkEntry(frame,font=font2, text_color='#000',fg_color='#fff',border_color='#B2016C',border_width=1,width=100)
id_entry.place(x=200,y=48)

name_label=ctk.CTkLabel(frame, font=font2, text='Product Name:',text_color='white')
name_label.place(x=10,y=100)
name_entry=ctk.CTkEntry(frame,font=font2, text_color='#000',fg_color='#fff',border_color='#B2016C',border_width=1,width=100)
name_entry.place(x=200,y=98)

stock_label=ctk.CTkLabel(frame, font=font2, text='Product stock:',text_color='white')
stock_label.place(x=10,y=150)
stock_entry=ctk.CTkEntry(frame,font=font2, text_color='#000',fg_color='#fff',border_color='#B2016C',border_width=1,width=100)
stock_entry.place(x=200,y=148)

price_label=ctk.CTkLabel(frame, font=font2, text='Product price:',text_color='white')
price_label.place(x=10,y=200)
price_entry=ctk.CTkEntry(frame,font=font2, text_color='#000',fg_color='#fff',border_color='#B2016C',border_width=1,width=100)
price_entry.place(x=200,y=198)

add_button=ctk.CTkButton(frame, command=insert, font=font2,text_color='white',text='Add',fg_color='red', hover_color='green3', bg_color='#1B1B21', cursor='hand2', corner_radius=8, width=80)
add_button.place(x=10,y=248)

delete_button=ctk.CTkButton(frame, command=deleted, font=font2,text_color='white',text='Delete',fg_color='red', hover_color='green3', bg_color='#1B1B21', cursor='hand2', corner_radius=8, width=80)
delete_button.place(x=220,y=248)

update_button=ctk.CTkButton(frame, command=update,font=font2,text_color='white',text='Update',fg_color='red', hover_color='green3', bg_color='#1B1B21', cursor='hand2', corner_radius=8, width=80)
update_button.place(x=115,y=248)

style=ttk.Style(app)

style.theme_use("clam")
style.configure('Treeview',font=font3, foreground='#fff',background='0A0B0C', fieldbackground='#1B1B21',borderwidth=0)
style.map('Treeview',background=[('selected','#AA04A7')])

tree = ttk.Treeview(app,height = 20)
tree['columns']=('id','Name','stock','Price')
tree.column('#0', width=0, stretch =tk.NO)
tree.column('id', anchor=tk.CENTER, width=150)
tree.column('Name', anchor=tk.CENTER, width=150)
tree.column('stock', anchor=tk.CENTER, width=150)
tree.column('Price', anchor=tk.CENTER, width=150)
tree.heading('id', text='ID')
tree.heading('Name',text='Name')
tree.heading('stock',text='Stock')
tree.heading('Price',text='Price')
tree.place(x=550,y=70)

tree.bind('<ButtonRelease>',display_data)

add_to_treeview()
app.mainloop()

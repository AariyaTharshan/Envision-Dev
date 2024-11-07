from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Enivision 6.0")
root.geometry("1440x1200")

menubar = Menu(root)

file = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file)

settings = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Settings",menu=settings)

images = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Images",menu=images)

process = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Process",menu=process)

measurements = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Measurements",menu=measurements)

help = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=help)

root.config(menu = menubar)

ft = Frame(root,relief="ridge",bd=2,bg="#696969",height=45)
ft.propagate(False)
fm = Frame(root,relief="ridge",bd=2,height=500)
fm.propagate(False)
fb1 = Frame(root,relief="ridge",bd=2)
fb1.propagate(False)
fb2 = Frame(root,relief="ridge",bd=2)
fb2.propagate(False)

#Top frame
stp_button = Button(ft,text="",relief="flat").place(x=10,y=5,width=30,height=30)
null_button = Button(ft,text="",relief="flat").place(x=50,y=5,width=30,height=30)
search_button = Button(ft,text="",relief="flat").place(x=90,y=5,width=30,height=30)
clk_button = Button(ft,text="",relief="flat").place(x=130,y=5,width=30,height=30)
set_button = Button(ft,text="",relief="flat").place(x=170,y=5,width=30,height=30)
lable_x = Label(ft,text="X: 0",font=("Helventica",10,"bold"),background="#696969").place(x=350,y=12)
lable_y = Label(ft,text="Y: 0",font=("Helventica",10,"bold"),background="#696969").place(x=450,y=12)
grey_value = Label(ft,text="Gray Value: ",font=("Helventica",10,"bold"),background="#696969").place(x=550,y=12)
grey_value_input = Entry(ft,textvariable="",relief="solid",font=("Helventica",11)).place(x=645,y=10,width=25,height=25)
mode_lable = Label(ft,text="Mode:",font=("Helventica",10,"bold"),background="#696969").place(x=675,y=12)

#Bottom Left Frame
lable_start = Label(fb1,text="Start Here",font=("Helventica",18,"bold"),foreground="red").place(x=10,y=10)
play_btn = Button(fb1,text="Play",relief="solid").place(x=275,y=10,width=55,height=55)
snap_btn = Button(fb1,text="Snap",relief="solid").place(x=350,y=10,width=55,height=55)
rec_btn  = Button(fb1,text="Master",relief="solid").place(x=425,y=10,width=55,height=55)


lable_mag = Label(fb1,text="Mag X : ",font=("Helventica",10,"bold"))
lable_mag.place(x=25,y=50)
mag_option = [1,1000]
dd_mag = ttk.Combobox(fb1,state="readonly",values=mag_option)
dd_mag.place(x=100,y=50)

location = StringVar(value="C:\\Users\\ADMIN\\Desktop")
lable_location = Label(fb1,text="Location : ",font=("Helventica",10,"bold"))
lable_location.place(x=25,y=85)
loc_entry = Entry(fb1,textvariable=location,relief="solid",font=("Helventica",11)).place(x=100,y=85,width=350,height=20)
open_button = Button(fb1,text="Open",relief="groove").place(x=470,y=75)

lable_from = Label(fb1,text="From",font=("Helventica",10))
lable_from.place(x=25,y=115)
from_option = ["28-10-2024"]
dd_from = ttk.Combobox(fb1,state="readonly",values=from_option)
dd_from.place(x=100,y=115)

lable_to = Label(fb1,text="To",font=("Helventica",10))
lable_to.place(x=270,y=115)
to_option = ["28-10-2024"]
dd_to = ttk.Combobox(fb1,state="readonly",values=to_option)
dd_to.place(x=307,y=115)

rf_button = Button(fb1,text="Refresh",relief="groove")
rf_button.place(x=470,y=110)

ft.pack(fill='x',pady=5)
fm.pack(fill='x',padx=10)
fb1.place(x=10, y=560, width=535, height=150)
fb2.place(x=560, y=560, width=795, height=150)

root.mainloop()
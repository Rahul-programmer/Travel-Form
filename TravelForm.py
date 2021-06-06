from tkinter import *
root= Tk()
root.geometry('800x300')
root.title("Travel Form")
def getvalue():
    with open("record.txt","a") as f:
        f.write(f"{name_value.get(),Age_value.get(),Gender_value.get(),Phone_value.get(),Payment_value.get(),Place_value.get()}")

Name = Label(root,text="Name",fg="Red").grid(row=0,column=3,padx=5,pady=8)
Age =Label(root,text="Age",fg="Red").grid(row=1,column=3,padx=5,pady=8)
Gender=Label(root,text="Gender",fg="Red").grid(row=2,column=3,padx=5,pady=8)
Phone=Label(root,text="Phone number",fg="Red").grid(row=3,column=3,padx=5,pady=8)
Payment_mode=Label(root,text="Modeofpayment",fg="Red").grid(row=4,column=3,padx=5,pady=8)
Place=Label(root,text="Place to visit",fg="RED").grid(row=5,column=3,padx=5,pady=8)

name_value=StringVar()
Age_value=StringVar()
Phone_value=StringVar()
Payment_value=StringVar()
Gender_value=StringVar()
Place_value=StringVar()

food_service_value=IntVar()


name_entry=Entry(root,textvariable=name_value ).grid(row=0,column=4)
Age_entry=Entry(root,textvariable=Age_value ).grid(row=1,column=4)
Gender_entry=Entry(root,textvariable=Gender_value ).grid(row=2,column=4)
Phone_entry=Entry(root,textvariable=Phone_value ).grid(row=3,column=4)
Payment_entry=Entry(root,textvariable=Payment_value ).grid(row=4,column=4)
Place_entry=Entry(root,textvariable=Place_value ).grid(row=5,column=4)

food_service=Checkbutton(root,text="Do you want your food").grid(row=6,column=3)

Submit_Button=Button(root,text="SubmitButton",padx=5,pady=8,command=getvalue).grid(row=8,column=3)



root.mainloop()
from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("400x220")
root.title("Interest Calculator")

def cal():
    try:
        x = combo.get()
        principal = int(p_entry.get())
        rate = int(r_entry.get())
        time = int(t_entry.get())
        if x == "Simple Interest":
            calculation = (principal*rate*time)/100
            result_lbl['text'] = f"Simple Interest is: {calculation} Rs."
        elif x == "Compound Interest":
            calculation = int((principal*(1+(rate)/100)**time))
            result_lbl['text'] = f"Compound Interest is: {calculation} Rs."

    except:
        result_lbl['text'] = "Please fill the Entries."

frame = Frame(root,borderwidth=5,bg="orange")
frame.pack(fill=X)

p_lbl = Label(frame,text="Principal",bg="orange",font=("Helvetica",10,"bold"))
p_lbl.grid(row=0,column=0)

p_entry = Entry(frame,font=("Helvetica",10,"bold"))
p_entry.grid(row=0,column=1,pady=10)


r_lbl = Label(frame,text="Rate",bg="orange",font=("Helvetica",10,"bold"))
r_lbl.grid(row=1,column=0,pady=10)

r_entry = Entry(frame,font=("Helvetica",10,"bold"))
r_entry.grid(row=1,column=1,pady=10)

t_lbl = Label(frame,text="Time",bg="orange",font=("Helvetica",10,"bold"))
t_lbl.grid(row=2,column=0,pady=10)

t_entry = Entry(frame,font=("Helvetica",10,"bold"))
t_entry.grid(row=2,column=1,pady=10)

combo_lbl = Label(frame,text="Select One",bg="orange",font=("Helvetica",10,"bold"))
combo_lbl.grid(row=3,column=0)
combo = ttk.Combobox(frame,values=["Simple Interest","Compound Interest"],font=("Helvetica",10,"bold"))
combo.set("Select")
combo.grid(row=3,column=1,pady=10)

result_lbl = Label(frame,bg="orange",font=("Helvetica",10,"bold"))
result_lbl.grid(row=4,column=1)
btn = Button(frame, text="Calculate",font=("Helvetica",10,"bold"),bg="orange",command=cal)
btn.grid(row=5,column=0)

root.mainloop()
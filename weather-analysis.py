import tkinter
import tkinter.messagebox
from tkinter import ttk
import json
import datetime


class Object:
    def __init__(self,class_name,Row,Column,columnspan=1,rowspan=1,padx=0,pady=0):
        self.wrapped_class=class_name
        self.wrapped_class.grid(row=Row,column=Column,columnspan=columnspan,rowspan=rowspan,padx=padx,pady=pady)

    def __getattr__(self,name):
        return getattr(self.wrapped_class,name)

class NewWindow(tkinter.Toplevel):
    def __init__(self,title="NewWindow",master=None):
        super().__init__(master=master)
        self.title=title

class MyEntry(tkinter.Entry):
    def __init__(self,master=None,state="normal",textvariable=""):
        super().__init__(master=master)
        self.config(textvariable=textvariable,state=state)
    
    def check(self):
        try:
            float(self.get())
            return True
        except:
            tkinter.messagebox.showinfo("Error","Invalid format")
            return False

class DateEntry(tkinter.Entry):
    def __init__(self,master=None,textvariable=""):
        super().__init__(master=master)
        self.config(textvariable=textvariable,state="normal")

    def check(self):
        try:
            datetime.datetime.strptime(self.get(), "%Y-%m-%d")
            return True
        except:
            tkinter.messagebox.showinfo("Error","Invalid format")
            return False



def add():
    add=NewWindow("Add",window)
    add.geometry("200x200")
    add.resizable(False,False)
    date_label_add=Object(tkinter.Label(add,text="date:"),0,0)
    date_entry_add=Object(DateEntry(add),0,1)
    tmin_label_add=Object(tkinter.Label(add,text="tmin:"),1,0)
    tmin_entry_add=Object(MyEntry(add),1,1)
    tmax_label_add=Object(tkinter.Label(add,text="tmax:"),2,0)
    tmax_entry_add=Object(MyEntry(add),2,1)
    prcp_label_add=Object(tkinter.Label(add,text="prcp:"),3,0)
    prcp_entry_add=Object(MyEntry(add),3,1)
    snow_label_add=Object(tkinter.Label(add,text="snow:"),4,0)
    snow_entry_add=Object(MyEntry(add),4,1)
    snwd_label_add=Object(tkinter.Label(add,text="snwd:"),5,0)
    snwd_entry_add=Object(MyEntry(add),5,1)
    awnd_label_add=Object(tkinter.Label(add,text="awnd:"),6,0)
    awnd_entry_add=Object(MyEntry(add),6,1)
    add_entrys=[date_entry_add,tmin_entry_add,tmax_entry_add,prcp_entry_add,snow_entry_add,snwd_entry_add,awnd_entry_add]
    button_check=Object(tkinter.Button(add,text="Add",command=lambda:check_add(add_entrys)),7,1)
    

def check_add(entrys):
    global length
    global datas
    global set_data
    for entry in entrys:
        if not entry.check():
            return
    datas.append({"date":entrys[0].get(),"tmin":entrys[1].get(),"tmax":entrys[2].get(),"prcp":entrys[3].get(),"snow":entrys[4].get(),"snwd":entrys[5].get(),"awnd":entrys[6].get()})
    length+=1
    set_data.add(datas[-1]["date"])
    datas=sorted(datas,key=lambda datas:datas["date"])
    # main_entrys=[date_entry,tmin_entry,tmax_entry,prcp_entry,snow_entry,snwd_entry,awnd_entry]
    # zip_entrys=zip(entrys,main_entrys)
    # for entry,main_entry in zip_entrys:
    #     if entry.check():
    #         #TO_DO


    #         # main_entry.config(textvariable=tkinter.StringVar(value=entry.get()))
            

def check_edit():
    global datas
    if not radio_var.get():
        for entry in entrys:
            if not entry.check():
                values=[datas[index][property] for property in ["date","tmin","tmax","prcp","snow","snwd","awnd"]]
                entry.config(textvariable=tkinter.StringVar(value=values[entrys.index(entry)]))
        for entry,property in zip(entrys,["date","tmin","tmax","prcp","snow","snwd","awnd"]):
            datas[index][property]=entry.get()
        values=[datas[index][property] for property in ["date","tmin","tmax","prcp","snow","snwd","awnd"]]
        

def left():
    global length
    global index
    if index<=0:
        index=length-1
    else:
        index-=1
    date_entry.config(textvariable=tkinter.StringVar(value=datas[index]["date"]))
    tmin_entry.config(textvariable=tkinter.StringVar(value=datas[index]["tmin"]))
    tmax_entry.config(textvariable=tkinter.StringVar(value=datas[index]["tmax"]))
    prcp_entry.config(textvariable=tkinter.StringVar(value=datas[index]["prcp"]))
    snow_entry.config(textvariable=tkinter.StringVar(value=datas[index]["snow"]))
    snwd_entry.config(textvariable=tkinter.StringVar(value=datas[index]["snwd"]))
    awnd_entry.config(textvariable=tkinter.StringVar(value=datas[index]["awnd"]))
    values=[datas[index][property] for property in ["date","tmin","tmax","prcp","snow","snwd","awnd"]]

def right():
    global length
    global index
    if index>=length-1:
        index=0
    else:
        index+=1
    date_entry.config(textvariable=tkinter.StringVar(value=datas[index]["date"]))
    tmin_entry.config(textvariable=tkinter.StringVar(value=datas[index]["tmin"]))
    tmax_entry.config(textvariable=tkinter.StringVar(value=datas[index]["tmax"]))
    prcp_entry.config(textvariable=tkinter.StringVar(value=datas[index]["prcp"]))
    snow_entry.config(textvariable=tkinter.StringVar(value=datas[index]["snow"]))
    snwd_entry.config(textvariable=tkinter.StringVar(value=datas[index]["snwd"]))
    awnd_entry.config(textvariable=tkinter.StringVar(value=datas[index]["awnd"]))
    values=[datas[index][property] for property in ["date","tmin","tmax","prcp","snow","snwd","awnd"]]

def search(dates):
    global values
    if radio_var.get():
        try:
            global datas
            date=dates.get()
            for i,data in enumerate(datas):
                if data["date"]==date:
                    index=i
                    break
            date_entry.config(textvariable=tkinter.StringVar(value=datas[index]["date"]))
            tmin_entry.config(textvariable=tkinter.StringVar(value=datas[index]["tmin"]))
            tmax_entry.config(textvariable=tkinter.StringVar(value=datas[index]["tmax"]))
            prcp_entry.config(textvariable=tkinter.StringVar(value=datas[index]["prcp"]))
            snow_entry.config(textvariable=tkinter.StringVar(value=datas[index]["snow"]))
            snwd_entry.config(textvariable=tkinter.StringVar(value=datas[index]["snwd"]))
            awnd_entry.config(textvariable=tkinter.StringVar(value=datas[index]["awnd"]))
            values=[datas[index][property] for property in ["date","tmin","tmax","prcp","snow","snwd","awnd"]]
        except UnboundLocalError:
            tkinter.messagebox.showinfo("Error","There is no this date or it was inputted wrongly")
            date_entry.config(textvariable=tkinter.StringVar(value=values[0]))
            tmin_entry.config(textvariable=tkinter.StringVar(value=values[1]))
            tmax_entry.config(textvariable=tkinter.StringVar(value=values[2]))
            prcp_entry.config(textvariable=tkinter.StringVar(value=values[3]))
            snow_entry.config(textvariable=tkinter.StringVar(value=values[4]))
            snwd_entry.config(textvariable=tkinter.StringVar(value=values[5]))
            awnd_entry.config(textvariable=tkinter.StringVar(value=values[6]))
    

def radio(*args):
    if radio_var.get():
        date_entry.bind("<Return>",lambda event:search(date_entry))
        for entry in set(entrys)-{date_entry}:
            entry.config(state="readonly")
        button_search.config(state="normal")
    else:
        for entry in entrys:
            entry.config(state="normal")
            entry.bind("<Return>",lambda event:check_edit())
        button_search.config(state="disabled")


def display(canvas,new_datas,selecteds,checkbuttons):
    canvas.delete("all")
    x_0=30
    y_0=160
    x_length=276
    y_length=156
    canvas.create_line(x_0,y_0,x_0+x_length+24,160, arrow=tkinter.LAST)
    canvas.create_line(x_0,y_0,30,y_0-y_length+24, arrow=tkinter.LAST)
    x_s=[]
    
    for i in range(1,13):
        x=x_0+i*(x_length//12)
        x_s.append(x)
        canvas.create_line(x,y_0-5,x,y_0+5)
        canvas.create_text(x,y_0+9,text=i)
    for year in new_datas.keys():
        for i in range(len(checkbuttons)):
            if year==checkbuttons[i]["text"] and selecteds[i].get():
                y_s=[]
                for month in new_datas[year].keys():
                    y_s.append(y_0-new_datas[year][month])
                coord=list(zip(x_s,y_s))
                for i in range(len(coord)-1):
                    canvas.create_line(coord[i][0],coord[i][1],coord[i+1][0],coord[i+1][1])

def statistics():
    global datas
    new_datas={}
    for data in datas:
        year=data["date"].split("-")[0]
        month=data["date"].split("-")[1]
        if year not in new_datas:
            new_datas[year]={}
        if month not in new_datas[year]:
            new_datas[year][month]=[float(data["tmin"]),1]
        else:
            new_datas[year][month][0]+=float(data["tmin"])
            new_datas[year][month][1]+=1
    for year in new_datas.keys():
        for month in new_datas[year].keys():
            new_datas[year][month]=int(round(new_datas[year][month][0]/new_datas[year][month][1]))

    tk=NewWindow()
    
    tk.geometry("500x200")
    tk.resizable(True,True)
    
    
    
    canvas=tkinter.Canvas(tk,width=400,height=300)
    canvas.place(x=20,y=10)
    x_0=30
    y_0=160
    x_length=276
    y_length=156
    canvas.create_line(x_0,y_0,x_0+x_length+24,160, arrow=tkinter.LAST)
    canvas.create_line(x_0,y_0,30,y_0-y_length+24, arrow=tkinter.LAST)
    x_s=[]
    
    for i in range(1,13):
        x=x_0+i*(x_length//12)
        x_s.append(x)
        canvas.create_line(x,y_0-5,x,y_0+5)
        canvas.create_text(x,y_0+9,text=i)
    checkbuttons=[]
    selecteds=[]
    for year in new_datas.keys():
        selecteds.append(tkinter.IntVar())
        checkbuttons.append(tkinter.Checkbutton(tk,text=year,variable=selecteds[-1],command=lambda:display(canvas,new_datas,selecteds,checkbuttons)))
    y=10
    for checkbutton in checkbuttons:
        checkbutton.place(x=400,y=y)
        y+=30
    
def help():
    info=NewWindow()
    info.geometry("650x200")
    # info.resizable(False,False)
    info_text=tkinter.Text(info,width=75)
    info_text.place(x=10,y=10)
    info_text.insert("1.0","There is a search mode that allows you to find data by a specific date.\n"
    "To do this, enter the date in the format YYYY-MM-DD."
    "\nThen press Enter."
    "\nThere is an edit mode that allows you to edit data."
    "\nTo do this, you need to rewrite some information and press Enter."
    "\nThe Search button allows you to find data by date from the drop-down list."
    "\nThe Add button allows you to add data."
    "\nThe Statistics button allows you to look at the graph of minimum temperatures (on average) by month of each year."
    "\nThe < > buttons allow you to change the date")

datas=json.load(open("rdu-weather-history.json"))
set_data=set()
for data in datas:
    set_data.add(data['date'])
length=len(set_data)
index=0
window=tkinter.Tk()
window.geometry("700x300")
window.resizable(False,False)
window.title("Weather Report")
date_label=Object(tkinter.Label(window,text="date:"),0,0)
date_entry=Object(DateEntry(window,textvariable=tkinter.StringVar(value=datas[index]["date"])),0,1,columnspan=2)
tmin_label=Object(tkinter.Label(window,text="tmin:"),1,0)
tmin_entry=Object(MyEntry(window,state="readonly",textvariable=tkinter.StringVar(value=datas[index]["tmin"])),1,1,columnspan=2)
tmax_label=Object(tkinter.Label(window,text="tmax:"),2,0)
tmax_entry=Object(MyEntry(window,state="readonly",textvariable=tkinter.StringVar(value=datas[index]["tmax"])),2,1,columnspan=2)
prcp_label=Object(tkinter.Label(window,text="prcp:"),3,0)
prcp_entry=Object(MyEntry(window,state="readonly",textvariable=tkinter.StringVar(value=datas[index]["prcp"])),3,1,columnspan=2)
snow_label=Object(tkinter.Label(window,text="snow:"),4,0)
snow_entry=Object(MyEntry(window,state="readonly",textvariable=tkinter.StringVar(value=datas[index]["snow"])),4,1,columnspan=2)
snwd_label=Object(tkinter.Label(window,text="snwd:"),5,0)
snwd_entry=Object(MyEntry(window,state="readonly",textvariable=tkinter.StringVar(value=datas[index]["snwd"])),5,1,columnspan=2)
awnd_label=Object(tkinter.Label(window,text="awnd:"),6,0)
awnd_entry=Object(MyEntry(window,state="readonly",textvariable=tkinter.StringVar(value=datas[index]["awnd"])),6,1,columnspan=2)
button_left=Object(tkinter.Button(window,text="<",command=left),7,0)
dates=Object(ttk.Combobox(window,width=10,values=list(sorted(set_data))),7,1)
button_search=Object(tkinter.Button(window,text="Пошук",command=lambda:search(dates)),7,2)
button_right=Object(tkinter.Button(window,text=">",command=right),7,3,padx=5)
button_add=Object(tkinter.Button(window,width=10,text="Додати",command=add),8,1,columnspan=2,pady=5)

entrys=[date_entry,tmin_entry,tmax_entry,prcp_entry,snow_entry,snwd_entry,awnd_entry]
values=[datas[index][property] for property in ["date","tmin","tmax","prcp","snow","snwd","awnd"]]


radio_var=tkinter.BooleanVar()
radio_var.trace_add("write",radio)
radio_var.set(True)
radio_search=Object(tkinter.Radiobutton(window,text="Search",variable=radio_var,value=True),0,4)
radio_edit=Object(tkinter.Radiobutton(window,text="Edit",variable=radio_var,value=False),1,4)
button_statistic=Object(tkinter.Button(window,width=10,text="Statistics",command=statistics),9,1,columnspan=2,pady=5)

help_label=Object(tkinter.Label(window,text="To discover more, press the button"),0,6)
help_button=Object(tkinter.Button(window,text="Hint",command=help),1,6)

window.mainloop()
with open("rdu-weather-history.json","w") as f:
    json.dump(datas,f)

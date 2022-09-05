#import module
from ipaddress import ip_address
from tkinter import*

host_path='C:\Windows\System32\drivers\etc'
ip_address='127.0.0.1'

def Block():
    website_lists=enter_Website.get(1.0,END)
    Website=list(website_lists.split(","))
    with open (host_path,'r+')as host_file:
        file_content=host_file.read()
        for web in Website:
            if web in file_content:
                display=Label(window,text='Already Blocked',font='arial')
                display.place(x=200,y=200)
        else:
            host_file.write(ip_address+" "+web+'\n')
            Label(window,text="Blocked",font='arial').place(x=230,y=200)

def unblock():
    website_lists=enter_Website.get(1.0,END)
    Website=list(website_lists.split(","))
    with open(host_path,'r+') as host_file:
        file_content=host_file.readlines()
        for web in Website:
            if web in website_lists:
                with open(host_path,'r+') as f:
                    for line in file_content:
                        if line.strip(',')!=website_lists:
                            f.write(line)
                            Label(window,text="UnBlocked",font='arial').place(x=350,y=200)
        else:
            display=Label(window,text='Already UnBlocked',font='arial')
            display.place(x=350,y=200)
def exit():
    window.destroy ()

from numpy import block

#to make a window
window = Tk() #window is project of Tk () class

#set window Title
window.title ("Suvasish")
window.geometry("650x400")
window.maxsize (650,400)
window.minsize (650,400)
#set Header
l1=Label (window,text = "WEBSITE BLOCKER",font="arial 12 bold")
l1.pack ()
l2=Label (window,text = "Developed @ByJithon,2022",font= "arial 18 bold")
l2.pack(side = BOTTOM)

l3=Label (window ,text="Enter WebSite",font="arial 10")
l3.place(x=8,y=60)
enter_Website=Text (window,width='50',height='2')
enter_Website.place(x=120,y=60)

b1=Button (window,text="Block",font="arial 12 bold",bg="green",fg="red",command=Block)
b1.place(x=200,y=100)
b2=Button (window,text="UnBlock",font="arial 12 bold",bg="green",fg="red",command=unblock)
b2.place(x=250,y=100)
b3=Button (window,text="Exit",font="arial 12 bold",bg="red",fg="black",command=exit)
b3.place(x=340,y=100)

window.mainloop ()
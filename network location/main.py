#by petrucciii

#import all modules
try:
    import tkinter as tk 
except:
    import Tkinter as tk
import json
from urllib.request import urlopen


#window setting
root = tk.Tk()
root.configure(bg="black")
root.title("Network Location")
root.geometry("300x200")
root.resizable(False, False)
try:
    root.iconbitmap("images/nl.ico")
except:
    pass #fix


try:
    
    #shearching the network location
    url = "http://ipinfo.io/json"
    response = urlopen(url)
    data = json.load(response)

    #network location
    ip = ["IP-Addres:", data["ip"]]
    server = ["Server:", data["org"]]
    city = ["City:", data["city"]]
    country = ["Country:", data["country"]]
    region = ["Region:" ,data["region"]]

    #title
    title = tk.Label(root, text="Your Network Location", bg="white", fg="red", font=("",15)).place(x=10, y=0)
    credit = tk.Label(root, text="by petrucciii", bg="black", fg="grey", font=("", 9)).place(x=10, y=29)

    #printing network location
    iptk = tk.Label(root, text=ip, bg="black", fg="white").place(x=10, y=50)
    servertk = tk.Label(root, text=server, bg="black", fg="white").place(x=10, y=70)
    citytk = tk.Label(root, text=city, bg="black", fg="white").place(x=10, y=90)
    countrytk = tk.Label(root, text=country, bg="black", fg="white").place(x=10, y=110)
    regiontk = tk.Label(root, text=region, bg="black", fg="white").place(x=10, y=130)

#connection error
except:

    error = tk.Label(root, text="NO INTERNET CONNECTION", bg="black", fg="red", font=("Times", 16, "bold")).pack()
    connect = tk.Label(root, text="Please, connect your device", bg="black", fg="red", font=("Times", 10, "bold")).pack()


if __name__ == "__main__":
    root.mainloop()

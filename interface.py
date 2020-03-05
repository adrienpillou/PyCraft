from tkinter import *
from serverwrapper import Server

# Updating the player list
def UpdatePlayerListbox():
    playerListBox.delete(0,END)
    for item in server.GetPlayerList():
        playerListBox.insert(END, item)

# Updating app interface
def UpdateInterface():
    available = server.TestIfServerIsAvailable()
    if available:
        UpdatePlayerListbox()
        slotsLabel['text'] = "Slots : {0}".format(server.GetSlotsInfos())
        pingLabel['text'] = "Ping : {0}ms".format(str(server.GetLatency()))
            
    elif not available:
        playerListBox.delete(0,END)
        slotsLabel['text'] = "Slots : -/-"
        pingLabel['text'] = "Ping : -ms"
    
    root.after(refreshRate, UpdateInterface)
    
def EstablishConnection(server):
    print("Establishing connection to the server on {0}:{1}...".format(server.ip,server.port))
    server = Server(server.ip,server.port)
    server.TestIfServerIsAvailable()
    if(server.isOnline):
        print("This server is online.")
    else:
        print("This server is currently offline.")
    UpdateInterface()

root = Tk()
root.title("PyCraft")
root.iconbitmap("./terminal_bloc.ico")
root.resizable(width=False,height=False)
root.geometry("300x400+760+390")
frame = Frame(root)
frame.pack()
refreshRate = 1000 #(ms)


server = Server("127.0.0.1", "25565") # Default connexion settings

# Creating widgets elements
ipAddressLabel = Label(frame, text="Server address : ", font="Helvetica 10 bold")
portLabel = Label(frame,text="Server port : ", font="Helvetica 10 bold")
ipAddressField = Entry(frame)
ipAddressField.insert(0, "127.0.0.1")
portAddressField = Entry(frame)
portAddressField.insert(0,"25565")
slotsLabel = Label(frame , text ="Slots : -/-", font="Helvetica 10 bold")
pingLabel = Label(frame, text = "Ping : -ms", font="Helvetica 10 bold")
submitButton = Button(frame, text="Query", command = lambda:EstablishConnection(server))
playerListLabel = Label(frame, text="Connected Players :", font="Helvetica 10 bold")
playerListBox = Listbox(frame)

# Positionning elements on a grid
ipAddressLabel.pack()
ipAddressField.pack()
portLabel.pack()
portAddressField.pack()
submitButton.pack()
slotsLabel.pack()
pingLabel.pack()
playerListLabel.pack()
playerListBox.pack(side="left",fill="y")

listBoxScrollBar = Scrollbar(frame, orient="vertical")
listBoxScrollBar.config(command=playerListBox.yview)
listBoxScrollBar.pack(side="right", fill="y")
playerListBox.config(yscrollcommand=listBoxScrollBar.set)

#server = serverwrapper.Server("93.25.248.66", "25565")
UpdateInterface()
root.mainloop()

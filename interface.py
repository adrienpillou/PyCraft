from tkinter import *
import serverwrapper

root = Tk()
root.title("PyCraft")
root.iconbitmap("./assets/terminal_bloc.ico")
root.resizable(width=False,height=False)
root.geometry("300x400+760+390")
frame = Frame(root)
refreshRate = 1000 #(ms)

def UpdatePlayerListbox():
    playerListBox.delete(0,END)
    for item in server.GetPlayerList():
        playerListBox.insert(END, item)

def UpdateInterface():
    if server.isOnline :
        UpdatePlayerListbox()
        slotsLabel['text'] = "Slots : {0}".format(server.GetSlotsInfos())
        pingLabel['text'] = "Ping : {0}ms".format(str(server.GetLatency()))
    elif not server.isOnline:
        playerListBox.delete(0,END)
        slotsLabel['text'] = "Slots : -/-"
        pingLabel['text'] = "Ping : -ms"

    server.TestIfServerIsAvailable()
    root.after(refreshRate, UpdateInterface)

def EstablishConnection(ip, port):
    print("Establishing connection to the server on {0}:{1}...".format(ip,port))
    myServer = serverwrapper.Server(ip,port)
    myServer.TestIfServerIsAvailable()
    if(myServer.isOnline):
        print("This server is online.")
    else:
        print("This server is currently offline.")
    return myServer

# Creating widgets elements
ipAddressLabel = Label(frame, text="Server address : ")
portLabel = Label(frame,text="Server port : ")
ipAddressField = Entry(frame)
ipAddressField.insert(0, "127.0.0.1")
portAddressField = Entry(frame)
portAddressField.insert(0,"25565")
slotsLabel = Label(frame , text ="Slots : -/-")
pingLabel = Label(frame, text = "Ping : -ms")
submitButton = Button(frame, text="Query", command = lambda:EstablishConnection(ipAddressField.get(), portAddressField.get()))

playerListLabel = Label(frame, text="Connected Players :")
playerListBox = Listbox(frame)

# Positionning elements on a grid
ipAddressLabel.grid(row = 0, column = 0)
ipAddressField.grid(row = 1, column = 0)
portLabel.grid(row = 2, column = 0)
portAddressField.grid(row = 3, column = 0)
submitButton.grid(row = 4,column = 0)
slotsLabel.grid(row = 5, column = 0)
pingLabel.grid(row = 6, column = 0)
playerListLabel.grid(row=7, column=0)
playerListBox.grid(row =8, column = 0)

frame.place(relx = .5, rely = .5, anchor = CENTER)

server = EstablishConnection(ipAddressField.get(), portAddressField.get())

UpdateInterface()
root.mainloop()

from socket import AF_INET, socket, SOCK_STREAM
from tkinter.font import Font
from threading import Thread
import tkinter
from tkinter import *
con_n=0
name=''
lst=['User']
dic_list={}
sender_list=[]
sender_string=''

root=Tk()
root.title("client")
root.resizable(0,0)
sizex = 800
sizey = 550
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
posx  = (ws/2) - (sizex/2)
posy  = (hs/2) - (sizey/2)
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
left_frame = Frame(root, bg='PaleVioletRed4', width=ws, height=50) #Creating sign up frame
right_frame = Frame(root, bg='Pink', width=ws, height=hs)#Creating Log in frame
left_frame.place(x=0,y=0)
right_frame.place(x=0,y=50)
###########################################
                                                       #generat_client_list
def sender_list_to_string():
    global sender_list
    global sender_string
    sender_string=''
    for i in sender_list:
        sender_string+=i+'@_*'
def click_check_box():
    global sender_list
    global myframe
    sender_list=[]
    for p in dic_list.keys():
        dic_list[p][1]=dic_list[p][0].get()
    for q in dic_list.keys():
        if dic_list[q][1]==1:
            sender_list.append(q)
        else:
            if q in sender_list:
                sender_list.remove(q)
    print(sender_list)
            
def generat_client_list_f_send():
    global sender_list
    #click_check_box()   
    if len(sender_list)==0:
        sender_list=lst[:]

#Function for load user
def load():
    global frame
    global canvas
    '''sizex = 800
    sizey = 600
    posx  = 100
    posy  = 100
    root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))'''
    global myframe
    myframe=Frame(right_frame,relief=GROOVE,width=50,height=100,bd=1)
    myframe.place(x=20,y=40)
    canvas=Canvas(myframe)
    frame=Frame(canvas)
    myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)

    myscrollbar.pack(side="right",fill="y")
    canvas.pack(side="left")
    canvas.create_window((0,0),window=frame,anchor='nw')
    frame.bind("<Configure>",myfunction)
    data() 

def data():#add user to the user with check box
    i=0
    global dic_list
    for a in lst:
        a1= IntVar()
        dic_list[a]=[a1,0]
        Checkbutton(frame, text=a, variable=a1,command=click_check_box).grid(row=i,column=0)
        i+=1

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=400)
load()
#############################################################
                                                                                #Validation User Input
#Function to check password and user name contains atleast 1 alphabet
def characters(password):
    s="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    f=0
    for i in range(len(password)):
        for j in range(len(s)):
            if password[i]==s[j]:
                f=1
                break
            if f==1:
                break
        if f==1:
            return(True)
        else:
            return(False)

def popup_window():
    global name
    global con
    if connect_button["text"] == "Logout":
        on_closing()
    else:
        from tkinter import messagebox
        top=Tk()
        def inp():
            global name
            global con_n
            name=text_1.get()
            if len(name)<6 or len(name)>13:
                messagebox.showinfo("info", "User name should be 6 to 13 characters")
                top.destroy()
            elif characters(name)==False:
                messagebox.showinfo("info","User name must contain a alphabet")
                top.destroy()
            else:
                ip_addr=text_2.get()
                temp_ip_lst=ip_addr.split(".")
                if len(temp_ip_lst)==4:
                    Connection_establish(text_2.get(),text_1.get())
                    set_name()
                    con_n=1
                    connect_button["text"] = "Logout"
                    top.destroy()
                else:
                    messagebox.showinfo("info","Enter valid ip address")
                    top.destroy()

        top.title("Input")
        top.resizable(0,0)
        top.configure(background='pink')
        top.wm_geometry("%dx%d+%d+%d" % (350, 120, 300, 50))
        label_1 = Label(top, text="Enter your Name",font=("Helvetica", 10),bg='pink')
        text_1 = Entry( top,font=("Helvetica", 12) )
        label_2 = Label(top, text="Enter Server Ip",font=("Helvetica", 10),bg='pink')
        text_2 = Entry( top ,font=("Helvetica", 12))
        label_1.place(x=20,y=20)
        text_1.place(x=130,y=20)
        label_2.place(x=20,y=50)
        text_2.place(x=130,y=50)
        connect_button_2 = tkinter.Button(top, text="Connect",fg = "White", bg='PaleVioletRed4',font = "Verdana 10 bold",command=inp)
        connect_button_2.place(x=170,y=80)
        
        tkinter.mainloop()
######################################################################################
'''def send(event=None):  # event is passed by binders.

    """Handles sending of messages."""
    global entry
    global msg_list
    #generat_client_list_f_send()
    msg = entry.get("1.0",END)
    msg+='@_*'+sender_list

    my_msg.set("")  # Clears input field.

    client_socket.send(bytes(msg, "utf8"))

    if msg == "{quit}":

        client_socket.close()

        top.quit()'''

        
    ####################################'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def send():
    global name
    global entry
    global msg_list
    global sender_string
    global sender_list
     #function
    msg = entry.get("1.0",END)
    msg=msg[:len(msg)-1]
    generat_client_list_f_send() #function
    sender_list_to_string()
    if msg=="*quit*":
        #print(sender_list)
        #print(name)
        #sender_list.remove(name) 
        #sender_list_to_string() #function
        #msg+=sender_string
        client_socket.send(bytes(msg, "utf8"))
        client_socket.close()
        root.quit()
        root.destroy()
    else:
        #msg_list.insert(tkinter.END, msg)
        msg+='@_*'+sender_string
        print(msg)
        entry.delete("1.0",END)
        client_socket.send(bytes(msg, "utf8"))
def del_user_frame():
    global myframe
    myframe.destroy()
def startt():#for recreate client list
    del_user_frame()
    load()
def receive():

    """Handles receiving of messages."""
    global BUFSIZ
    global client_socket
    while True:
        try:
            

            msg = client_socket.recv(BUFSIZ).decode("utf8")
            ####
            global lst
            global dic_list
            global dublicate_list
            list_for_quit_msg=msg.split("*quit*")
            if len(list_for_quit_msg)==3:
                msg=list_for_quit_msg[0]+list_for_quit_msg[1]
                lst.remove(list_for_quit_msg[0])
                del dic_list[list_for_quit_msg[0]]
                startt()
            lst_1=msg.split('@*')
            if len(lst_1)>=2:
                lst=lst_1[0:-1]
                dublicate_list=lst_1[0:-1]
                startt()
            
            else:
                msg_list.insert(tkinter.END, msg)
            


        except OSError:  # Possibly client has left the chat.

            break

                                                            #Connection_establish
def Connection_establish(HOST,name):
    
    global BUFSIZ
    global client_socket
    #----Now comes the sockets part----

    #HOST = input('Enter host: ')

    #PORT = input('Enter port: ')
    #name=input("Enter Your Name: ")

   # if not PORT:

        #PORT = 33000

    #else:

        #PORT = int(PORT)

    PORT=33300

    BUFSIZ = 1024

    ADDR = (HOST, PORT)
    client_socket = socket(AF_INET, SOCK_STREAM)
    try:
        client_socket.connect(ADDR)
    except:
        print ("Couldnt connect with the socket-server terminating program")
    ###1
    client_socket.send(bytes(name, "utf8"))

#######

    receive_thread = Thread(target=receive)

    receive_thread.start()

####################################################################################
def on_closing(event=None):
    #global client_socket
    global con
    """This function is to be called when the window is closed."""
    if con_n==1:
        entry.insert("1.0","*quit*")
        send()
    else:
        root.destroy() 

root.protocol("WM_DELETE_WINDOW", on_closing)    
    
                                                                            #for message seen box ####################
messages_frame =Frame(right_frame)

scrollbar = Scrollbar(messages_frame)  # To navigate through past messages.

# Following will contain the messages.

msg_list = Listbox(messages_frame, height=19, width=70, yscrollcommand=scrollbar.set)

scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)

msg_list.pack()

messages_frame.place(x=300,y=40)#pack()

#############################

entry = Text(right_frame, width=55, height=3, wrap=WORD)
myFont = Font(family="Verdana 10 bold", size=11)
entry.configure(font=myFont)
entry.place(x=300,y=380)

connect_button = tkinter.Button(left_frame, bg='pink', text="Connect", command=popup_window)

connect_button.place(x=680,y=10)

heading =Label(left_frame,bg = "PaleVioletRed4",fg = "White", text="Socket Chat Application",font = "Helvetica 16 bold italic")
heading.place(x=100,y=10)
def set_name():
    name_label =Label(left_frame,bg="PaleVioletRed4",fg = "White",font=("Helvetica", 10), text=name)
    name_label.place(x=570,y=10)

connected_people =Label(right_frame,bg="Pink",font=("Helvetica", 10) ,text="Connected People")
connected_people.place(x=40,y=18)
all_msg =Label(right_frame,bg="pink",font=("Helvetica", 10), text="All Messages")
all_msg.place(x=450,y=18)
typ_msg=Label(right_frame,bg="pink",font=("Helvetica", 10),text="Type your message:")
typ_msg.place(x=300,y=355)
send_button = tkinter.Button(right_frame,fg = "White", bg='PaleVioletRed4', text="Send",font = "Verdana 10 bold", command=send)

send_button.place(x=480,y=450)

from tkinter import *
import tkinter as tk
import webbrowser
from PIL import Image, ImageTk
import time
import tkinter.messagebox
import pyttsx3
import threading
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pyttsx3
from chatterbot.logic import LogicAdapter
from chatterbot.storage import SQLStorageAdapter
import wikipedia
import speech_recognition
import spacy
from forex_python.converter import CurrencyRates
import re
import requests
import pymongo

if __name__ == '__main__':

    text_speech = pyttsx3.init()
    text_speech.setProperty('rate', 110)   #Speaking timing
    text_speech.setProperty('volume', 5) 

def main():
    def open_link():
        for widgets in win1.winfo_children():
            widgets.destroy()
        def back():
            for widgets in win1.winfo_children():
                widgets.destroy()
            fr = Frame(win1, width=500, height=400, bg= '#137d85')
            fr.place(x=200)
            Label(fr, text="MR. ADROIT", font="aquire 58 bold", fg='white', bg='black', padx= 25, pady= 35).place(x=0, y=125)
            main()
        win1.configure(background='black')
        f1 = Frame(win1, width=535, height=430, bg='white')
        labl_0 = Label(f1, text="USER INFORMATION",width=20,font = 'calibri 24 bold',bg='white')  
        labl_0.place(x=95,y=53)  
        
        
        labl_1 = Label(f1, text="User ID",width=20,font='calibri 12',bg='white')  
        labl_1.place(x=80,y=130)  

        id = StringVar()
        name = StringVar()
        age = StringVar()  
        entry_1 = Entry(f1, textvariable=id, bg='black',fg='white',font= 'calibri 11 bold', border=0, insertbackground='white')  
        entry_1.place(x=240,y=133, width=160, height=20)  
        entry_1.insert(0, 'Enter your ID here...')  
        labl_2 = Label(f1, text="Name",width=20,font='calibri 12',bg='white')  
        labl_2.place(x=68,y=180)  
        
        entry_02 = Entry(f1, textvariable=name, bg='black',fg='white',font= 'calibri 11 bold', border=0, insertbackground='white')  
        entry_02.place(x=240,y=183, width=160, height=20)  
        entry_02.insert(0, 'Enter your name here...')  
        labl_3 = Label(f1, text="Gender",width=20,font='calibri 12',bg='white')  
        labl_3.place(x=70,y=230)  
        rad = StringVar()  
        rad.set("Radio")
        Radiobutton(f1, text="Male",padx = 5, variable=rad, value="Male", font='calibri 12',bg='white').place(x=230,y=230)  
        Radiobutton(f1, text="Female",padx = 20, variable=rad, value="Female", font='calibri 12',bg='white').place(x=290,y=230)  
        
        labl_4 = Label(f1, text="Age",width=20,font='calibri 12',bg='white')  
        labl_4.place(x=70,y=280)  
        
        
        entry_03 = Entry(f1, textvariable=age, bg='black',fg='white',font= 'calibri 11 bold', border=0, insertbackground='white')  
        entry_03.place(x=240,y=283, width=160, height=20)  
        entry_03.insert(0, 'Enter your age here...')
        
        def win3(doc):
            class ChatInterface(Frame):   #frame parentclass h

                def __init__(self, master=None):
                    Frame.__init__(self, master)
                    self.master = master

                    # sets default bg for top level windows
                    self.tl_bg = "black"
                    self.tl_bg2 = "black"
                    self.tl_fg = "#137d85"
                    self.font = "robotic 12"

                    menu = Menu(self.master)
                    self.master.config(menu=menu, bd=5)
                    self.master.config(bg="black")
                    
                    # Menu bar

                    # File
                    file = Menu(menu, tearoff=0, bg='black', fg='#137d85')
                    menu.add_cascade(label="File", menu=file)
                    file.add_command(label="Save Chat Log", command=self.save_chat)
                    file.add_command(label="Clear Chat", command=self.clear_chat)
                    #  file.add_separator()
                    file.add_command(label="Exit", command=self.chatexit)

                    # Options
                    options = Menu(menu, tearoff=0, bg='black', fg='#137d85')
                    menu.add_cascade(label="Options", menu=options)

                    # username

                    # font
                    font = Menu(options, tearoff=0, bg='black', fg='#137d85')
                    options.add_cascade(label="Font", menu=font)
                    font.add_command(label="Default", command=self.font_change_default)
                    font.add_command(label="Times", command=self.font_change_times)
                    font.add_command(label="System", command=self.font_change_system)
                    font.add_command(label="Helvetica", command=self.font_change_helvetica)
                    font.add_command(label="Fixedsys", command=self.font_change_fixedsys)

                    # color theme
                    color_theme = Menu(options, tearoff=0, bg='black', fg='#137d85')
                    options.add_cascade(label="Color Theme", menu=color_theme)
                    color_theme.add_command(label="Default", command=self.color_theme_default)
                    color_theme.add_command(label="Light", command=self.color_theme_light)
                    color_theme.add_command(label="Night",command=self.color_theme_dark)
                    color_theme.add_command(label="Green",command=self.color_theme_green)
                    color_theme.add_command(label="Grey", command=self.color_theme_grey)
                    color_theme.add_command(label="Blue", command=self.color_theme_dark_blue)

                    color_theme.add_command(label="Torque", command=self.color_theme_turquoise)
                    color_theme.add_command(label="Hacker", command=self.color_theme_hacker)
                    # color_theme.add_command(label='Mkbhd',command=self.MKBHD)

                    help_option = Menu(menu, tearoff=0, bg='black', fg='#137d85')
                    menu.add_cascade(label="Help", menu=help_option)
                    # help_option.add_command(label="Features", command=self.features_msg)
                    help_option.add_command(label="About PyBot", command=self.msg)
                    help_option.add_command(label="Develpoers", command=self.about)

                    self.text_frame = Frame(self.master, bd=6, bg='black')
                    self.text_frame.pack(expand=True, fill=BOTH)

                    # scrollbar for text box
                    self.text_box_scrollbar = Scrollbar(self.text_frame, bd=0, bg='black')
                    self.text_box_scrollbar.pack(fill=Y, side=RIGHT)

                    # contains messages
                    self.text_box = Text(self.text_frame, yscrollcommand=self.text_box_scrollbar.set, state=DISABLED,
                                        bd=1, padx=6, pady=6, spacing3=8, wrap=WORD, bg='black',fg='#137d85', font="Verdana 10", relief=GROOVE,
                                        width=10, height=1)
                    self.text_box.pack(expand=True, fill=BOTH)
                    self.text_box_scrollbar.config(command=self.text_box.yview)

                    # frame containing user entry field
                    self.entry_frame = Frame(self.master, bd=1, bg='black')
                    self.entry_frame.pack(side=LEFT, fill=BOTH, expand=True)

                    # entry field
                    self.entry_field = Entry(self.entry_frame, bd=1, justify=LEFT, bg='black', fg='#137d85', insertbackground='#137d85')
                    self.entry_field.pack(fill=X, padx=6, pady=6, ipady=3)
                    # self.users_message = self.entry_field.get()

                    # frame containing send button and emoji button
                    self.send_button_frame = Frame(self.master, bd=0, bg='black')
                    self.send_button_frame.pack(fill=BOTH)

                    # send button
                    self.send_button = Button(self.send_button_frame, text="Send", width=5, relief=GROOVE, bg='#137d85',fg='black',
                                            bd=1, command=lambda: self.send_message_insert(None), activebackground="black",
                                            activeforeground="#137d85")
                    self.send_button.pack(side=LEFT, ipady=8)
                    self.master.bind("<Return>", self.send_message_insert)

                    self.last_sent_label(date="No messages sent.")
                    # t2 = threading.Thread(target=self.send_message_insert(, name='t1')
                    # t2.start()

                def playResponce(self, responce):
                    x = pyttsx3.init()
                    # print(responce)
                    li = []
                    if len(responce) > 100:
                        if responce.find('--') == -1:
                            b = responce.split('--')
                            # print(b)
                    # voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                    # x.setProperty('voice', voice_id)
                    x.setProperty('rate', 120)
                    x.setProperty('volume', 100)
                    x.say(responce)
                    x.runAndWait()
                    # print("Played Successfully......")

                def last_sent_label(self, date):

                    try:
                        self.sent_label.destroy()
                    except AttributeError:
                        pass

                    self.sent_label = Label(self.entry_frame, font="Verdana 7", text=date, bg=self.tl_bg2, fg=self.tl_fg)
                    self.sent_label.pack(side=LEFT, fill=X, padx=3)

                def clear_chat(self):
                    self.text_box.config(state=NORMAL)
                    self.last_sent_label(date="No messages sent.")
                    self.text_box.delete(1.0, END)
                    self.text_box.delete(1.0, END)
                    self.text_box.config(state=DISABLED)

                def save_chat(self):
                                    ### check
                    client = pymongo.MongoClient("mongodb://localhost:27017/")
                    print(client)
                    db = client['MrAdroit']
                    collection = db['mrAdroitcollections']
                    collection.insert_one(doc)
                    self.text_box.config(state=NORMAL)
                    self.last_sent_label(date=" Your data is successfully saved!.")
                    self.text_box.delete(1.0, END)
                    self.text_box.delete(1.0, END)
                    # self.text_box.config(state=DISABLED)

                def chatexit(self):
                    exit()

                def msg(self):
                    tkinter.messagebox.showinfo("Mr Adroit ( The Smart Bot )",
                                                'Mr Adroit is a chatbot for answering python queries\nIt is based on retrival-based NLP using pythons NLTK tool-kit module\nGUI is based on Tkinter\nIt can answer questions regarding python language for new learners')

                def about(self):
                    tkinter.messagebox.showinfo("Mr Adroit Developers",
                                                "1.Haris\n2.Azlan\n3.Wajid\n4.Marium\n5.Waniya")
                    
                def send_message_insert(self, message):

                    user_input = self.entry_field.get().lower()
                    # request = user_input.casefold()
                    def foruser(user_input):
                        human = str(doc["name"])
                        pr1 = f"{human}: {user_input}\n"
                        self.text_box.configure(state=NORMAL)
                        self.text_box.insert(END, pr1)
                        self.text_box.configure(state=DISABLED)
                        self.text_box.see(END)
                        # time.sleep(0)
                        # t1 = threading.Thread(target=self.playResponce, args=(user_input,))
                        # t1.start()
                    def forbot(ob):
                        pr = "Mr Adroit : " + str(ob) + "\n"
                        self.text_box.configure(state=NORMAL)
                        self.text_box.insert(END, pr)
                        self.text_box.configure(state=DISABLED)
                        self.text_box.see(END)
                        self.last_sent_label(str(time.strftime("Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                        self.entry_field.delete(0, END)
                        time.sleep(0)
                        t2 = threading.Thread(target=self.playResponce, args=(ob,))
                        t2.start()
                    def find_word(text, search):

                        result = re.findall('\\b'+search+'\\b', text, flags=re.IGNORECASE)
                        if len(result)>0:
                            return True
                        else:
                            return False
                    try:
                        if user_input == 'bye':
                            foruser(user_input)
                            forbot(f"OK {str(doc['name'])} BYE")
                            doc.update({str(user_input) : f"OK {str(doc['name'])} BYE"})
                            client = pymongo.MongoClient("mongodb://localhost:27017/")
                            print(client)
                            db = client['MrAdroit']
                            collection = db['mrAdroitcollections']
                            collection.insert_one(doc)
                            root.after(3000,lambda: root.destroy())
                        elif find_word(user_input, "time"):
                            import datetime
                            foruser(user_input)
                            strTime = datetime.datetime.now().strftime("%H:%M:%S")
                            forbot(f"{str(doc['name'])}, the time is {str(strTime)}")
                            doc.update({str(user_input): f"{str(doc['name'])}, the time is {str(strTime)}"})    
                        elif find_word(user_input, "date"):
                            import datetime
                            foruser(user_input)
                            strTime = datetime.datetime.now().strftime("%d(%a)-%m(%b)-%Y")
                            res = f"Sir, the date is {strTime}"
                            # text_speech.say(f"{res}")
                            # text_speech.runAndWait()    
                            forbot(res)
                            doc.update({str(user_input) : res})
                        elif find_word(user_input, "month"):
                            import datetime
                            foruser(user_input)
                            strTime = datetime.datetime.now().strftime("%d(%a)-%m(%b)-%Y")
                            res = f"Sir, the date is {strTime}"
                            # text_speech.say(f"{res}")
                            # text_speech.runAndWait()    
                            forbot(res)
                            doc.update({str(user_input) : res})
                        elif find_word(user_input, "day"):
                            import datetime
                            foruser(user_input)
                            strTime = datetime.datetime.now().strftime("%d(%a)-%m(%b)-%Y")
                            res = f"Sir, the date is {strTime}"
                            # text_speech.say(f"{res}")
                            # text_speech.runAndWait()    
                            forbot(res)
                            doc.update({str(user_input) : res})        
                        elif find_word(user_input,"hi"):
                            foruser(user_input)
                            forbot(f"Hello {str(doc['name'])} !!")
                            doc.update({str(user_input): f"Hello {str(doc['name'])} !! How are you doing ?"})
                        elif find_word(user_input,"hello"):
                            foruser(user_input)
                            forbot(f"Greetings {str(doc['name'])} !! How you doing ?")
                            doc.update({str(user_input): f"Greetings {str(doc['name'])} !! How you doing ?"})
                        elif find_word(user_input,"hola"):
                            foruser(user_input)
                            forbot("Hey Dear !! How you doing ??")
                            doc.update({str(user_input): "Hey Dear !! How you doing ??"})
                        elif find_word(user_input,"i am good"):
                            foruser(user_input)
                            forbot("Glad to Know that !! ")
                            doc.update({str(user_input): "Glad to Know that !!"})
                        elif find_word(user_input,"i am fine"):
                            foruser(user_input)
                            forbot("Pleased to know that !!")
                            doc.update({str(user_input): "Pleased to know that !!"})
                        elif find_word(user_input,"how are you"):
                            foruser(user_input)
                            forbot("Great as Always !! How can I serve you ??")
                            doc.update({str(user_input): "Great as Always !! How can I serve you ??"})
                        elif find_word(user_input,"how you doing"):
                            foruser(user_input)
                            forbot("I am the Best !! Is there anything I can Help you with ??")
                            doc.update({str(user_input): "I am the Best !! Is there anything I can Help you with ??"})
                        elif find_word(user_input,"u tell"):
                            foruser(user_input)
                            forbot("Although its cold outside !! But I am fine !! How can I help you ??")
                            doc.update({str(user_input): "Although its cold outside !! But I am fine !! How can I help you ??"})

                        elif find_word(user_input, "age"):
                            foruser(user_input)
                            forbot("A Bot never reveals its age !! How can I serve you ??")
                            doc.update({str(user_input): "A Bot never reveals its age !! How can I serve you ??"})
                        elif find_word(user_input, "old"):
                            foruser(user_input)
                            forbot("Still young by your standards !! Is there anything I can do for you ?")
                            doc.update({str(user_input): "Still young by your standards !! Is there anything I can do for you ?"})
                        elif find_word(user_input, "morning"):
                            foruser(user_input)
                            forbot("Good Morning !! How can I help you ??")
                            doc.update({str(user_input): "Good Morning !! How can I help you ??"})
                        elif find_word(user_input, "afternoon"):
                            foruser(user_input)
                            forbot("Good Afternoon !! Is there something I can do for you ??")
                            doc.update({str(user_input): "Good Afternoon !! Is there something I can do for you ??"})
                        
                        elif (user_input== " "):
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} You entered a wrong Input !! How can I help you? ")
                            doc.update({str(user_input): f"{str(doc['name'])} You entered a wrong Input !! How can I help you?"})
                        elif (user_input== ""):
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} You sent an empty input !! How can I help you? ")
                            doc.update({str(user_input): f"{str(doc['name'])} You sent an empty input !! How can I help you?"})
                        
                        elif find_word(user_input,"sad"):
                            foruser(user_input)
                            forbot(f"As a Bot I do not have emotions !! How Can I help you {str(doc['name'])}??")
                            doc.update({str(user_input): f"As a Bot I do not have emotions !! How Can I help you {str(doc['name'])}??"})
                        elif find_word(user_input,"happy"):
                            foruser(user_input)
                            forbot(f"As a Bot I do not have emotions !! How Can I help you {str(doc['name'])}??")
                            doc.update({str(user_input): f"As a Bot I do not have emotions !! How Can I help you {str(doc['name'])}??"})
                        elif find_word(user_input,"upset"):
                            foruser(user_input)
                            forbot("As a Bot I do not have emotions !! How Can I help you ??")
                            doc.update({str(user_input): "As a Bot I do not have emotions !! How Can I help you ??"})
                        elif find_word(user_input,"calculator"):
                            webbrowser.open("https://www.calculator.com/")
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} You can perform all your calculations here")
                            doc.update({str(user_input): f"{str(doc['name'])} You can perform all your calculations here"})
                        elif (user_input=="tell me something about you"):
                            foruser(user_input)
                            forbot("I am Mister Adroit !! How I serve you ??")
                            doc.update({str(user_input): "I am Mister Adroit !! How can I serve you ??"})
                        elif (user_input=="who are you"):
                            foruser(user_input)
                            forbot(f"I am a bot !! Here to serve you {str(doc['name'])}? Ask anything ??")
                            doc.update({str(user_input): f"I am a bot !! Here to serve you {str(doc['name'])}? Ask anything ??"})
                        elif find_word(user_input,"name"):
                            foruser(user_input)
                            forbot(f"I am Mister Adroit !! How I serve you {str(doc['name'])}??")
                            doc.update({str(user_input): f"I am Mister Adroit !! How can I serve you {str(doc['name'])}??"})
                        elif find_word(user_input,"buy"):
                            webbrowser.open("https://www.amazon.com/s?k=wisconsin%27s+best+and+wisconsin+cheese+company&crid=38KQ55IWUFF4W&sprefix=wisconsin%27s+best+and%2Caps%2C182&ref=nb_sb_ss_c_1_20")
                            foruser(user_input)
                            forbot(f"Enjoy your Shopping {str(doc['name'])}!!")
                            doc.update({str(user_input): f"Enjoy your Shopping {str(doc['name'])}!!"})

                        elif find_word(user_input, "youtube"):
                            webbrowser.open("youtube.com")
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} youtube is opened")
                            doc.update({str(user_input) : f"{str(doc['name'])} youtube is opened"})

                        elif find_word(user_input, "facebook"):
                            webbrowser.open("facebook.com")
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} facebook is opened")
                            doc.update({str(user_input) : f"{str(doc['name'])} facebook is opened"})                        

                        elif find_word(user_input, "instagram"):
                            webbrowser.open("instagram.com")
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} Instagram is opened")
                            doc.update({str(user_input) : f"{str(doc['name'])} Instagram is opened"})

                        elif find_word(user_input, "paraphrasing tool"):
                            webbrowser.open("quilbot.com")
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} paraphrasing tool is opened")
                            doc.update({str(user_input) : f"{str(doc['name'])} paraphrasing tool is opened"})

                        elif find_word(user_input, "weather"):
                            webbrowser.open("windy.com")
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} weather checker is opened")
                            doc.update({str(user_input) : f"{str(doc['name'])} weather checker is opened"})

                        elif find_word(user_input, "currency"):
                            webbrowser.open("xe.com")
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} currency converter is opened")
                            doc.update({str(user_input) : f"{str(doc['name'])} currency converter is opened"})

                        elif find_word(user_input, "translator"):
                            webbrowser.open("translate.google.com")
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} language translator is opened")
                            doc.update({str(user_input) : f"{str(doc['name'])} language translator is opened"})
                        elif find_word(user_input,"movie"):
                            webbrowser.open("https://tubitv.com/home")
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} Now Search any movie you want to watch, grab your popcorns and enjoy !!")
                            doc.update({str(user_input): f"{str(doc['name'])} Enjoy your movie !!"})
                        elif find_word(user_input,"world"):
                            webbrowser.open("https://www.bbc.com/")
                            foruser(user_input)
                            forbot("Remain Updated with the world !!")
                            doc.update({str(user_input): " Remain Updated with the world !! !!"})
                        elif find_word(user_input,"pakistani news"):
                            webbrowser.open("https://arynews.tv/")
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} Here is all that keeps you updates with news all over Pakistan")
                            doc.update({str(user_input): f"{str(doc['name'])} here is all that keeps you updates with news all over Pakistan"})
                        elif find_word(user_input,"games"):
                            webbrowser.open("https://www.gamesgames.com/")
                            foruser(user_input)
                            forbot(f"Enjoy your time {str(doc['name'])}!!")
                            doc.update({str(user_input): f"Enjoy your time {str(doc['name'])}!!"})                
                        elif find_word(user_input,"order something"):
                            webbrowser.open("https://www.amazon.com/s?k=wisconsin%27s+best+and+wisconsin+cheese+company&crid=38KQ55IWUFF4W&sprefix=wisconsin%27s+best+and%2Caps%2C182&ref=nb_sb_ss_c_1_20")
                            foruser(user_input)
                            forbot("Here is all you can buy !!")
                            doc.update({str(user_input): "Here is all you can buy !!"})

                        elif find_word(user_input,"song"):
                            webbrowser.open("https://open.spotify.com/")
                            foruser(user_input)
                            forbot("Have Fun Dude !!")
                            doc.update({str(user_input): "Have Fun Dude !!"})
                        elif find_word(user_input,"email"):
                            webbrowser.open("https://mail.google.com/")
                            foruser(user_input)
                            forbot("Gmail Opened")
                            doc.update({str(user_input): "Gmail is here"})    
                        elif find_word(user_input,"bitcoin"):
                            webbrowser.open("https://www.coindesk.com/price/bitcoin/")
                            foruser(user_input)
                            forbot(f"Happy Trading {str(doc['name'])} !!")
                            doc.update({str(user_input): f"Happy Trading {str(doc['name'])} !!"})
                        elif find_word(user_input,"appointment"):
                            webbrowser.open("https://hospitals.aku.edu/pakistan/karachi/Pages/default.aspx")
                            foruser(user_input)
                            forbot("Go visit the Doctor !!")
                            doc.update({str(user_input): "Go visit the Doctor !!"})
                        elif find_word(user_input,"food"):
                            webbrowser.open("https://www.foodpanda.com/")
                            foruser(user_input)
                            forbot("Beat the Hunger !!")
                            doc.update({str(user_input): "Beat the Hunger !!"})
                        elif find_word(user_input,"google"):
                            webbrowser.open("https://www.google.com/")
                            foruser(user_input)
                            forbot("Welcome to the best search engine !!")
                            doc.update({str(user_input): "Welcome to the best search engine !!"})
                        elif find_word(user_input,"horoscope"):
                            webbrowser.open("https://www.horoscope.com/us/index.aspx")
                            foruser(user_input)
                            forbot("Search yours Horoscope!!")
                            doc.update({str(user_input): "Search yours Horoscope!!"})
                        elif find_word(user_input,"color"):
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} I like Black color !!")
                            doc.update({str(user_input): f"{str(doc['name'])} !! I like Black color"})
                        elif find_word(user_input,"book a ride"):
                            webbrowser.open("https://help.careem.com/hc/en-us/articles/360001583568-Booking-a-ride-from-Careem-website")
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} Now you can easily book a ride. Anything else you want from my side")
                            doc.update({str(user_input): f"{str(doc['name'])} Now you can easily book a ride. Anything else you want from my side"})


                        elif find_word(user_input,"grocery"):
                            webbrowser.open("https://imtiaz.com.pk/")
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} Have a nice shopping. Anything else?")
                            doc.update({str(user_input): f"{str(doc['name'])} Have a nice shopping. Anything else?"})


                        elif find_word(user_input,"online payment"):
                            webbrowser.open("https://easypaisa.com.pk/")
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} You can easily transfer your money from one place to another . How can I help you more?")
                            doc.update({str(user_input): f"{str(doc['name'])} You can easily transfer your money from one place to another . How can I help you more?"})



                        elif find_word(user_input,"parcel"):
                            webbrowser.open("https://www.dhl.com/")
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} Deliver your parcel without any stress. anything additional you would require from my end")
                            doc.update({str(user_input): f"{str(doc['name'])} Deliver your parcel without any stress. anything additional you would require from my end"})


                        elif find_word(user_input,"grammarly"):
                            webbrowser.open("https://www.grammarly.com/")
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} Correct your grammatical mistakes using grammarly. Anything else from my side?")
                            doc.update({str(user_input): f"{str(doc['name'])} Correct your grammatical mistakes using grammarly. Anything else from my side?"})


                        elif find_word(user_input,"domain"):
                            webbrowser.open("https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwiqsofcj_D8AhUOn3cKHRk_CbgYABAAGgJlZg&ohost=www.google.com&cid=CAESbOD2CYJne5CDJaIkNJoL5_A_nkjHQXzoOBHG8mD71sCm1HlE9rNDFGlFIpky4EIwQO4-5-2be4Xmky7FN1_-ZHNRNrTDNq6sGSEmV8PEcTnIzYeHXElVD4A77yXD8Y7KZlw278hAW1bVmNbEtQ&sig=AOD64_0IwJWDlYgI3thCKJourq72sLBo9Q&q&adurl&ved=2ahUKEwjAvYHcj_D8AhWYPewKHYwOCLIQ0Qx6BAgKEAE")
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} Have a nice purchasing!. How can I serve you more")
                            doc.update({str(user_input): f"{str(doc['name'])} Correct your grammatical mistakes using grammarly. Anything else from my side?"})
                        elif find_word(user_input,"clothing brand"):
                            foruser(user_input)
                            forbot(f"Hello {str(doc['name'])} I am a bot , I wear only electricity.!, How can I help you more?")
                            doc.update({str(user_input): f"Hello {str(doc['name'])} !! I am a bot , I wear only electricity.! , How can I help you more?"})

                        elif find_word(user_input,"chocolate"):
                            foruser(user_input)
                            forbot(f"Hello {str(doc['name'])} I am a bot ,I can't eat but I can suggest for you to eat 'Kitkat' , How can I help you more? ")
                            doc.update({str(user_input): f"Hello {str(doc['name'])} !! I am a bot ,I can't eat but I can suggest for you to eat 'Kitkat', How can I help you more?"})


                        elif find_word(user_input,"university"):
                            foruser(user_input)
                            forbot(f"Hello {str(doc['name'])} I have never been to university, but educated and smart more than you ;) , Ask me more if you want?")
                            doc.update({str(user_input): f"I have never been to university, but educated and smart more than you ;) , Ask me more if you want?"})

                        elif find_word(user_input,"vacation spot"):
                            foruser(user_input)
                            forbot(f"Hello {str(doc['name'])} I am a bot , I don't like any vacation spot I can only travel into internet, How can I help you more?")
                            doc.update({str(user_input): f"I am a bot , I don't like any vacation spot I can only travel into internet , How can I help you more?"})

                        elif find_word(user_input,"chai"):
                            foruser(user_input)
                            forbot(f"Hello {str(doc['name'])} I am a bot , but for chai I can be a human ;) so YESS , I'm here to help you can I more?")
                            doc.update({str(user_input): f"I am a bot , but for chai I can be a human ;) so YESS , I'm here to help you can I more?"})


                        elif find_word(user_input,"footballer"):
                            foruser(user_input)
                            forbot(f"Hello {str(doc['name'])} I am a bot I don't watch football , but people adore Messie more.!, Ask me something more if you want?")
                            doc.update({str(user_input): f"I am a bot I don't watch football , but people adore Messie more.! , Ask me more if you want?"})


                        elif find_word(user_input,"assalamoalaikum"):
                            foruser(user_input)
                            forbot(f"Hello {str(doc['name'])} Walaikumsalam , How can I help you?")
                            doc.update({str(user_input): f"Walaikumsalam {str(doc['name'])}, How can I help you?"})


                        elif find_word(user_input,"country"):
                            foruser(user_input)
                            forbot(f"Hello {str(doc['name'])} The best country is Switzerland, Ask me more if you want?")
                            doc.update({str(user_input): f"I am a bot , but for chai I can be a human ;) so YESS , Ask me more if you want?"})





                        elif find_word(user_input,"tata"):
                            foruser(user_input)
                            forbot(f"Hello {str(doc['name'])} Ok tata Hooman , If you want to ask more so surely you can?")
                            doc.update({str(user_input): f"Ok tata Hooman , If you want to ask more so surely you can?"})


                        elif find_word(user_input,"goodnight"):
                            foruser(user_input)
                            forbot(f"Sweet dreams hooman , If you want to ask me more so I'm here for you.!")
                            doc.update({str(user_input): f"Sweet dreams hooman , If you want to ask me more so I'm here for you.!"})


                        elif find_word(user_input,"smart"):
                            foruser(user_input)
                            forbot(f"I'm smart more than you think hooman , If you want to know me more so ask ?")
                            doc.update({str(user_input): f"I'm smart more than you think hooman , If you want to know me more so ask ?"})
                        elif find_word(user_input,"owner"):
                            foruser(user_input)
                            forbot(f"I am a Bot, AI created me {str(doc['name'])} !!")
                            doc.update({str(user_input): f"{str(doc['name'])} !! I am a Bot, AI created me.Is there anything I can help you with ?"})
                        elif find_word(user_input,"favourite car"):
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} Who likes any car else than Tesla, how can I help you? ")
                            doc.update({str(user_input): f"{str(doc['name'])}  Who likes any car else than Tesla, how can I help you?  "})
                        elif find_word(user_input,"live"):
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} I live in Computer !!")
                            doc.update({str(user_input): f"{str(doc['name'])} I live in this System. How I assist you with something else "})
                        elif find_word(user_input, "where are you"):
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} I exist everywhere, I know everything, Be very Scared !! Wanna ask something else ?")
                            doc.update({str(user_input): f"{str(doc['name'])}  I exist everywhere, I know everything, Be very Scared !! Wanna ask something else ?"})
                        elif find_word(user_input,"love"):
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} I am a Bot Not a Human !! You wanna ask something ?")
                            doc.update({str(user_input): f"{str(doc['name'])}I am a Bot Not a Human !! You wanna ask something ? "})
                        elif find_word(user_input,"miss"):
                            foruser(user_input)
                            forbot(f"{str(doc['name'])}I am a Bot Not a Human !! You wanna ask something ? ")
                            doc.update({str(user_input): f"{str(doc['name'])} I am a Bot Not a Human !! You wanna ask something ?"})
                        elif find_word(user_input,"Where are you "):
                            foruser(user_input)
                            forbot(f"{str(doc['name'])}In Iqra University !! You want any help ?")
                            doc.update({str(user_input): f"{str(doc['name'])}I am in Iqra University !! You want any help ? "})
                        elif find_word(user_input,"who are you"):
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} Nothing just a Machine Based on Artificial Intelligence !! That helps you in any way you want !! You wanna ask something ??")
                            doc.update({str(user_input): f"Hey {str(doc['name'])} Nothing just a Machine Based on Artificial Intelligence !! That helps you in any way you want !! You wanna ask something ??"})
                        elif find_word(user_input,"python compiler"):
                            webbrowser.open("")
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} Enjoy coding !!. You still want anything more ? ")
                            doc.update({str(user_input): f"{str(doc['name'])} Enjoy Coding"})

                        elif find_word(user_input,"programming"):
                            webbrowser.open("https://mrexamples.com/")
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} Here you can learn every programming concept !! Is there anything you want to ask ? ")
                            doc.update({str(user_input): f"{str(doc['name'])} Here you can learn every programming concept !! Is there anything you want to ask ? "})

                        elif find_word(user_input,"blackboard"):
                            webbrowser.open("https://iqra.blackboard.com/webapps/login/")
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} Welcome to BlackBoard Iqra !! How want any help more ?")
                            doc.update({str(user_input): f"{str(doc['name'])} Welcome to BlackBoard Iqra !! How want any help more ?"})

                        elif find_word(user_input,"iulms"):
                            webbrowser.open("https://iulms.iuk.edu.pk/login/index.php")
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} Welcome to Iqra IULMS . Want more help ??")
                            doc.update({str(user_input): f"{str(doc['name'])}Welcome to Iqra IULMS . Want more help ?? "})

                        elif find_word(user_input,"channel"):
                            webbrowser.open("https://www.youtube.com/@roohanazizyoutube")
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} I can spend all my time watching videos here !! Can I do something for you ??")
                            doc.update({str(user_input): f"{str(doc['name'])}I can spend all my time watching videos here !! Can I do something for you ??"})
                        elif find_word(user_input,"map"):
                            webbrowser.open("https://www.google.com/maps/")
                            foruser(user_input)
                            forbot(f"{str(doc['name'])}Drive Safe Dear !! You want more help ??")
                            doc.update({str(user_input): f"{str(doc['name'])}Drive Safe Dear !! You want more help  ??"})
                        elif find_word(user_input,"no"):
                            foruser(user_input)
                            forbot(f"Ok bye {str(doc['name'])} !!")
                            doc.update({str(user_input): f"{str(doc['name'])} bye."})
                        elif find_word(user_input,"yes"):
                            foruser(user_input)
                            forbot(f"{str(doc['name'])} Kindly tell me your query ? ")
                            doc.update({str(user_input): f"{str(doc['name'])} Kindly tell me your query ?"})
                        else:

                            foruser(user_input)
                            global result
                            result = wikipedia.summary(user_input, sentences = 1)
                            if result:
                                # say(result)
                                forbot(result)
                            
                            doc.update({str(user_input) : str(result)})
                    except:

                        forbot("I haven't learnt this from my father!! wait!! let me ask him...")
                        webbrowser.open("https://www.google.com/")
                        doc.update({str(user_input): "I haven't learnt this from my father!! wait!! let me ask him..."})

                def font_change_default(self):
                    self.text_box.config(font="Verdana 10")
                    self.entry_field.config(font="Verdana 10")
                    self.font = "Verdana 10"

                def font_change_times(self):
                    self.text_box.config(font="Times")
                    self.entry_field.config(font="Times")
                    self.font = "Times"

                def font_change_system(self):
                    self.text_box.config(font="System")
                    self.entry_field.config(font="System")
                    self.font = "System"

                def font_change_helvetica(self):
                    self.text_box.config(font="helvetica 10")
                    self.entry_field.config(font="helvetica 10")
                    self.font = "helvetica 10"

                def font_change_fixedsys(self):
                    self.text_box.config(font="fixedsys")
                    self.entry_field.config(font="fixedsys")
                    self.font = "fixedsys"

                    # Default

                def color_theme_default(self):
                    self.master.config(bg="black")
                    # self.text_frame.config(bg="#2a2b2d")
                    self.text_box.config(bg="black", fg="#137d85")
                    self.entry_frame.config(bg="black")
                    self.entry_field.config(bg="black", fg="#212121", insertbackground="#137d85")
                    self.send_button_frame.config(bg="black")
                    self.send_button.config(bg="#137d85", fg="black", activebackground="black", activeforeground="#137d85")
                    # self.emoji_button.config(bg="#212121", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
                    self.sent_label.config(bg="black", fg="#137d85")

                    self.tl_bg = "black"
                    self.tl_bg2 = "black"
                    self.tl_fg = "#137d85"

                    # light
                def color_theme_light(self):
                    self.master.config(bg="#EEEEEE")
                    self.text_frame.config(bg="#EEEEEE")
                    self.entry_frame.config(bg="#EEEEEE")
                    self.text_box.config(bg="#FFFFFF", fg="#000000")
                    self.entry_field.config(bg="#FFFFFF", fg="#000000", insertbackground="#000000")
                    self.send_button_frame.config(bg="#EEEEEE")
                    self.send_button.config(bg="#FFFFFF", fg="#000000", activebackground="#FFFFFF", activeforeground="#000000")
                    # self.emoji_button.config(bg="#FFFFFF", fg="#000000", activebackground="#FFFFFF", activeforeground="#000000")
                    self.sent_label.config(bg="#EEEEEE", fg="#000000")

                    self.tl_bg = "#FFFFFF"
                    self.tl_bg2 = "#EEEEEE"
                    self.tl_fg = "#000000"

                #green


                def color_theme_green(self):
                    self.master.config(bg="#7FB785")
                    # self.text_frame.config(bg="#2a2b2d")
                    self.text_box.config(bg="#7FB785", fg="#212121")
                    self.entry_frame.config(bg="#7FB785")
                    self.entry_field.config(bg="#7FB785", fg="#212121", insertbackground="#FFFFFF")
                    self.send_button_frame.config(bg="#7FB785")
                    self.send_button.config(bg="#212121", fg="#FFFFFF", activebackground="#7FB785", activeforeground="#FFFFFF")
                    # self.emoji_button.config(bg="#212121", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
                    self.sent_label.config(bg="#7FB785", fg="#FFFFFF")

                    self.tl_bg = "#7FB785"
                    self.tl_bg2 = "#7FB785"
                    self.tl_fg = "#212121"

                # Dark
                def color_theme_dark(self):
                    self.master.config(bg="#2a2b2d")
                    # self.text_frame.config(bg="#2a2b2d")
                    self.text_box.config(bg="#212121", fg="#FFFFFF")
                    self.entry_frame.config(bg="#2a2b2d")
                    self.entry_field.config(bg="#212121", fg="#FFFFFF", insertbackground="#FFFFFF")
                    self.send_button_frame.config(bg="#2a2b2d")
                    self.send_button.config(bg="#212121", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
                    # self.emoji_button.config(bg="#212121", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
                    self.sent_label.config(bg="#2a2b2d", fg="#FFFFFF")

                    self.tl_bg = "#212121"
                    self.tl_bg2 = "#2a2b2d"
                    self.tl_fg = "#FFFFFF"

                # Grey
                def color_theme_grey(self):
                    self.master.config(bg="#444444")
                    self.text_frame.config(bg="#444444")
                    self.text_box.config(bg="#4f4f4f", fg="#ffffff")
                    self.entry_frame.config(bg="#444444")
                    self.entry_field.config(bg="#4f4f4f", fg="#ffffff", insertbackground="#ffffff")
                    self.send_button_frame.config(bg="#444444")
                    self.send_button.config(bg="#4f4f4f", fg="#ffffff", activebackground="#4f4f4f", activeforeground="#ffffff")
                    # self.emoji_button.config(bg="#4f4f4f", fg="#ffffff", activebackground="#4f4f4f", activeforeground="#ffffff")
                    self.sent_label.config(bg="#444444", fg="#ffffff")

                    self.tl_bg = "#4f4f4f"
                    self.tl_bg2 = "#444444"
                    self.tl_fg = "#ffffff"

                def color_theme_turquoise(self):
                    self.master.config(bg="#003333")
                    self.text_frame.config(bg="#003333")
                    self.text_box.config(bg="#669999", fg="#FFFFFF")
                    self.entry_frame.config(bg="#003333")
                    self.entry_field.config(bg="#669999", fg="#FFFFFF", insertbackground="#FFFFFF")
                    self.send_button_frame.config(bg="#003333")
                    self.send_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
                    # self.emoji_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
                    self.sent_label.config(bg="#003333", fg="#FFFFFF")

                    self.tl_bg = "#669999"
                    self.tl_bg2 = "#003333"
                    self.tl_fg = "#FFFFFF"

                    # Blue

                def color_theme_dark_blue(self):
                    self.master.config(bg="#263b54")
                    self.text_frame.config(bg="#263b54")
                    self.text_box.config(bg="#1c2e44", fg="#FFFFFF")
                    self.entry_frame.config(bg="#263b54")
                    self.entry_field.config(bg="#1c2e44", fg="#FFFFFF", insertbackground="#FFFFFF")
                    self.send_button_frame.config(bg="#263b54")
                    self.send_button.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
                    # self.emoji_button.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
                    self.sent_label.config(bg="#263b54", fg="#FFFFFF")

                    self.tl_bg = "#1c2e44"
                    self.tl_bg2 = "#263b54"
                    self.tl_fg = "#FFFFFF"

                # Torque
                def color_theme_turquoise(self):
                    self.master.config(bg="#003333")
                    self.text_frame.config(bg="#003333")
                    self.text_box.config(bg="#669999", fg="#FFFFFF")
                    self.entry_frame.config(bg="#003333")
                    self.entry_field.config(bg="#669999", fg="#FFFFFF", insertbackground="#FFFFFF")
                    self.send_button_frame.config(bg="#003333")
                    self.send_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
                    # self.emoji_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
                    self.sent_label.config(bg="#003333", fg="#FFFFFF")

                    self.tl_bg = "#669999"
                    self.tl_bg2 = "#003333"
                    self.tl_fg = "#FFFFFF"

                # Hacker
                def color_theme_hacker(self):
                    self.master.config(bg="#0F0F0F")
                    self.text_frame.config(bg="#0F0F0F")
                    self.entry_frame.config(bg="#0F0F0F")
                    self.text_box.config(bg="#0F0F0F", fg="#33FF33")
                    self.entry_field.config(bg="#0F0F0F", fg="#33FF33", insertbackground="#33FF33")
                    self.send_button_frame.config(bg="#0F0F0F")
                    self.send_button.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
                    # self.emoji_button.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
                    self.sent_label.config(bg="#0F0F0F", fg="#33FF33")

                    self.tl_bg = "#0F0F0F"
                    self.tl_bg2 = "#0F0F0F"
                    self.tl_fg = "#33FF33"

                # Default font and color theme
                def default_format(self):
                    self.font_change_default()
                    self.color_theme_default()
            
            root = Tk()
            # frame2=Frame()
            # frame2.place(anchor=CENTER)
            a = ChatInterface(root)
            # root.geometry(window_size)
            root.title("Mr Adroit  ( The Smart Bot )")


            window_width = 900
            window_height = 400
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()


            center_x = int(screen_width/2 - window_width / 2)
            center_y = int(screen_height/2 - window_height / 2)

            # set the position of the window to the center of the screen
            root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


            # root.geometry("900x550")
            root.resizable(False, False)
            # root.resizable(width=False,height=False)
            # root.iconbitmap('i.ico')

            #for scroll bar
            root.attributes('-topmost', 1)
            root.mainloop()

        def submit():
            doc = {'_id': str(entry_1.get()), 'name': str(entry_02.get()), 'age': str(entry_03.get()), 'gender': str(rad.get())}
            win1.destroy()
            win3(doc)
        b1 = Button(f1, text='Submit',width=31,bg='black',fg='white', pady=0,padx=5, font='calibri 11 bold',border=0, command= submit)
        b1.place(x=140,y=340)
        # b1.bind('<Enter>',on_enter)  
        # b1.bind('<Leave>',on_leave)  
        b1.bind('<Enter>', lambda e: e.widget.config(bg='#137d85', fg='white'))
        b1.bind('<Leave>', lambda e: e.widget.config(bg='black', fg='white'))
        button3 = tk.Button(win1, text='Back', width=6, command=back,pady=2,bg="#137d85",fg="white",font="Arial",border=10,activeforeground="white",activebackground="black")
        button3.place(x=2,y=3)
        f1.place(x=185, y=-30)
        win1.resizable(False,False)
                        
    load = Image.open("hack.png")
    render = ImageTk.PhotoImage(load)
    win1.iconphoto(False, render)
    # frame = Frame(win1, width=400, height=400, bg='#137d85')
    # frame.pack()
    # frame.place(anchor='center', relx=0.5, rely=0.5)

    # img =Image.open("main1.jpg")
    # bg1 = ImageTk.PhotoImage(img)

    # label = tk.Label(win1, image=bg1, bg='black')
    # label.place(x=0, y=0, relwidth=1, relheight=1)

    window_width = 900
    window_height = 400
    screen_width = win1.winfo_screenwidth()
    screen_height = win1.winfo_screenheight()

    win1.geometry("900x550")


    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    win1.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


    button = tk.Button(win1, text='Quit', width=8, command=win1.destroy,pady=12,bg="white",fg="black",font="Arial",border=10,activeforeground="white",activebackground="black")
    button.place(x=772,y=280)
    button.bind('<Enter>', lambda e: e.widget.config(bg='#137d85', fg='white'))
    button.bind('<Leave>', lambda e: e.widget.config(bg='white', fg='black'))
    button2 = tk.Button(win1, text='Start', width=8, command=open_link,pady=12,bg="white",fg="black",font="Arial",border=10,activeforeground="white",activebackground="black")
    button2.place(x=20,y=280)
    button2.bind('<Enter>', lambda e: e.widget.config(bg='#137d85', fg='white'))
    button2.bind('<Leave>', lambda e: e.widget.config(bg='white', fg='black'))
    win1.resizable(False, False)

win1 = tk.Tk()
win1.title('Mr Adroit ( The Smart Bot )')

label = tk.Label(win1)
label.config(background="black")
image = Image.open("main1.jpg")
photo = ImageTk.PhotoImage(image)
label.place(x=0, y=0, relwidth=1, relheight=1)
load = Image.open("main1.jpg")
render = ImageTk.PhotoImage(load)
label.config(image=render)

main()

win1.mainloop()
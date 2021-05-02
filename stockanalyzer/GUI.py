try:
    from tkinter import *
    import tkinter.messagebox
    import tkinter.filedialog
    from PIL import ImageTk, Image
    import requests
    from tkinter import messagebox
    import random
    import urllib.request
    import os
    import sys

    import numpy as np
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    # Python2
    import tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
import matplotlib

# Data Source
import yfinance as yf

# Data viz
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import pandas as pd
matplotlib.use('TkAgg')
from predict import *

#================================STOCK CLASS===================================#
# Constant(s)
global data
BASE_URL = "http://ichart.finance.yahoo.com/table.csv?s="
# individual breaks the file into it's own list
# individual_list[0] will give you the first row
# individual_list[0][0] will give you the first row first column attribute


class Stock(object):

    def __init__(self, name):
        self.name = name

    # response_file is after the file has been processed through process_file.
    def average_open():
        global data
        total_sum = 0
        counter = 0
        open_list = data['Open'].tolist()
        for item in open_list:
            total_sum += item
            counter += 1
        average = total_sum / counter
        print('---------------------------------------------------------------------------------------')
        print(average)
        return average
    
    def pred():
        global data
        return data
    def average_high():
        total_sum = 0
        counter = 0
        open_list = data['High'].tolist()

        for item in open_list:
            total_sum += item
            counter += 1
        average = total_sum / counter
        return average

    def average_low():
        total_sum = 0
        counter = 0
        open_list = data['Low'].tolist()
        for item in open_list:
            total_sum += item
            counter += 1
        average = total_sum / counter
        return average

    def average_close():
        total_sum = 0
        counter = 0
        open_list = data['Close'].tolist()

        for item in open_list:
            total_sum += item
            counter += 1
        average = total_sum / counter
        return average

    def average_volume():
        total_sum = 0
        counter = 0
        open_list = data['Volume'].tolist()
        for item in open_list:
            total_sum += item
            counter += 1
        average = total_sum / counter
        return average

    # PAGE TWO METHODS
    # OPEN
    def pageTwo_Open(self, days, individual_list):
        # give me the list of open
        open_list = []
        # 0:90 means for the first three months
        NEW_FLOAT_LIST = individual_list[:days]
        for items in NEW_FLOAT_LIST:
            open_list.append(items[0])
        return open_list, len(open_list)

    # HIGH
    def pageTwo_High(self, days, individual_list):
        # give me the list of open
        open_list = []
        # 0:90 means for the first three months
        NEW_FLOAT_LIST = individual_list[:days]
        for items in NEW_FLOAT_LIST:
            open_list.append(items[1])
        return open_list, len(open_list)

    # LOW
    def pageTwo_Low(self, days, individual_list):
        # give me the list of open
        open_list = []
        # 0:90 means for the first three months
        NEW_FLOAT_LIST = individual_list[:days]
        for items in NEW_FLOAT_LIST:
            open_list.append(items[2])
        return open_list, len(open_list)

    # Close
    def pageTwo_Close(self, days, individual_list):
        print("PAGE TWO INDIVIUDAL LIST", individual_list)
        # give me the list of open
        open_list = []
        # 0:90 means for the first three months
        NEW_FLOAT_LIST = individual_list[:days]
        print("CLOSE LIST:", NEW_FLOAT_LIST)
        for items in NEW_FLOAT_LIST:
            open_list.append(items[3])
        return open_list, len(open_list)

    # Volume
    def pageTwo_Volume(self, days, individual_list):
        # give me the list of open
        open_list = []
        # 0:90 means for the first three months
        NEW_FLOAT_LIST = individual_list[:days]
        print("VOLUME LIST:", NEW_FLOAT_LIST)
        for items in NEW_FLOAT_LIST:
            open_list.append(items[4])
        return open_list, len(open_list)


#===========================MAIN CLASS===================================#
LARGE_FONT = ("Verdana", 20)
NORMAL_FONT = ("Helvetica", 16)
BASE_URL = "http://ichart.finance.yahoo.com/table.csv?s="

OBJECT_LIST = []


class Page(tk.Tk):
    # Google = Stock(object)
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def get_page(self, classname):
        '''Returns an instance of a page given it's class name as a string'''
        for page in self.frames.values():
            if str(page.__class__.__name__) == classname:
                return page
        return None

# First Home page


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        load = Image.open(
            "/Users/vishn/OSTPL-MiniProject/stockanalyzer/assets/startBackground.jpeg")
        banner = ImageTk.PhotoImage(load)
        w = tk.Label(self, image=banner)
        w.image = banner
        w.place(x=0, y=0, relwidth=1, relheight=1)

        # Start Button
        self.startImage = tk.PhotoImage(
            file="/Users/vishn/OSTPL-MiniProject/stockanalyzer/assets/startButton.gif")
        button = tk.Button(self, image=self.startImage,
                           command=lambda: controller.show_frame("PageOne"))
        button.place(x=140, y=300)

        # Close Button
        self.closeImage = tk.PhotoImage(
            file="/Users/vishn/OSTPL-MiniProject/stockanalyzer/assets/closeButton.gif")
        close_button = Button(self, image=self.closeImage, command=self.quit)
        close_button.place(x=500, y=300)

    # Calculation Page


class PageOne(tk.Frame):
    def canv(self):
        self.canvas = FigureCanvasTkAgg(self.f)
        self.canvas.get_tk_widget().place(x=30, y=200)
        img = PhotoImage(
            file="/Users/vishn/OSTPL-MiniProject/stockanalyzer/assets/background.jpeg")
        canvas.create_image(20, 20, anchor=NW, image=img)
        self.canvas.draw()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Title Page of Page One
        load = Image.open(
            "/Users/vishn/OSTPL-MiniProject/stockanalyzer/assets/background.jpeg")
        new_image = load.resize((840, 100))
        banner = ImageTk.PhotoImage(new_image)
        w = tk.Label(self, image=banner)
        w.image = banner
        w.place(x=0, y=0)

        # calculate button
        self.button_Image = tk.PhotoImage(
            file="/Users/vishn/OSTPL-MiniProject/stockanalyzer/assets/calculateButton.gif")
        button_calculate = tk.Button(
            self, text="Calculate", command=lambda: self.averageTesting(),width=10)
        button_calculate.place(x=140, y=220)

        button_predict = tk.Button(self, text="Predict",width=10,command=combine_funcs(lambda: self.something()))
        button_predict.place(x=140, y=275)

        # Second Page Graph Button
        # self.graph_Image = tk.PhotoImage(file="/Users/LinPeng/PycharmProjects/StockPrediction/graphButton.gif")
        button_graph = tk.Button(self,  text="Graph", command=combine_funcs(
            lambda: controller.show_frame("PageTwo"), self.clearLabels))
        button_graph.place(x=100, y=370)

        # Clear Button
        # self.clear_Image = tk.PhotoImage(file="/Users/LinPeng/PycharmProjects/StockPrediction/clearButton.gif")
        clear_button = tk.Button(self,  text="Clear",
                                 command=self.initialClear)
        clear_button.place(x=250, y=370)

        # Restart Button
        # self.restart_Image = tk.PhotoImage(file="/Users/LinPeng/PycharmProjects/StockPrediction/restartButton.gif")
        restart_button = tk.Button(self, text="Restart", command=restart)
        restart_button.place(x=370, y=370)

        # Back to Start button
        # self.back_Image = tk.PhotoImage(file="/Users/LinPeng/PycharmProjects/StockPrediction/back80Button.gif")
        button_back = tk.Button(self,  text="Back",
                                command=combine_funcs(lambda: controller.show_frame("StartPage"), self.clear))
        button_back.place(x=510, y=370)

        # close Button
        close_button = tk.Button(self, text="Close", command=self.quit)
        close_button.place(x=650, y=370)

        # Label Ticker Symbol Input from user
        self.user_input_tickerSymbol = tk.Label(
            self, text="Enter Ticker Symbol: ")
        self.user_input_tickerSymbol.place(x=60, y=150)

        # Ticker Symbol Input from user
        self.tickerSymbol = StringVar()
        self.entry_tickerSymbol = tk.Entry(
            self, textvariable=self.tickerSymbol)
        self.entry_tickerSymbol.place(x=200, y=150, width=100)

        # Display the check boxes
        self.selectionButtons()
        self.stocks = {}

        # The ticker symbol that the user inputs
        self.prompt = StringVar()
        self.prompt.set('')
        self.label1 = tk.Label(self, textvariable=self.prompt)
        self.label1.place(x=330, y=530)

    def delete_TickerSymbolEntry(self):
        self.entry_tickerSymbol.delete(0, END)

    def createLabel_Average(self, cleanedText, placementValue):
        self.msg = Label(text=cleanedText, font=NORMAL_FONT, fg='SlateBlue4')
        self.msg.place(x=420, y=550+placementValue, anchor="center")

    def initialClear(self):
        try:
            getValues = [self.average_open.get(), self.average_high.get(), self.average_low.get(),
                         self.average_close.get(), self.average_volume.get()]
            checkBoxes = [self.average_open, self.average_high, self.average_low,
                          self.average_close, self.average_volume]
            length = len(getValues)
            for i in range(length):
                print(getValues[i])
                if getValues[i] == 1:
                    checkBoxes[i].set(0)
        except:
            pass
        finally:
            self.clear()

    def clear(self):
        self.prompt.set(" ")
        self.delete_TickerSymbolEntry()
        self.resultMsg.place_forget()
        length = len(self.switches)
        for i in range(length):
            self.newVarList[i].place_forget()
            self.newTextList[i].set(" ")
            if self.switches[i] == 1:
                self.checkBoxes[i].set(0)

    def clearLabels(self):
        length = len(self.switches)
        for i in range(length):
            self.newVarList[i].place_forget()
            self.newTextList[i].set(" ")

    def displayUpdate(self, varName, labelName):
        self.prompt.set("Entered Ticker Symbol: " +
                        self.tickerSymbol.get().upper())
        self.label1.update_idletasks()

        varName.set(self.cleanedText)
        labelName.update_idletasks()

    # Execute TicketSymbol and Average Calculation
    def something(self, event=None):
        global data
        processing(data)

    def averageTesting(self, event=None):
        global data
        data = yf.download(tickers=self.tickerSymbol.get(),
                           period='3y', interval='1d')
        # print(self.tickerSymbol.get())
        # processing(data)
        print(data)
        self.data=data
        data.reset_index(level=0, inplace=True)
        data.head()
        fig = go.Figure(data=go.Ohlc(x=data['Date'],
                                     open=data['Open'],
                                     high=data['High'],
                                     low=data['Low'],
                                     close=data['Close']))
        fig.show()
        if self.average_open.get() == 0 and self.average_high.get() == 0 and self.average_low.get() == 0 and \
                self.average_close.get() == 0 and self.average_volume.get() == 0 and len(self.tickerSymbol.get()) == 0:
            messagebox.showerror(
                "User Entry Error", "Insert a ticker symbol & check which you would like calculate")
        elif self.average_open.get() == 0 and self.average_high.get() == 0 and self.average_low.get() == 0 and \
                self.average_close.get() == 0 and self.average_volume.get() == 0:
            messagebox.showerror("Check Boxes Error",
                                 "Check which you would like to calculate")
        else:
            self.individual_list = []
            self.objectX = create_stockInstance(self.tickerSymbol.get())
            get_Data(self.tickerSymbol.get(),
                     self.objectX, self.individual_list)
            #self.cleanedUpList = cleanedUpList(self.individual_list)
            self.average()

    def get_Object(self):
        #print("PAGE ONE SELF OBJECTX: ", self.objectX)
        return self.objectX

    def label_Results(self):
        # label for Results
        self.resultMsg = tk.Label(self, text="RESULTS", font=LARGE_FONT)
        self.resultMsg.place(x=425, y=500, anchor="center")

    def destroy(self):
        for labels in self.newVarList:
            labels.place_forget()

    # Calculating the average(s)
    def average(self):
        self.label_Results()
        try:
            self.destroy()
        except:
            pass

        #open = Stock(self.objectX).average_open()
        open = Stock.average_open()
        # high = Stock(self.objectX).average_high(self.cleanedUpList)
        high = Stock.average_high()
        # low = Stock(self.objectX).average_low(self.cleanedUpList)
        low = Stock.average_low()
        # close = Stock(self.objectX).average_close(self.cleanedUpList)
        close = Stock.average_close()
        # volume = Stock(self.objectX).average_volume(self.cleanedUpList)
        volume = Stock.average_volume()

        self.switches = [self.average_open.get(), self.average_high.get(), self.average_low.get(),
                         self.average_close.get(), self.average_volume.get()]
        options = [("Open Average:", (round(open, 5))), ("High Average:", (round(high, 5))), ("Low Average:", (round(low, 5))),
                   ("Close Average:", (round(close, 5))), ("Volume Average:", (round(volume, 5)))]
        gotten = []
        self.checkBoxes = [self.average_open, self.average_high, self.average_low,
                           self.average_close, self.average_volume]
        self.list_of_widgets = []

        for k, option in enumerate(options):
            if self.switches[k]:
                gotten.append(option)

        self.newVarList = []
        self.newTextList = []
        self.cleanedText = " "

        length = len(gotten)
        print(length)
        self.placementValue = 25

        i = 0
        joinedList = []
        for value in range(length):
            joinedText = ''.join(str(gotten[value]))
            self.cleanedText = joinedText.replace(
                '(', '').replace(')', '').replace(',', '')
            joinedList.append(self.cleanedText)
            # creating a StringVar for each cleanedText
            self.newTextList.append(StringVar())
            self.newTextList[i].set('')
            self.newVarList.append(tk.Label(textvariable=self.newTextList[i]))
            self.newVarList[i].place(
                x=420, y=550+self.placementValue, anchor="center")
            self.displayUpdate(self.newTextList[i], self.newVarList[i])
            i += 1
            self.placementValue += 25

        print(joinedList)

    # selection buttons
    def selectionButtons(self):
        # Selection calculation list
        selectionButton = tk.Label(
            self, text="What would you like to calculate?")
        selectionButton.place(x=450, y=150)
        # average open check box
        self.average_open = IntVar()
        Checkbutton(self, text="Average Open",
                    variable=self.average_open).place(x=450, y=170)
        # average high check box
        self.average_high = IntVar()
        Checkbutton(self, text="Average High",
                    variable=self.average_high).place(x=450, y=195)
        # average low check box
        self.average_low = IntVar()
        Checkbutton(self, text="Average Low",
                    variable=self.average_low).place(x=450, y=220)
        # average close check box
        self.average_close = IntVar()
        Checkbutton(self, text="Average Close",
                    variable=self.average_close).place(x=450, y=245)
        # average volume check box
        self.average_volume = IntVar()
        Checkbutton(self, text="Average Volume",
                    variable=self.average_volume).place(x=450, y=270)


class PageTwo(PageOne):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        load = Image.open(
            "/Users/vishn/OSTPL-MiniProject/stockanalyzer/assets/graphBanner.gif")
        banner = ImageTk.PhotoImage(load)
        w = tk.Label(self, image=banner)
        w.image = banner
        w.place(x=0, y=0)

        button_back = tk.Button(self, text="Restart",
                                command=restart)
        button_back.place(x=50, y=130)

        self.button2 = tk.Button(
            self, text='Print Graph', command=self.print_it)
        self.button2.place(x=200, y=130)

        self.button3 = tk.Button(
            self, text='Clear Plot', command=self.clearCanvas)
        self.button3.place(x=370, y=130)

        self.button4 = tk.Button(self, text='Go Back', command=combine_funcs(
            lambda: controller.show_frame("PageOne"), self.clearBack))
        self.button4.place(x=550, y=130)

        self.button5 = tk.Button(self, text='Close', command=self.quit)
        self.button5.place(x=730, y=130)

        # Display selection buttons
        self.selectionButtons()

    def print_it(self):
        try:
            self.clearCanvas()
            self.canvas.get_tk_widget().destory()
        except:
            pass

        if self.selectedValue() == 0:
            messagebox.showerror("Oops!", "Select how many days to graph")
        else:
            self.f = Figure(figsize=(5, 5), dpi=110)
            self.p = self.f.gca()

            daysVar = self.days.get()
            page_one = self.controller.get_page("PageOne")
            # open = page_one.average_open.get()
            open = 102
            high = page_one.average_high.get()
            low = page_one.average_low.get()
            close = page_one.average_close.get()
            volume = page_one.average_volume.get()

            self.objectY = page_one.get_Object()
            # print("PAGE TWO OBJECTY:", self.objectY)

            pageTwo_cleanedUpList = convertToFloat(page_one.individual_list)

            # Returns list and the length of the list in a tuple
            self.varOpen = Stock(self.objectY).pageTwo_Open(
                daysVar, pageTwo_cleanedUpList)
            self.varHigh = Stock(self.objectY).pageTwo_High(
                daysVar, pageTwo_cleanedUpList)
            self.varLow = Stock(self.objectY).pageTwo_Low(
                daysVar, pageTwo_cleanedUpList)
            self.varClose = Stock(self.objectY).pageTwo_Close(
                daysVar, pageTwo_cleanedUpList)
            self.varVolume = Stock(self.objectY).pageTwo_Volume(
                daysVar, pageTwo_cleanedUpList)

            switches = [open, high, low, close, volume]
            options = [self.createOpen, self.createHigh,
                       self.createLow, self.createClose, self.createVolume]
            pageTwo_gotten = []
            for i, switch in enumerate(switches):
                if switch:
                    # print("SWITCH:", switch, " at", i)
                    pageTwo_gotten.append(options[i])
                    # createCanvas(self.f)
            pageTwo_gotten.append(self.createCanvas)
            length = len(pageTwo_gotten)

            for i in range(length):
                pageTwo_gotten[i]()

    # Create Canvas
    def createCanvas(self):
        self.canvas = FigureCanvasTkAgg(self.f)
        self.canvas.get_tk_widget().place(x=30, y=200)
        self.canvas.draw()

    # Clear Canvas
    def clearCanvas(self):
        self.canvas.get_tk_widget().place_forget()
        self.p.close()
        page_one = self.controller.get_page("PageOne")
        self.clear()
        page_one.clear()

    def clearBack(self):
        self.days.set(0)
        self.canvas.get_tk_widget().place_forget()
        self.p.close()

    def createOpen(self):
        createHist_Variables(self.varOpen[0], self.varOpen[1], self.p, 'Open')

    def createHigh(self):
        createHist_Variables(self.varHigh[0], self.varHigh[1], self.p, 'High')

    def createLow(self):
        createHist_Variables(self.varLow[0], self.varLow[1], self.p, 'Low')

    def createClose(self):
        createHist_Variables(
            self.varClose[0], self.varClose[1], self.p, 'Close')

    def createVolume(self):
        createHist_Variables(
            self.varVolume[0], self.varVolume[1], self.p, 'Volume')

    # selection buttons
    def selectionButtons(self):
        # Selection calculation list
        self.days = IntVar()
        self.selectionButton = tk.Label(
            self, text="How many days would you like to graph?")
        self.selectionButton.place(x=550, y=170)
        self.button30 = Radiobutton(
            self, text="30 Days", variable=self.days, value=30, command=self.selectedValue)
        self.button30.place(x=610, y=190)
        self.button60 = Radiobutton(
            self, text="60 Days", variable=self.days, value=60, command=self.selectedValue)
        self.button60.place(x=610, y=210)
        self.button90 = Radiobutton(
            self, text="90 Days", variable=self.days, value=90, command=self.selectedValue)
        self.button90.place(x=610, y=230)

    def selectedValue(self):
        self.daysVariable = int(self.days.get())
        print("You selected the option ", self.daysVariable)
        return self.daysVariable

#===============================EXTERNAL FUNCTIONS=======================================================================#


def createHist_Variables(histoList, lengthLength, p, histoLabel):
    histoList = histoList
    lengthList = lengthLength
    meanHistoList = np.mean(histoList)
    createHistogram(p, histoList, lengthList, meanHistoList, histoLabel)


def createHistogram(p, histoList, lengthList, meanHistoList, histoLabel):
    colorHistoList = ['red', 'blue', 'green', 'cyan', 'magenta', 'yellow', 'teal', 'orange', 'maroon', 'coral', 'cyan',
                      'orchid', 'lightpink', 'steelblue', 'midnightblue', 'gold', 'darkred', 'saddlebrown', 'black',
                      'dimgrey', 'peru']
    averageColorList = ['gold', 'darkred', 'saddlebrown', 'black', 'dimgrey', 'peru', 'aliceblue', 'yellowgreen',
                        'skyblue', 'darkblue', 'indigo']

    p.hist(histoList, color=random.choice(colorHistoList), alpha=0.75, histtype='stepfilled',
           label=histoLabel)
    # average line
    p.axvline(meanHistoList, color=random.choice(
        averageColorList), linewidth=2)
    p.set_xlabel('Daily', fontsize=15)
    p.set_ylabel('Frequency', fontsize=15)
    p.legend(loc='upper right')


def return_TickerSymbol(tickerSymbol):
    name = tickerSymbol
    return name


def create_stockInstance(tickerSymbol):
    # Creating multiple instances of Stock class from user input
    returned = tickerSymbol
    newInstance = Stock(returned)
    return newInstance


def get_Data(returned, newInstance, new_list):
    if len(returned) > 0:
        validate_file(new_list)
    else:
        messagebox.showerror("Oops", "Enter a valid ticker symbol")


def validate_file(new_list):
    new_list = data


def cleanedUpList(individual_list):
    # Popping the Categories
    individual_list.pop(0)
    # Popping the Dates
    for item in individual_list:
        item.pop(0)
    # Converting everything to float
    new_float_list = [[float(j) for j in i] for i in individual_list]
    return new_float_list


def convertToFloat(strList):
    # Converting everything to float
    new_float_list = [[float(j) for j in i] for i in strList]
    return new_float_list

# Function to Combine methods


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

# Function to Restart the entire program


def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)


if __name__ == "__main__":
    global root
    root = Page()
    root.geometry('850x850')
    root.title("STOCK V.1")
    root.mainloop()

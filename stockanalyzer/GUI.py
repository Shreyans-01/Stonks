
#from predict import *
from tkinter import *
from tkinter import messagebox
import tkinter.filedialog
from PIL import ImageTk, Image
import requests
import urllib.request
import os
import sys

import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import tkinter as tk

import matplotlib

# Data Source
import yfinance as yf

# For Plotting
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import pandas as pd

from bs4 import BeautifulSoup
import requests
import mouse
import time
matplotlib.use('TkAgg')

global data, pred_val, avg_open, avg_high, avg_low, avg_close

# Stocks


class Stock(object):

    def __init__(self, name):
        self.name = name

    # response_file is after the file has been processed through process_file.
    def average_open():
        global data
        total_sum = 0
        counter = 0
        open_list = data['open'].tolist()
        for item in open_list:
            total_sum += item
            counter += 1
        average = total_sum / counter
        return average

    def pred():
        global data
        return data

    def average_high():
        total_sum = 0
        counter = 0
        open_list = data['high'].tolist()

        for item in open_list:
            total_sum += item
            counter += 1
        average = total_sum / counter
        return average

    def average_low():
        total_sum = 0
        counter = 0
        open_list = data['low'].tolist()
        for item in open_list:
            total_sum += item
            counter += 1
        average = total_sum / counter
        return average

    def average_close():
        total_sum = 0
        counter = 0
        open_list = data['close'].tolist()

        for item in open_list:
            total_sum += item
            counter += 1
        average = total_sum / counter
        return average

    def average_volume():
        total_sum = 0
        counter = 0
        open_list = data['volume'].tolist()
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


# Main
LARGE_FONT = ("Verdana", 20)
NORMAL_FONT = ("Helvetica", 16)


class Page(tk.Tk):
    # Google = Stock(object)
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree):
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
            "/OSTPL-MiniProject/stockanalyzer/assets/bg-startpage.jpg")
        banner = ImageTk.PhotoImage(load)
        w = tk.Label(self, image=banner)
        w.image = banner
        w.place(x=0, y=0, relwidth=1, relheight=1)

        # Start Button
        button = tk.Button(self, text="Start",
                           command=lambda: controller.show_frame("PageOne"), width=10, font=('oswald', 25, 'bold'), bg='#ff7b00')
        button.place(x=160, y=300)

        # Close Button
        close_button = Button(self, text="Close", command=self.quit, width=10, font=(
            'oswald', 25, 'bold'), bg='#D0EFFF')
        close_button.place(x=520, y=300)

    # Calculation Page


class PageOne(tk.Frame):
    def canv(self):
        self.canvas = FigureCanvasTkAgg(self.f)
        self.canvas.get_tk_widget().place(x=30, y=200)
        img = PhotoImage(
            file="/OSTPL-MiniProject/stockanalyzer/assets/bgstonks.jpg")
        canvas.create_image(20, 20, anchor=NW, image=img)
        self.canvas.draw()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Title Page of Page One
        load = Image.open(
            "/OSTPL-MiniProject/stockanalyzer/assets/bgstonks.jpg")
        new_image = load.resize((840, 200))
        banner = ImageTk.PhotoImage(new_image)
        w = tk.Label(self, image=banner)
        w.image = banner
        w.place(x=0, y=0)

        # calculate button
        button_calculate = tk.Button(
            self, text="Calculate", command=lambda: self.averageTesting(), width=10)
        button_calculate.place(x=140, y=320)

        button_predict = tk.Button(
            self, text="Predict", width=10, command=combine_funcs(lambda: self.something()))
        button_predict.place(x=140, y=375)

        button_graph = tk.Button(self,  text="Graph", command=combine_funcs(
            lambda: controller.show_frame("PageTwo"), self.clearLabels))
        button_graph.place(x=100, y=470)

        button_compare = tk.Button(self,  text="Compare", command=combine_funcs(lambda: controller.show_frame("PageThree"), self.clearLabels))
        button_compare.place(x=210, y=470)

        clear_button = tk.Button(self,  text="Clear",
                                 command=self.initialClear)
        clear_button.place(x=320, y=470)

        restart_button = tk.Button(self, text="Restart", command=restart)
        restart_button.place(x=430, y=470)

        button_back = tk.Button(self,  text="Back",
                                command=combine_funcs(lambda: controller.show_frame("StartPage"), self.clear))
        button_back.place(x=540, y=470)

        # close Button
        close_button = tk.Button(self, text="Close", command=self.quit)
        close_button.place(x=650, y=470)

        # Label Ticker Symbol Input from user
        self.user_input_tickerSymbol = tk.Label(
            self, text="Enter Ticker Symbol: ")
        self.user_input_tickerSymbol.place(x=60, y=250)

        # Ticker Symbol Input from user
        self.tickerSymbol = StringVar()
        self.entry_tickerSymbol = tk.Entry(
            self, textvariable=self.tickerSymbol)
        self.entry_tickerSymbol.place(x=200, y=250, width=100)

        # Display the check boxes
        self.selectionButtons()
        self.stocks = {}

        # The ticker symbol that the user inputs
        self.prompt = StringVar()
        self.prompt.set('')
        self.label1 = tk.Label(self, textvariable=self.prompt)
        self.label1.place(x=330, y=630)

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
        try:
            length = len(self.switches)
            for i in range(length):
                self.newVarList[i].place_forget()
                self.newTextList[i].set(" ")
        except:
            pass

    def displayUpdate(self, varName, labelName):
        self.prompt.set("       Entered Ticker Symbol: " +
                        self.tickerSymbol.get().upper())
        self.label1.update_idletasks()

        varName.set(self.cleanedText)
        labelName.update_idletasks()

    # Execute TicketSymbol and Average Calculation
    def something(self, event=None):
        global data, pred_val
        df1 = pd.DataFrame(data)
        #pred_val = processing(df1)
        self.average(1)

    def averageTesting(self, event=None):
        global data
        data = yf.download(tickers=self.tickerSymbol.get(),
                           period='3y', interval='1d')
        data.reset_index(level=0, inplace=True)
        # Change all column headings to be lower case, and remove spacing
        data.columns = [str(x).lower().replace(' ', '_') for x in data.columns]
        # Convert Date column to datetime
        data.loc[:, 'date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')
        print(data)
        self.data = data
        data.reset_index(level=0, inplace=True)
        data.head()

        if self.average_open.get() == 0 and self.average_high.get() == 0 and self.average_low.get() == 0 and \
                self.average_close.get() == 0 and self.average_volume.get() == 0 and len(self.tickerSymbol.get()) == 0:
            messagebox.showerror(
                "User Entry Error", "Insert a ticker symbol & check which you would like calculate")
        elif self.average_open.get() == 0 and self.average_high.get() == 0 and self.average_low.get() == 0 and \
                self.average_close.get() == 0 and self.average_volume.get() == 0:
            messagebox.showerror("Check Boxes Error",
                                 "Check which you would like to calculate")
        else:
            self.average(0)

    def label_Results(self):
        # label for Results
        self.resultMsg = tk.Label(self, text="RESULTS", font=LARGE_FONT)
        self.resultMsg.place(x=425, y=550, anchor="center")

    def destroy(self):
        for labels in self.newVarList:
            labels.place_forget()

    # Calculating the average(s)
    def average(self, n):
        global pred_val
        self.label_Results()
        try:
            self.destroy()
        except:
            pass

        open = Stock.average_open()
        high = Stock.average_high()
        low = Stock.average_low()
        close = Stock.average_close()
        volume = Stock.average_volume()

        self.switches = [self.average_open.get(), self.average_high.get(), self.average_low.get(),
                         self.average_close.get(), self.average_volume.get(), n]
        options = [('Open Average : ', (round(open, 5))), ('High Average : ', (round(high, 5))), ('Low Average : ', (round(low, 5))),
                   ('Close Average : ', (round(close, 5))), ('Volume Average : ', (round(volume, 5)))]
        gotten = []
        self.checkBoxes = [self.average_open, self.average_high, self.average_low,
                           self.average_close, self.average_volume]
        self.list_of_widgets = []
        if n == 1:
            if data["adj_close"][data.shape[0]-1]<=pred_val:
                color=1
            else:
                color=0
            options.append(('Next Day Prediction : ', (round(pred_val, 5))))
        for k, option in enumerate(options):
            if self.switches[k]:
                gotten.append(option)
        self.newVarList = []
        self.newTextList = []
        self.cleanedText = " "

        length = len(gotten)
        self.placementValue = 25

        i = 0
        joinedList = []
        for value in range(length):
            joinedText = ''.join(str(gotten[value]))
            self.cleanedText = joinedText.replace('(', '').replace(')', '').replace(',', '').replace('\'','')
            joinedList.append(self.cleanedText)
            # creating a StringVar for each cleanedText
            self.newTextList.append(StringVar())
            self.newTextList[i].set('')
            if n==1 and value==length-1:
                if color==1:
                    self.newVarList.append(tk.Label(textvariable=self.newTextList[i],fg='green',font=('bold')))
                else:
                    self.newVarList.append(tk.Label(textvariable=self.newTextList[i],fg='red', font=('bold')))
            else:
                self.newVarList.append(tk.Label(textvariable=self.newTextList[i]))
            self.newVarList[i].place(x=420, y=650+self.placementValue, anchor="center")
            self.displayUpdate(self.newTextList[i], self.newVarList[i])
            i += 1
            self.placementValue += 25

        print(joinedList)
        url='https://ca.finance.yahoo.com/quote/'+self.tickerSymbol.get()+'?p='+self.tickerSymbol.get()+'&.tsrc=fin-tre-srch'
        # url = 'https://ca.finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-tre-srch'
        variable_time=0
        while True:
            try:
                page = requests.get(url)
                soup = BeautifulSoup(page.text, 'lxml')
                if  soup.find('span', class_ = 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)')!=None:
                    price = soup.find('span', class_ = 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text
                    # print(price)
                    print(self.tickerSymbol.get())
                    root.update_idletasks()
                    print(float(price))
                    diff=float(price)-float(data['close'][data.shape[0]-1])
                    diff='%.6f' %diff
                    # diff=round(diff,4)
                    print(diff)
                    
                    if float(data['close'][data.shape[0]-1])<float(price):
                        self.stockprice = tk.Label(self, text="Current value: "+str(price)+'\n▲'+str(diff), font=NORMAL_FONT,anchor="center",fg='green')
                        self.stockprice.place(x=350, y=575)
                    else:
                        self.stockprice = tk.Label(self, text="Current value: "+str(price)+'\n▼'+str(diff), font=NORMAL_FONT,anchor="center",fg='red')
                        self.stockprice.place(x=350, y=575)
                    # self.stockprice.config(text="")
                    
                    

                if mouse.is_pressed("left"):
                    break
                root.update_idletasks()
            except:
                pass
            root.update_idletasks()
            

        # price=1
        

    # selection buttons
    def selectionButtons(self):
        global avg_open, avg_close, avg_low, avg_high
        # Selection calculation list
        selectionButton = tk.Label(
            self, text="What would you like to calculate?")
        selectionButton.place(x=450, y=250)
        # average open check box
        self.average_open = IntVar()
        Checkbutton(self, text="Average Open",
                    variable=self.average_open).place(x=450, y=270)
        avg_open = self.average_open
        # average high check box
        self.average_high = IntVar()
        Checkbutton(self, text="Average High",
                    variable=self.average_high).place(x=450, y=295)
        avg_high = self.average_high
        # average low check box
        self.average_low = IntVar()
        Checkbutton(self, text="Average Low",
                    variable=self.average_low).place(x=450, y=320)
        avg_low = self.average_low
        # average close check box
        self.average_close = IntVar()
        Checkbutton(self, text="Average Close",
                    variable=self.average_close).place(x=450, y=345)
        avg_close = self.average_close
        # average volume check box
        self.average_volume = IntVar()
        Checkbutton(self, text="Average Volume",
                    variable=self.average_volume).place(x=450, y=370)


class PageTwo(PageOne):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        load = Image.open("/OSTPL-MiniProject/stockanalyzer/assets/graphbg.png")
        banner = ImageTk.PhotoImage(load)
        new_image1 = load.resize((840, 200))
        banner = ImageTk.PhotoImage(new_image1)
        w = tk.Label(self, image=banner)
        w.image = banner
        w.place(x=0, y=0)
        button_back = tk.Button(self, text="Restart",
                                command=restart)
        button_back.place(x=50, y=230)

        self.button2 = tk.Button(
            self, text='Print Graph', command=self.print_it)
        self.button2.place(x=200, y=230)

        self.button3 = tk.Button(
            self, text='Clear Plot', command=self.clearCanvas)
        self.button3.place(x=370, y=230)

        self.button4 = tk.Button(self, text='Go Back', command=combine_funcs(
            lambda: controller.show_frame("PageOne"), self.clearBack))
        self.button4.place(x=550, y=230)

        self.button5 = tk.Button(self, text='Close', command=self.quit)
        self.button5.place(x=730, y=230)

        self.button6 = tk.Button(
            self, text="Detailed Graph", width=10, command=lambda: self.detailed_graph())
        self.button6.place(x=400, y=810)

        # Display selection buttons
        self.selectionButtons()

    def detailed_graph(self):
        global data
        fig = go.Figure(data=go.Ohlc(x=data['date'],
                                     open=data['open'],
                                     high=data['high'],
                                     low=data['low'],
                                     close=data['close']))
        fig.show()

    def print_it(self):
        global data, avg_open, avg_close, avg_high, avg_low
        try:
            self.clearCanvas()
            self.canvas.get_tk_widget().destory()
        except:
            pass

        if self.selectedValue() == 0:
            messagebox.showerror("Oops!", "Select how many days to graph")
        else:
            self.f = Figure(figsize=(9, 4), dpi=110)
            self.p = self.f.gca()
            daysVar = self.days.get()
            plot1 = self.f.add_subplot(111)
            df = pd.DataFrame(
                columns=['date', 'open', 'high', 'low', 'close', 'volume'])
            print(data)
            print(data['date'][0])
            for i in range(data.shape[0]-1-daysVar, data.shape[0]-1):
                new_row = pd.Series(data={'date': data['date'][i], 'open': data['open'][i], 'high': data['high']
                                          [i], 'low': data['low'][i], 'close': data['close'][i], 'volume': data['volume'][i]}, name=i)
                df = df.append(new_row)
            if avg_open.get() == 1:
                plot1.plot(df['date'], df['open'], label="Open")
            if avg_close.get() == 1:
                plot1.plot(df['date'], df['close'], label="Close")
            if avg_high.get() == 1:
                plot1.plot(df['date'], df['high'], label="High")
            if avg_low.get() == 1:
                plot1.plot(df['date'], df['low'], label="Low")

            leg = plot1.legend()

            self.createCanvas()
    # Create Canvas

    def createCanvas(self):
        self.canvas = FigureCanvasTkAgg(self.f)
        self.canvas.get_tk_widget().place(x=-70, y=360)
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

    # selection buttons

    def selectionButtons(self):
        # Selection calculation list
        self.days = IntVar()
        self.selectionButton = tk.Label(
            self, text="How many days would you like to graph?")
        self.selectionButton.place(x=550, y=270)
        self.button30 = Radiobutton(
            self, text="30 Days", variable=self.days, value=30, command=self.selectedValue)
        self.button30.place(x=610, y=290)
        self.button60 = Radiobutton(
            self, text="60 Days", variable=self.days, value=60, command=self.selectedValue)
        self.button60.place(x=610, y=310)
        self.button90 = Radiobutton(
            self, text="90 Days", variable=self.days, value=90, command=self.selectedValue)
        self.button90.place(x=610, y=330)

    def selectedValue(self):
        self.daysVariable = int(self.days.get())
        print("You selected the option ", self.daysVariable)
        return self.daysVariable

class PageThree(PageOne):
    datae=[]
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        load = Image.open("/OSTPL-MiniProject/stockanalyzer/assets/graphbg.png")
        banner = ImageTk.PhotoImage(load)
        new_image1 = load.resize((840, 200))
        banner = ImageTk.PhotoImage(new_image1)
        w = tk.Label(self, image=banner)
        w.image = banner
        w.place(x=0, y=0)

        # Label Ticker Symbol Input from user
        self.user_input_tickerSymbol = tk.Label(
            self, text="Enter Ticker Symbol: ")
        self.user_input_tickerSymbol.place(x=60, y=250)

        # Ticker Symbol Input from user
        self.tickerSymbol=[StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]
        for i in range(5):
            self.entry_tickerSymbol = tk.Entry(
                self, textvariable=self.tickerSymbol[i])
            self.entry_tickerSymbol.place(x=200 +i*100, y=250, width=100)

        # button_back = tk.Button(self, text="Restart",
        #                         command=restart)
        # button_back.place(x=50, y=230)

        self.button3 = tk.Button(
            self, text='Clear Plot', command=self.clearCanvas)
        self.button3.place(x=250, y=300)

        self.button4 = tk.Button(self, text='Go Back', command=combine_funcs(
            lambda: controller.show_frame("PageOne"), self.clearBack))
        self.button4.place(x=350, y=300)

        self.button5 = tk.Button(self, text='Close', command=self.quit)
        self.button5.place(x=450, y=300)

        # self.button6 = tk.Button(
        #     self, text="Detailed Graph", width=10, command=lambda: self.detailed_graph())
        # self.button6.place(x=400, y=810)
        
        button_print = tk.Button(self, text="Print",command=self.print_it)
        button_print.place(x=150, y=300)

        # Display selection buttons
        self.selectionButtons()

    def detailed_graph(self):
        global data
        fig = go.Figure(data=go.Ohlc(x=data['date'],
                                     open=data['open'],
                                     high=data['high'],
                                     low=data['low'],
                                     close=data['close']))
        fig.show()

    def print_it(self):
        global data, avg_open, avg_close, avg_high, avg_low
        try:
            self.clearCanvas()
            self.canvas.get_tk_widget().destory()
        except:
            pass

        if self.selectedValue() == 0:
            messagebox.showerror("Error", "Select how many days to graph")
        else:
            datae=[]
            counter=0
            for i in range(5):
                if self.tickerSymbol[i].get()!="":
                    datae.append(yf.download(tickers=self.tickerSymbol[i].get(),period='3y', interval='1d')) 
                    datae[i].reset_index(level=0, inplace=True)
                    # Change all column headings to be lower case, and remove spacing
                    datae[i].columns = [str(x).lower().replace(' ', '_') for x in datae[i].columns]
                    counter+=1
                    #print(datae[i])
            self.f = Figure(figsize=(9, 4), dpi=110)
            self.p = self.f.gca()
            daysVar = self.days.get()
            plot1 = self.f.add_subplot(111)
            list_df = [pd.DataFrame(columns=['date', 'close']),pd.DataFrame(columns=['date', 'close']),pd.DataFrame(columns=['date', 'close']),pd.DataFrame(columns=['date', 'close']),pd.DataFrame(columns=['date', 'close'])]
            for j in range(counter):
                for i in range(datae[j].shape[0]-1-daysVar, datae[j].shape[0]-1):
                    new_row = pd.Series(data={'date': datae[j]['date'][i], 'close': datae[j]['close'][i]}, name=i)
                    list_df[j] = list_df[j].append(new_row)
            
            for i in range(counter):
                plot1.plot(list_df[i]['date'], list_df[i]['close'], label=self.tickerSymbol[i].get())
            leg = plot1.legend(loc="upper right")

            self.createCanvas()
    # Create Canvas

    def createCanvas(self):
        self.canvas = FigureCanvasTkAgg(self.f)
        self.canvas.get_tk_widget().place(x=-70, y=360)
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

    # selection buttons

    def selectionButtons(self):
        # Selection calculation list
        self.days = IntVar()
        self.selectionButton = tk.Label(
            self, text="How many days would you like to graph?")
        self.selectionButton.place(x=550, y=270)
        self.button30 = Radiobutton(
            self, text="30 Days", variable=self.days, value=30, command=self.selectedValue)
        self.button30.place(x=610, y=290)
        self.button60 = Radiobutton(
            self, text="60 Days", variable=self.days, value=60, command=self.selectedValue)
        self.button60.place(x=610, y=310)
        self.button90 = Radiobutton(
            self, text="90 Days", variable=self.days, value=90, command=self.selectedValue)
        self.button90.place(x=610, y=330)

    def selectedValue(self):
        self.daysVariable = int(self.days.get())
        print("You selected the option ", self.daysVariable)
        return self.daysVariable


# External Functions


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
    root.title("STONKS")
    root.mainloop()

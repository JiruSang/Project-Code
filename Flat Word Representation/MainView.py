#-*-   coding:   utf-8   -*-
from tkinter import *

import tkinter as tk

from tkinter import ttk

from Regression import ReGression

# Develop a simple scoring system GUI
class ViewMain:

    def __init__(self, parent):
        '''Create the GUI.'''

        # Framework.
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack()

        # Model.
        self.state = StringVar()
        self.state.set("Predict:")

        self.title = StringVar()
        self.title_lab = Label(self.frame, textvariable=self.title, fg='black', width=80, height=3, compound='center')
        self.title.set("<<<Automatic Scoring System>>>")
        self.title_lab.pack()


        self.input = StringVar()
        self.text = Text(self.frame)
        self.text.pack()

        e = StringVar()
        entry = Entry(self.frame, validate='key', textvariable=e, width=80)
        entry.pack()

        self.variable = StringVar(self.frame)
        self.variable.set("Q1")

        # set up a pull-down menu
        w = OptionMenu(self.frame, self.variable, "Q1", "Q2", "Q3","Q4")
        w.pack()

        self.label = Label(self.frame,textvariable=self.state)
        self.label.pack()

        # Buttons to control application.
        self.up = Button(self.frame, text='predict', command=self.upClick,fg='black', width=80, height=3)
        self.up.pack(side='left')


    def upClick(self):
        self.label.setvar()

        line = self.text.get("0.0", "end")

        ques = self.variable.get()


        print(line,self.variable.get())

        rg = ReGression(filepath="data/all_"+ques+".txt")

        y_pred = rg.predict(sentence=line)


        res = 'Score for this answer :'+str(y_pred[0][0])


        self.state.set(res)




    def quitClick(self):
        self.parent.destroy()


if __name__ == '__main__':
    window = Tk()
    myapp = ViewMain(window)
    window.mainloop()
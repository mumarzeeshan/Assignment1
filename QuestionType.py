#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Oct 13, 2017 05:06:41 PM
import sys
import TF
import MCQ
import Numerc
import Login
import Database


try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import QuestionType_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = QuestionType (root)
    QuestionType_support.init(root, top)
    root.mainloop()

w = None
def create_QuestionType(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = QuestionType (w)
    QuestionType_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_QuestionType():
    global w
    w.destroy()
    w = None


class QuestionType:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI Black} -size 11 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI Black} -size 12 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font14 = "-family {Segoe UI Black} -size 18 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"

        top.geometry("688x525+371+102")
        top.title("QuestionType")
        top.configure(background="#333333")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.07, rely=0.29, relheight=0.58, relwidth=0.86)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#00ffff")
        self.Frame1.configure(width=595)

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.2, rely=0.07, height=47, width=350)
        self.Label2.configure(background="#333333")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font12)
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''What type of question you want to add?''')
        self.Label2.configure(width=350)

        def TrF():
            root.destroy()
            TF.vp_start_gui()



        def MCQs():
            root.destroy()
            MCQ.vp_start_gui()

        def Numeric():
            root.destroy()
            Numerc.vp_start_gui()


        self.TF = Button(self.Frame1, command = lambda : TrF() )
        self.TF.place(relx=0.39, rely=0.33, height=33, width=114)
        self.TF.configure(activebackground="#ffffff")
        self.TF.configure(activeforeground="#000000")
        self.TF.configure(background="#333333")
        self.TF.configure(disabledforeground="#a3a3a3")
        self.TF.configure(font=font10)
        self.TF.configure(foreground="#ffffff")
        self.TF.configure(highlightbackground="#d9d9d9")
        self.TF.configure(highlightcolor="black")
        self.TF.configure(pady="0")
        self.TF.configure(text='''T/F''')
        self.TF.configure(width=114)

        self.MCQs = Button(self.Frame1, command = lambda : MCQs())
        self.MCQs.place(relx=0.39, rely=0.56, height=33, width=114)
        self.MCQs.configure(activebackground="#ffffff")
        self.MCQs.configure(activeforeground="#000000")
        self.MCQs.configure(background="#333333")
        self.MCQs.configure(disabledforeground="#a3a3a3")
        self.MCQs.configure(font=font10)
        self.MCQs.configure(foreground="#ffffff")
        self.MCQs.configure(highlightbackground="#d9d9d9")
        self.MCQs.configure(highlightcolor="black")
        self.MCQs.configure(pady="0")
        self.MCQs.configure(text='''MCQs''')
        self.MCQs.configure(width=114)

        self.Numeric = Button(self.Frame1, command = lambda: Numeric())
        self.Numeric.place(relx=0.39, rely=0.79, height=33, width=114)
        self.Numeric.configure(activebackground="#ffffff")
        self.Numeric.configure(activeforeground="#000000")
        self.Numeric.configure(background="#333333")
        self.Numeric.configure(disabledforeground="#a3a3a3")
        self.Numeric.configure(font=font10)
        self.Numeric.configure(foreground="#ffffff")
        self.Numeric.configure(highlightbackground="#d9d9d9")
        self.Numeric.configure(highlightcolor="black")
        self.Numeric.configure(pady="0")
        self.Numeric.configure(text='''Numeric''')

        self.Label = Label(top)
        self.Label.place(relx=0.35, rely=0.1, height=21, width=194)
        self.Label.configure(background="#333333")
        self.Label.configure(disabledforeground="#a3a3a3")
        self.Label.configure(font=font14)
        self.Label.configure(foreground="#ffffff")
        self.Label.configure(text='''Add a Question''')
        self.Label.configure(width=194)

        self.FinishButton = Button(self.Frame1, command=lambda: finish())
        self.FinishButton.place(relx=0.05, rely=0.79, height=33, width=68)
        self.FinishButton.configure(activebackground="#d9d9d9")
        self.FinishButton.configure(activeforeground="#000000")
        self.FinishButton.configure(background="#333333")
        self.FinishButton.configure(disabledforeground="#a3a3a3")
        self.FinishButton.configure(font=font10)
        self.FinishButton.configure(foreground="#ffffff")
        self.FinishButton.configure(highlightbackground="#d9d9d9")
        self.FinishButton.configure(highlightcolor="black")
        self.FinishButton.configure(pady="0")
        self.FinishButton.configure(text='''Finish''')
        self.FinishButton.configure(width=68)

        def finish():
            root.destroy()
            #Database.conn.close()
            Login.vp_start_gui()






if __name__ == '__main__':
    vp_start_gui()




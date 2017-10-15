#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Oct 15, 2017 09:16:43 PM
import sys


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

import Quiz_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Quiz (root)
    Quiz_support.init(root, top)
    root.mainloop()

w = None
def create_Quiz(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Quiz (w)
    Quiz_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Quiz():
    global w
    w.destroy()
    w = None


class Quiz:
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
        font9 = "-family {Segoe UI Black} -size 24 -weight bold -slant"  \
            " roman -underline 0 -overstrike 0"

        top.geometry("731x552+357+93")
        top.title("Quiz")
        top.configure(background="#333333")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.CreationFrame = Frame(top)
        self.CreationFrame.place(relx=0.14, rely=0.25, relheight=0.52
                , relwidth=0.72)
        self.CreationFrame.configure(relief=GROOVE)
        self.CreationFrame.configure(borderwidth="1")
        self.CreationFrame.configure(relief=GROOVE)
        self.CreationFrame.configure(background="#00ffff")
        self.CreationFrame.configure(highlightbackground="#d9d9d9")
        self.CreationFrame.configure(highlightcolor="black")
        self.CreationFrame.configure(width=525)

        self.Question = Label(self.CreationFrame)
        self.Question.place(relx=0.11, rely=0.11, height=21, width=394)
        self.Question.configure(background="#333333")
        self.Question.configure(disabledforeground="#a3a3a3")
        self.Question.configure(font=font10)
        self.Question.configure(foreground="#ffffff")
        self.Question.configure(text='''Q:''')
        self.Question.configure(width=394)

        self.Next = Button(self.CreationFrame)
        self.Next.place(relx=0.38, rely=0.77, height=34, width=107)
        self.Next.configure(activebackground="#d9d9d9")
        self.Next.configure(activeforeground="#000000")
        self.Next.configure(background="#333333")
        self.Next.configure(disabledforeground="#a3a3a3")
        self.Next.configure(font=font10)
        self.Next.configure(foreground="#ffffff")
        self.Next.configure(highlightbackground="#d9d9d9")
        self.Next.configure(highlightcolor="black")
        self.Next.configure(pady="0")
        self.Next.configure(text='''Next Question''')
        self.Next.configure(width=107)

        self.a = Label(self.CreationFrame)
        self.a.place(relx=0.11, rely=0.25, height=21, width=134)
        self.a.configure(background="#d9d9d9")
        self.a.configure(disabledforeground="#a3a3a3")
        self.a.configure(foreground="#000000")
        self.a.configure(text='''a''')
        self.a.configure(width=134)

        self.b = Label(self.CreationFrame)
        self.b.place(relx=0.11, rely=0.43, height=21, width=134)
        self.b.configure(activebackground="#f9f9f9")
        self.b.configure(activeforeground="black")
        self.b.configure(background="#d9d9d9")
        self.b.configure(disabledforeground="#a3a3a3")
        self.b.configure(foreground="#000000")
        self.b.configure(highlightbackground="#d9d9d9")
        self.b.configure(highlightcolor="black")
        self.b.configure(text='''b''')
        self.b.configure(width=134)

        self.c = Label(self.CreationFrame)
        self.c.place(relx=0.59, rely=0.25, height=21, width=144)
        self.c.configure(activebackground="#f9f9f9")
        self.c.configure(activeforeground="black")
        self.c.configure(background="#d9d9d9")
        self.c.configure(disabledforeground="#a3a3a3")
        self.c.configure(foreground="#000000")
        self.c.configure(highlightbackground="#d9d9d9")
        self.c.configure(highlightcolor="black")
        self.c.configure(text='''c''')
        self.c.configure(width=144)

        self.d = Label(self.CreationFrame)
        self.d.place(relx=0.59, rely=0.42, height=21, width=144)
        self.d.configure(activebackground="#f9f9f9")
        self.d.configure(activeforeground="black")
        self.d.configure(background="#d9d9d9")
        self.d.configure(disabledforeground="#a3a3a3")
        self.d.configure(foreground="#000000")
        self.d.configure(highlightbackground="#d9d9d9")
        self.d.configure(highlightcolor="black")
        self.d.configure(text='''d''')
        self.d.configure(width=144)

        self.UserAnswer = Entry(self.CreationFrame)
        self.UserAnswer.place(relx=0.36, rely=0.63, relheight=0.07
                , relwidth=0.24)
        self.UserAnswer.configure(background="white")
        self.UserAnswer.configure(disabledforeground="#a3a3a3")
        self.UserAnswer.configure(font="TkFixedFont")
        self.UserAnswer.configure(foreground="#000000")
        self.UserAnswer.configure(insertbackground="black")
        self.UserAnswer.configure(width=124)

        self.Logo = Label(top)
        self.Logo.place(relx=0.36, rely=0.14, height=41, width=211)
        self.Logo.configure(activebackground="#f9f9f9")
        self.Logo.configure(activeforeground="black")
        self.Logo.configure(background="#333333")
        self.Logo.configure(disabledforeground="#a3a3a3")
        self.Logo.configure(font=font9)
        self.Logo.configure(foreground="#ffffff")
        self.Logo.configure(highlightbackground="#d9d9d9")
        self.Logo.configure(highlightcolor="black")
        self.Logo.configure(text='''Quiz''')






if __name__ == '__main__':
    vp_start_gui()




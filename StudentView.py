#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Oct 15, 2017 03:39:56 PM
import sys
import profile

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

import StudentView_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = CreateAQuiz (root)
    StudentView_support.init(root, top)
    root.mainloop()

w = None
def create_CreateAQuiz(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = CreateAQuiz (w)
    StudentView_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_CreateAQuiz():
    global w
    w.destroy()
    w = None


class CreateAQuiz:
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
        top.title("CreateAQuiz")
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



        def getQuizes():
            i = 0
            x=[0,0]
            Database.c.execute("SELECT qTitle from Question")
            str=Database.c.fetchall()
            print str[0][0]
            self.Label8.configure(text=str[0][0])
            #self.Label8.configure(text="Quiz#1,Quiz#2,Quiz#3,Quiz#4,Quiz#5,Quiz#6,Quiz#7")
            #self.Label8.configure(text=str[0])
                # print "quiz"



        self.Label8 = Label(self.CreationFrame)
        self.Label8.place(relx=0.11, rely=0.2, height=40, width=394)
        self.Label8.configure(background="#333333")
        self.Label8.configure(disabledforeground="#a3a3a3")

        self.Label8.configure(foreground="#ffffff")
        #self.Label8.configure(text='''What quiz you want to take?''')
        self.Label8.configure(width=394)


        self.Label1 = Label(self.CreationFrame)
        self.Label1.place(relx=0.11, rely=0.35, height=21, width=394)
        self.Label1.configure(background="#333333")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''What quiz you want to take?''')
        self.Label1.configure(width=394)

        self.QuizChoice = Entry(self.CreationFrame)
        self.QuizChoice.place(relx=0.11, rely=0.49, relheight=0.07
                , relwidth=0.75)
        self.QuizChoice.configure(background="white")
        self.QuizChoice.configure(disabledforeground="#a3a3a3")
        self.QuizChoice.configure(font="TkFixedFont")
        self.QuizChoice.configure(foreground="#000000")
        self.QuizChoice.configure(insertbackground="black")
        self.QuizChoice.configure(width=394)

        self.TakeQuiz = Button(self.CreationFrame, command=lambda: getQuizes())
        self.TakeQuiz.place(relx=0.42, rely=0.6, height=34, width=87)
        self.TakeQuiz.configure(activebackground="#d9d9d9")
        self.TakeQuiz.configure(activeforeground="#000000")
        self.TakeQuiz.configure(background="#333333")
        self.TakeQuiz.configure(disabledforeground="#a3a3a3")
        self.TakeQuiz.configure(font=font10)
        self.TakeQuiz.configure(foreground="#ffffff")
        self.TakeQuiz.configure(highlightbackground="#d9d9d9")
        self.TakeQuiz.configure(highlightcolor="black")
        self.TakeQuiz.configure(pady="0")
        self.TakeQuiz.configure(text='''Get Quiz''')
        self.TakeQuiz.configure(width=87)

        def quiz(q):
            if q=="AP":
                '''This class configures and populates the toplevel window.
                          top is the toplevel containing window.'''
                _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
                _fgcolor = '#000000'  # X11 color: 'black'
                _compcolor = '#d9d9d9'  # X11 color: 'gray85'
                _ana1color = '#d9d9d9'  # X11 color: 'gray85'
                _ana2color = '#d9d9d9'  # X11 color: 'gray85'
                font10 = "-family {Segoe UI Black} -size 11 -weight bold " \
                         "-slant roman -underline 0 -overstrike 0"
                font9 = "-family {Segoe UI Black} -size 24 -weight bold -slant" \
                        " roman -underline 0 -overstrike 0"

                top.geometry("731x552+357+93")
                top.title("Quiz")
                top.configure(background="#333333")
                top.configure(highlightbackground="#d9d9d9")
                top.configure(highlightcolor="black")

                Database.c.execute("SELECT Question from Question where QID=2")
                b=Database.c.fetchone()
                Database.c.execute("SELECT Option1 from Question where QID=2")
                d = Database.c.fetchone()
                Database.c.execute("SELECT Option2 from Question where QID=2")
                e = Database.c.fetchone()
                Database.c.execute("SELECT Option3 from Question where QID=2")
                f = Database.c.fetchone()


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
                self.Question.configure(text=b)
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
                self.a.configure(text=d)
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
                self.b.configure(text=e)
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
                self.c.configure(text=f)
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
                #root.destroy()
                #Quiz.vp_start_gui()
                print "q"


            print "Quiz"
        self.submit = Button(self.CreationFrame, command= lambda : quiz(self.QuizChoice.get()))
        self.submit.place(relx=0.42, rely=0.8, height=34, width=87)
        self.submit.configure(activebackground="#d9d9d9")
        self.submit.configure(activeforeground="#000000")
        self.submit.configure(background="#333333")
        self.submit.configure(disabledforeground="#a3a3a3")
        self.submit.configure(font=font10)
        self.submit.configure(foreground="#ffffff")
        self.submit.configure(highlightbackground="#d9d9d9")
        self.submit.configure(highlightcolor="black")
        self.submit.configure(pady="0")
        self.submit.configure(text='''submit''')
        self.submit.configure(width=87)

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
    profile.run('vp_start_gui()')


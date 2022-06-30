from tkinter import *
import tkinter.messagebox as box

#   RIVEDERE QUESTA CLASSE
class VistaUnclockAmministratore():

            def   __init__(self):
                          window = Tk()
                          window.title('Login amministratore')

                          frame = Frame(window)

                          self.Label1 = Label(window,text = 'Nome utente:')
                          self.Label1.pack(padx=15,pady= 5)

                          self.entry1 = Entry(window,bd =5)
                          self.entry1.pack(padx=15, pady=5)

                          self.username = self.entry1.get()

                          self.Label2 = Label(window,text = 'Password: ')
                          self.Label2.pack(padx = 15,pady=6)

                          self.entry2 = Entry(window, bd=5)
                          self.entry2.pack(padx = 15,pady=7)

                          self.password = self.entry2.get()
                          # BHO QUESTE ULTIME DUE
                          self.frame.pack(padx=100,pady = 19)
                          self.window.mainloop()

            def login():
                    if (self.username == 'RistoMatic' and  self.password == 'amadeus'):
                              btn = Button(self.frame, text = 'Check Login',command = self.dialog1)
                              return True
                    else:
                          btn = Button(self.frame, text ='Check Login', command = self.dialog2)
                          return False

                    btn.pack(side = RIGHT , padx =5)





            def dialog1():
                      box.showinfo('info','Accesso concesso!')
            def dialog2():
                      box.showinfo('info','Accesso negato!')

from math import e
from tkinter import *

import tkinter.messagebox


click = False



def start():

    global tk

    tk = Tk()

    tk.title("Tic Tac Toe")


    def play(button):

        global click, tk


        if button["text"] == " " and click:

            button["text"] = "X"

            click = False

        elif button["text"] == " ":

            button['text'] = "O"

            click = True


        if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or

            button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or

            button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or

            button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or

            button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or

            button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or

            button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or

            button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):

            answer = tkinter.messagebox.askquestion('X Player won the game!!!', 'Do you want to play again')
            tk.destroy()
            

            if answer == 'yes': start()


        elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or

            button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or

            button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or

            button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or

            button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or

            button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or

            button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or

            button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):

            answer = tkinter.messagebox.askquestion('O Player won the game!!!', 'Do you want to play again')
            tk.destroy()

            if answer == 'yes': start()


        elif (button1["text"] != " " and button2["text"] != " " and button3["text"] != " " and

              button4["text"] != " " and button5["text"] != " " and button6["text"] != " " and

              button7["text"] != " " and button8["text"] != " " and button9["text"] != " "):

            answer = tkinter.messagebox.askquestion('Draw!!!', 'Do you want to play again')

            tk.destroy()

            if answer == 'yes': start()




    button1 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button1))

    button1.grid(row=1, column=0)


    button2 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button2))

    button2.grid(row=1, column=1)


    button3 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button3))

    button3.grid(row=1, column=2)


    button4 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button4))

    button4.grid(row=2, column=0)


    button5 = Button(tk, text=" ", font=("Times 26 bold"), height=4, width=8, command=lambda:play(button5))

    button5.grid(row=2, column=1)


    button6 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button6))

    button6.grid(row=2, column=2)


    button7 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button7))

    button7.grid(row=3, column=0)


    button8 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button8))

    button8.grid(row=3, column=1)


    button9 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button9))

    button9.grid(row=3, column=2)



    tk.mainloop()


start()

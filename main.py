from tkinter import *
import tkmacosx



root= Tk()

root.title('Calc')
root.geometry('240x315')
root.config(padx=0, pady=0)
root.grid_columnconfigure(0, weight=1)
root.resizable(False, False)
root.config(bg='#5b5b5b')



text = Label(root,height=1,text='0', width=25, justify='right', anchor='e', bg='#1f1d1d', fg='white', font=('Helvetica',60))
text.grid(column=0, row=0, columnspan=4)

btn1 = tkmacosx.Button(root, text='AC', bg='#2e2c2c', fg='white', height=48, width=60, font=('arial', 20), highlightthickness=0)
btn2 = tkmacosx.Button(root, text='-/+', bg='#2e2c2c', fg='white', height=48, width=60, font=('arial', 20), highlightthickness=0)
btn3 = tkmacosx.Button(root, text='%', bg='#2e2c2c', fg='white', height=48, width=60, font=('arial', 20), highlightthickness=0)
btn4 = tkmacosx.Button(root, text='/', bg='orange', fg='white', height=48, width=60, font=('arial', 20), highlightthickness=0)

btn1.grid(column=0, row=2, sticky=NSEW)
btn2.grid(column=1, row=2, sticky=NSEW)
btn3.grid(column=2, row=2, sticky=NSEW)
btn4.grid(column=3, row=2, sticky=NSEW)


btn5 = tkmacosx.Button(root, text='7', bg='#5b5b5b', fg='white', height=48, width=60, font=('arial', 20), highlightthickness=0)
btn6 = tkmacosx.Button(root, text='8', bg='#5b5b5b', fg='white', height=48, width=60, font=('arial', 20), highlightthickness=0)
btn7 = tkmacosx.Button(root, text='9', bg='#5b5b5b', fg='white', height=48, width=60, font=('arial', 20), highlightthickness=0)
btn8 = tkmacosx.Button(root, text='x', bg='orange', fg='white', height=48, width=60, font=('arial', 20), highlightthickness=0)

btn5.grid(column=0, row=3, sticky=NSEW)
btn6.grid(column=1, row=3, sticky=NSEW)
btn7.grid(column=2, row=3, sticky=NSEW)
btn8.grid(column=3, row=3, sticky=NSEW)


btn9 = tkmacosx.Button(root, text='6', bg='#5b5b5b', fg='white', height=48, width=60, font=('arial', 20), highlightthickness=0)
btn10 = tkmacosx.Button(root, text='5', bg='#5b5b5b', fg='white', height=48, width=60, font=('arial', 20), highlightthickness=0)
btn11 = tkmacosx.Button(root, text='4', bg='#5b5b5b', fg='white', height=48, width=60, font=('arial', 20), highlightthickness=0)
btn12 = tkmacosx.Button(root, text='-', bg='orange', fg='white', height=48, width=60, font=('arial', 20), highlightthickness=0)


btn9.grid(column=0, row=4, sticky=NSEW)
btn10.grid(column=1, row=4, sticky=NSEW)
btn11.grid(column=2, row=4, sticky=NSEW)
btn12.grid(column=3, row=4, sticky=NSEW)



btn13 = tkmacosx.Button(root, text='1', bg='#5b5b5b', fg='white', height=48, width=60, font=('arial', 20), highlightthickness=0)
btn14 = tkmacosx.Button(root, text='2', bg='#5b5b5b', fg='white', height=48, width=60, font=('arial', 20), highlightthickness=0)
btn15 = tkmacosx.Button(root, text='3', bg='#5b5b5b', fg='white', height=48, width=60, font=('arial', 20), highlightthickness=0)
btn16 = tkmacosx.Button(root, text='+', bg='orange', fg='white', height=48, width=60, font=('arial', 20), highlightthickness=0)

btn13.grid(column=0, row=5, sticky=NSEW)
btn14.grid(column=1, row=5, sticky=NSEW)
btn15.grid(column=2, row=5, sticky=NSEW)
btn16.grid(column=3, row=5, sticky=NSEW)

btn17 = tkmacosx.Button(root, text=' 0 ', bg='#5b5b5b', fg='white', height=48, width=120, padx=3, font=('arial', 20), highlightthickness=0)
btn18 = tkmacosx.Button(root, text=' . ', bg='#5b5b5b', fg='white', height=48, width=60, font=('arial', 20), highlightthickness=0)
btn19 = tkmacosx.Button(root, text='=', bg='orange', fg='white', height=48, width=60, font=('arial', 20), highlightthickness=0)


btn17.grid(column=0, row=6, sticky=NSEW, columnspan=2)
btn18.grid(column=2, row=6, sticky=NSEW)
btn19.grid(column=3, row=6, sticky=NSEW)


root.mainloop()

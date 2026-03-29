from tkinter import *
root= Tk()
root.title('Example of Place')
root.geometry("300x250")
label= Label(root,text='Absolute position',bg='purple',fg='white')
label.place(x=50,y=50,width=100,height=50)
root.mainloop()

# from tkinter import *


# root= Tk()

# root.title("Simple calculator")
# root.config(bg='black')

# e = Entry(root, width=35, borderwidth=5)
# e.grid(row=0,column=0,columnspan=3, padx=10,pady=10)

# def button_click(number):
#     current = e.get()
#     e.delete(0,END)
#     e.insert(0,str(current)+str(number))

# def button_clear():
#     e.delete(0, END)

# a=0
# def button_add():
#     firstnum=e.get()
#     global f_num,a
#     f_num=int(firstnum)
#     e.delete(0,END)
#     a=1
    

# def button_sub():
#     firstnum=e.get()
#     global f_num,a
#     f_num=int(firstnum)
#     e.delete(0,END)
#     a=2
    

# def button_mul():
#     firstnum=e.get()
#     global f_num,a
#     f_num=int(firstnum)
#     e.delete(0,END)
#     a=3
    
# def button_div():
#     firstnum=e.get()
#     global f_num,a
#     f_num=int(firstnum)
#     e.delete(0,END)
#     a=4
    


# def button_equal():
#     second_num=e.get()
#     e.delete(0,END)
#     if a==1:
#         e.insert(0,f_num+int(second_num))
#     elif a==2:
#         e.insert(0,f_num-int(second_num))
#     elif a==3:
#         e.insert(0,f_num+int(second_num))
#     elif a==4:
#         e.insert(0,f_num/int(second_num))
#     else:
#         print('not working')

    
# button_1= Button(root,bg='black',fg='white',text="1",padx=45,relief='groove',pady=20,command=lambda:button_click(1))
# button_2= Button(root,bg='black',foreground='white',text="2",padx=45,relief='groove' ,pady=20,command =lambda:button_click(2))
# button_3= Button(root,bg='black',foreground='white',text="3",padx=45 ,relief='groove',pady=20, command =lambda:button_click(3))
# button_4= Button(root,bg='black',foreground='white', text="4",padx=45,relief='groove' ,pady=20, command =lambda:button_click(4))
# button_5= Button(root,bg='black',foreground='white', text="5",padx=45,relief='groove' ,pady=20, command = lambda:button_click(5))
# button_6= Button(root,bg='black',foreground='white', text="6",padx=45,relief='groove' ,pady=20, command = lambda:button_click(6))
# button_7= Button(root,bg='black',foreground='white', text="7",padx=45,relief='groove' ,pady=20, command = lambda:button_click(7))
# button_8= Button(root,bg='black',foreground='white', text="8",padx=45,relief='groove' ,pady=20, command = lambda:button_click(8))
# button_9= Button(root,bg='black',foreground='white', text="9",padx=45,relief='groove' ,pady=20, command = lambda:button_click(9))
# button_0= Button(root,bg='black',foreground='white', text="0",padx=45,relief='groove' ,pady=20, command = lambda:button_click(0))

# button_equal=Button(root,text="=",bg='black',foreground='white',padx=95,pady=20,command=button_equal,relief='groove')
# button_add= Button(root,text="+",bg='black',foreground='white',padx=45,pady=20,command= button_add,relief='groove')
# button_clear=Button(root,text='Clear',bg='black',foreground='white',padx=85,pady=20,command=button_clear,relief='groove')
# button_sub= Button(root,text="-",bg='black',foreground='white',padx=45,relief='groove',pady=20,command=button_sub)

# button_mul= Button(root, text="x",padx=45,relief='groove' ,pady=20,bg='black',foreground='white',command =button_mul)
# button_div= Button(root, text="/",padx=45 ,relief='groove',pady=20, bg='black',foreground='white',command =button_div)


# button_1.grid(row=3,column=0)
# button_2.grid(row=3,column=1)
# button_3.grid(row=3,column=2)


# button_4.grid(row=2,column=0)
# button_5.grid(row=2,column=1)
# button_6.grid(row=2,column=2)


# button_7.grid(row=1,column=0)
# button_8.grid(row=1,column=1)
# button_9.grid(row=1,column=2)

# button_0.grid(row=4,column=0)
# button_clear.grid(row=4,column=1,columnspan=2)
# button_add.grid(row=5,column=0)
# button_equal.grid(row=5,column=1,columnspan=2)

# button_sub.grid(row=6,column=0)
# button_mul.grid(row=6,column=1)
# button_div.grid(row=6,column=2)


# root.mainloop()
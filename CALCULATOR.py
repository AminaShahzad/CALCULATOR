import tkinter.messagebox
from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('amina shahzad')
root.geometry('455x399')
Label(text='calculator',font = 'Helvetica 14 bold',pady=20).pack()
Label(text='<IT WILL RETURN APPROXIMATE VALUES FOR DECIMAL RESULTS.>').pack(side='bottom')
Label(text= 'NOTE : <AFTER EVERY CACULATION KINDLY CLICK CLEAR ONCE.>').pack(side='bottom')

value = StringVar()
value.set("")
E1=Entry(root,relief='sunken',borderwidth=20,bg='grey',fg='white',font='Helvetica 14 ',textvar=value).pack()
c=''
e=[]
def click(event):
    result=0

    global value
    global c , e
    a= event.widget.cget("text")
    if a!='Clear' and a!='=':
        value.set(value.get()+str(a))
        print(a)
    if a!='+'and a!='-' and a!='x' and a!= '/' and a!='Clear' and a!='=':
        c += str(a)
        print(c)
    else:
        e.append(c)


        if a!= '=' and a!= 'Clear':

           e.append(a)
           print(e)
           c=''

        if a == 'Clear':

            c=''
            f = ''
            e.pop()
            if e != []:
                e.pop()
            if e==[]:
                value.set('')
            print(e)
            for i in range(0, len(e)):
                f += str(e[i])
                value.set(f)






        elif a == '=':

           for i in e:
               if '/' in e:
                   f = e.index('/')
                   if len(e) >= 3:
                    if str(e[f - 1]).isdigit() == False or str(e[f + 1]).isdigit() == False:
                       tkinter.messagebox.showerror('Incorrect','YOU HAVE ENTERED AN INCORRECT VALUE!!')
                       e = []
                    else:
                       g = int(e[f - 1]) / int(e[f + 1])
                       print(result)
                       print(g)
                       e[f + 1] =int(g)
                       if len(e) >=3:
                          e.pop(f - 1)
                       e.remove('/')
                       print(e)
                       result = g
                       print(result)
                       c = ''
               elif 'x' in e:
                   f = e.index('x')
                   if len(e) >= 3:
                     if str(e[f - 1]).isdigit() == False or str(e[f + 1]).isdigit() == False:
                       tkinter.messagebox.showerror('Incorrect', 'YOU HAVE ENTERED AN INCORRECT VALUE!!')
                       e = []
                     else:
                       g = int(e[f - 1]) * int(e[f + 1])
                       print(result)
                       print(g)
                       e[f + 1] = g
                       if len(e) >= 3:
                           e.pop(f - 1)
                       e.remove('x')
                       print(e)
                       result = g
                       print(result)
                       c = ''

               elif '+' in e:
                 f=e.index('+')
                 if len(e) >= 3:
                   if str(e[f-1]).isdigit()== False or str(e[f+1]).isdigit()== False:
                     tkinter.messagebox.showerror('Incorrect', 'YOU HAVE ENTERED AN INCORRECT VALUE!!')
                     e=[]
                   else:
                     g=int(e[f-1])+int(e[f+1])
                     print(result)
                     print(g)
                     e[f+1]=g
                     if len(e) >= 3:
                         e.pop(f - 1)
                     e.remove('+')
                     print(e)
                     result= g
                     print(result)
                     c=''

               elif '-' in e:
                    f = e.index('-')
                    if len(e) >= 3:
                      if str(e[f-1]).isdigit()== False or str(e[f+1]).isdigit()== False:
                        tkinter.messagebox.showerror('Incorrect', 'YOU HAVE ENTERED AN INCORRECT VALUE!!')
                        e=[]
                      else:
                        g = int(e[f - 1]) - int(e[f + 1])
                        print(result)
                        print(g)
                        e[f + 1] = g
                        if len(e) >= 3:
                            e.pop(f - 1)
                        e.remove('-')
                        print(e)
                        result = g
                        print(result)
                        c=''

           value.set(result)
           e = []

count=9
f1=Frame(root,borderwidth=30,relief='sunken')
for i in range(0,3):
    for j in range(0,3):
       b=Button(f1,text =count, borderwidth=5,relief='sunken',padx=20)
       b.grid(row=i,column=j)
       b.bind('<Button-1>', click)
       count-=1
b1=Button(f1,text = 0,borderwidth=5,relief='sunken',padx=20)
b1.grid(row=3,column=0)
b1.bind('<Button-1>',click)
b2=Button(f1,text = 'Clear',borderwidth=5,relief='sunken',padx=10)
b2.grid(row=0,column=3)
b2.bind('<Button-1>',click)
b3=Button(f1,text = '=',borderwidth=5,relief='sunken',padx=20)
b3.grid(row=3,column=1)
b3.bind('<Button-1>',click)
b4=Button(f1,text = '/',borderwidth=5,relief='sunken',padx=20)
b4.grid(row=3,column=2)
b4.bind('<Button-1>',click)
b5=Button(f1,text = '+',borderwidth=5,relief='sunken',padx=20)
b5.grid(row=1,column=3)
b5.bind('<Button-1>',click)
b6=Button(f1,text = '-',borderwidth=5,relief='sunken',padx=20)
b6.grid(row=2,column=3)
b6.bind('<Button-1>',click)
b7=Button(f1,text = 'x',borderwidth=5,relief='sunken',padx=20)
b7.grid(row=3,column=3)
b7.bind('<Button-1>',click)
f1.pack()
root.mainloop()
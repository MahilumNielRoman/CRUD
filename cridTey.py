from Tkinter import *

infos = []


def validationnum(number):
    if number.isdigit():
        return True
    elif number is "":
        return True
    else:
        return False



def validationlet(letter):
    if letter.isalpha():
        return True
    elif letter is "":
        return True
    else:
        return False


def limit_student_number(*args):
    studentnumber = 11
    limit = std.get()
    if len(limit) > studentnumber:
        std.set(limit[:studentnumber])


class student:
    def __init__(self, name, section, course, number):
        self.name = name
        self.section = section
        self.course = course
        self.number = number

    def getName(self):
        return self.name

    def getsection(self):
        return self.section

    def getcourse(self):
        return self.course

    def getnumber(self):
        return self.number

    def updateSelf(self, name, section, course, number):
        self.name = name
        self.section = section
        self.course = course
        self.number = number

        btn1['state'] = DISABLED
        btn2['state'] = NORMAL
        viewList()


def addInfo():
    global infos
    print(i1.get(), i2.get(), i3.get(), i4.get())
    info = student(i1.get(), i2.get(), i3.get(), i4.get())
    infos.append(info)
    viewList()


def deleteInfo(info):
    global infos
    infos.remove(info)
    viewList()


def updateInfo(info):
    i1.delete(0, 'end')
    i2.delete(0, 'end')
    i3.delete(0, 'end')
    i4.delete(0, 'end')
    i1.insert(0, info.getName())
    i2.insert(0, info.getsection())
    i3.insert(0, info.getcourse())
    i4.insert(0, info.getnumber())
    btn1['state'] = NORMAL
    btn2['state'] = DISABLED

    btn1.configure(command=lambda: info.updateSelf(i1.get(), i2.get(), i3.get(), i4.get()))


def viewList():
    global infos

    row = 1
    list = separator.grid_slaves()
    for l in list:
        l.destroy()

    addHeaders()
    for info in infos:
        Label(separator, text=info.getName(), background=color, width=10).grid(row=row, column=0, sticky= W, padx=10, pady=5)
        Label(separator, text=info.getsection(), background=color, width=10).grid(row=row, column=1,
                                                                                  sticky=W , padx=10, pady=5)
        Label(separator, text=info.getcourse(), background=color, width=10).grid(row=row, column=2,
                                                                                 sticky=W, padx=10, pady=5)
        Label(separator, text=info.getnumber(), background=color, width=10).grid(row=row, column=3,
                                                                                 sticky=W, padx=10, pady=5)
        btn_a1 = Button(separator, text="Update the List", width=15, command=lambda: updateInfo(info))
        btn_a2 = Button(separator, text="Delete the List", width=15, command=lambda: deleteInfo(info))

        btn_a1.grid(row=row, column=5, sticky=W, padx=2, pady=5)
        btn_a2.grid(row=row, column=6, sticky=E, padx=2, pady=5)
        row += 1

    i1.delete(0, 'end')
    i2.delete(0, 'end')
    i3.delete(0, 'end')
    i4.delete(0, 'end')


def addHeaders():
    separator.grid(row=15, column=0, columnspan=3, padx=10, pady=5, sticky=W + E + N + S)
    Label(separator, text="Student's Name", background=color, width=20).grid(row=0, column=0, sticky=W + E + N + S, padx=10, pady=5)
    Label(separator, text="Student's Section", background=color, width=20).grid(row=0, column=1, sticky=W + E + N + S,
                                                                                padx=10, pady=5)
    Label(separator, text="Student's Course", background=color, width=20).grid(row=0, column=2, sticky=W + E + N + S,
                                                                               padx=10, pady=5)
    Label(separator, text="Student's Student Number", background=color, width=20).grid(row=0, column=3,
                                                                                       sticky=W + E + N + S,
                                                                                       padx=10, pady=5)
    Label(separator, text="What would you like to do?", background=color, width=50).grid(row=0, column=4, sticky=W + E + N + S, padx=10,
                                                                     pady=5, columnspan=2)

products = []
color = "#d9d7d7"

root = Tk()
root.title("Student List")
root.configure(bg='orange')
root.geometry("1400x900")
root.resizable(0, 0)
std = StringVar()
std.trace('w', limit_student_number)

Label(root, text="Student's Information").grid(row=0, column=0, sticky=W, padx=5, pady=2)
Label(root, text="Student's Name: ").grid(row=1, column=0, sticky=W, padx=5, pady=2)
Label(root, text="Student's Section: ").grid(row=2, column=0, sticky=W, padx=5, pady=2)
Label(root, text="Student's Course: ").grid(row=1, column=2, sticky=W, padx=5, pady=2)
Label(root, text="Student's Student Number: ").grid(row=2, column=2, sticky=W, padx=5, pady=2)

i1 = Entry(root, width=20)
i2 = Entry(root, width=20)
i3 = Entry(root, width=20)
i4 = Entry(root, width=20, textvariable=std)

i1.grid(row=1, column=1, sticky=W, padx=10, pady=5)
i2.grid(row=2, column=1, sticky=W, padx=10, pady=5)
i3.grid(row=1, column=3, sticky=W, padx=10, pady=2)
i4.grid(row=2, column=3, sticky=W, padx=10, pady=2)

val1 = root.register(validationlet)
i1.config(validate="key", validatecommand=(val1, '%P'))
i3.config(validate="key", validatecommand=(val1, '%P'))

val2 = root.register(validationnum)
i4.config(validate="key", validatecommand=(val2, '%P'))

btn1 = Button(root, text="Update Information", width=15, state=DISABLED)
btn2 = Button(root, text="Add Information", width=15, state=NORMAL, command=addInfo)

btn1.grid(row=10, column=1, sticky=W, padx=10, pady=5)
btn2.grid(row=10, column=2, sticky=E, padx=10, pady=5)

separator = Frame(root, height=100, width=420, background=color, relief=SUNKEN)

addHeaders()
root.mainloop()
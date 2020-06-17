import tkinter

window = tkinter.Tk()
window.title("Ubishot")

def update_label():
    tkinter.Label(window,text = "Please enter a valid directory").grid(row = 4, column = 4)

tkinter.Label(window,text = "Please enter directory: ").grid(row=0, column = 4)
tkinter.Entry(window).grid(row = 2, column = 4)
tkinter.Button(window,text = "Change", command = update_label ).grid(row = 3, column = 3)





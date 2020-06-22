import tkinter
window = tkinter.Tk()
window.title("Ubishot")

def update_label():
    tkinter.Label(window,text = "Please enter a valid directory").grid(row = 4, column = 4)

def retrieve_input():
    inputValue = textBox.get()
    print(inputValue)

tkinter.Label(window,text = "Please enter directory: ").grid(row=0, column = 4)
textBox = tkinter.Entry(window)
textBox.grid(row = 2, column = 4)
tkinter.Button(window,text = "Change", command = retrieve_input ).grid(row = 3, column = 3)


window.mainloop()





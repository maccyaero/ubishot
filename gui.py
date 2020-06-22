import tkinter,os,sys
window = tkinter.Tk()
window.title("Ubishot")

def update_label():
    tkinter.Label(window,text = "Please enter a valid directory").grid(row = 4, column = 4)

def validate():
    inputValue = textBox.get()
    print(inputValue)
    directory = inputValue
    isDirectory = os.path.isdir(directory) #imported methos from OS module to check if entered directory is valid
    print(isDirectory)

    if isDirectory == False:
        update_label()
    else:
        change_directory(directory)


def change_directory(dir):
    command = "defaults write com.apple.screencapture location " #Shell Coomad to change default screenshot location
    command += dir #Appending the user entered directory to the command used to change screesnshot location
    print("The final command passing to cli is : " + command)
    os.system(command) #Runs the command on the shell.


tkinter.Label(window,text = "Please enter directory: ").grid(row=0, column = 4)
textBox = tkinter.Entry(window)
textBox.grid(row = 2, column = 4)
tkinter.Button(window,text = "Change", command = validate ).grid(row = 3, column = 3)


window.mainloop()





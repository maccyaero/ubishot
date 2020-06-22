import os,sys,gui

def validate():
    inputValue = gui.textBox.get()
    print(inputValue)
    directory = inputValue
    isDirectory = os.path.isdir(directory) #imported methos from OS module to check if entered directory is valid

    if isDirectory == False:
        gui.update_label
    else:
        change_directory(directory)


def change_directory(dir):
    command = "defaults write com.apple.screencapture location " #Shell Coomad to change default screenshot location
    command += dir #Appending the user entered directory to the command used to change screesnshot location
    print("The final command passing to cli is : " + command)
    os.system(command) #Runs the command on the shell.

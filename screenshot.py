import os,sys

command = "defaults write com.apple.screencapture location " #Shell Coomad to change default screenshot location

while True:
    directory = input("Enter the directory: ")
    isDirectory = os.path.isdir(directory) #imported methos from OS module to check if entered directory is valid

    if directory =='q': #user can press q to exit the program.
        sys.exit()

    if isDirectory == False:
        print('Please enter a valid directory or press q to exit.')
    else:
        break

command += directory #Appending the user entered directory to the command used to change screesnshot location
print("The final command passing to cli is : " + command)
os.system(command) #Runs the command on the shell.

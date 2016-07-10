import webbrowser
import time

####def openPage():
    ##time.sleep(10)
    ###webbrowser.open("http://www.google.co.ke")

###openPage()

##How to open a file using python
def open_file():
    file = open("C:\Users\Pum\Downloads\Windows 10 keys.txt")
    content = file.read()
    print(content)
    
open_file()

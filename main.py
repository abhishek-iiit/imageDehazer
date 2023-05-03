#importing the Libraries
import image_dehazer
import numpy as np
import PIL                      # Python Imaging Library
from tkinter import filedialog  # Used to provide GUI open/save feature
from tkinter import *
from PIL import Image,ImageTk   # used for handling image type file

#defining the Window
window = Tk()
window.geometry('1280x832')
window.resizable(0, 0)
window.title("Image Dehazer")
image=Image.open("_bg_.jpg")
photo=ImageTk.PhotoImage(image)
lab=Label(image=photo,bg='#8fb5c2')
lab.pack()

#Defining the Labels
message = Label(window, text="Image Dehazer" ,bg="#000000"  ,fg="#FFFF00"  ,width=50  ,height=3,font=('Helvetica', 35, 'italic bold '))
message.place(x=60, y=10)
message = Label(window, text="" ,bg="grey"  ,fg="black"  ,width=50  ,height=12, activebackground = "yellow" ,font=('Helvetica', 20 , ' bold ')) 
message.place(x=150, y=170)

def mainFunct():
        # provides a dialog box for asking file to open and returns it's path
        window.filename =  filedialog.askopenfilename()
        image_file= PIL.Image.open(window.filename)
        img = np.array(image_file)
        
        # Remove haze from image
        HazeCorrectedImg, haze_map = image_dehazer.remove_haze(img, showHazeTransmissionMap=False)
        output_image = Image.fromarray(HazeCorrectedImg)
                
        #Open video to save file
        window.filename =  filedialog.asksaveasfilename()
        output_image.save(window.filename+ '.jpg')
        Saved_Image = "Saved"
        message.configure(text= Saved_Image)

#Defining the buttons
funct = Button(window, text="ImageDehazer", command=mainFunct  ,fg="red"  ,bg="white"  ,width=20  ,height=3, activebackground = "grey" ,font=('Helvetica', 15 , ' bold '))
funct.place(x=1000, y=170)
quitWindow = Button(window, text="Quit", command=window.destroy  ,fg="red"  ,bg="white"  ,width=17  ,height=2, activebackground = "grey" ,font=('Helvetica', 15 , ' bold '))
quitWindow.place(x=1060, y=760)

window.mainloop()

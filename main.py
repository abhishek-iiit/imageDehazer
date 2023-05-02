import cv2
import image_dehazer
import os
import numpy as np
#importing the Libraries
from gtts import gTTS           # used for converting text to speech
import PIL                      # Python Imaging Library
import gtts                     # Google's text to Speech API
import pytesseract              # used for image to text conversion using OCR
from tkinter import filedialog  # Used to provide GUI open/save feature
from tkinter import *
from PIL import Image,ImageTk   # used for handling image type file
import pyperclip

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

def mainFunct():
        window.filename =  filedialog.askopenfilename()
        # provides a dialog box for asking file to open and returns it's path
        image_file= PIL.Image.open(window.filename)  
        
        
        # Read input image
        image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
        
        # Remove haze from image
        HazeCorrectedImg, haze_map = image_dehazer.remove_haze(image, showHazeTransmissionMap=False)

        # Save the output image to a file
        output_path = "outputImages/result.png"
        cv2.imwrite(output_path, HazeCorrectedImg)

#Defining the buttons
funct = Button(window, text="ImageDehazer", command=mainFunct  ,fg="red"  ,bg="white"  ,width=20  ,height=3, activebackground = "grey" ,font=('Helvetica', 15 , ' bold '))
funct.place(x=1000, y=170)
quitWindow = Button(window, text="Quit", command=window.destroy  ,fg="red"  ,bg="white"  ,width=17  ,height=2, activebackground = "grey" ,font=('Helvetica', 15 , ' bold '))
quitWindow.place(x=1060, y=760)

window.mainloop()

import math
from tkinter import *
from tkinter.colorchooser import askcolor
from PIL import Image
from pyscreenshot import grab
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter.font import Font
from pathlib import Path
import img2pdf
import os
import sys
import playsound
import webbrowser

import random

root = Tk()
DEFAULT_COLOR = 'black'
color = DEFAULT_COLOR
mousePosX = 0
mousePosY = 0

def motion(event):
    x, y = event.x, event.y


def showxy(event):
    global mousePosX
    global mousePosY
    mousePosX = event.x
    mousePosY = event.y

def openfile():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Open Sound File",
                                          filetypes=(("MP3 Files", "*.mp3"),
                                                     ("WAV Files", "*.wav")))
    return filename

class popupWindow(object):
    def __init__(self, master, label):
        top=self.top=Toplevel(master)
        self.l=Label(top, text=label)
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()

class Window(Frame):
    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'
    DEFAULT_TEXT_SIZE = 12

    global color
    global textsize
    color = DEFAULT_COLOR
    textsize = DEFAULT_TEXT_SIZE

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom

    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.master = master

        # Create slideArea inside of Frame
        self.slide = Canvas(self, width=math.ceil(650/900*screenWidth),
                            height=math.ceil(400/600*screenHeight), bg="white", highlightbackground="grey")
        self.slide.place(x=math.ceil(125/900*screenWidth), y=math.ceil(150/600*screenHeight))
        self.slide.x = math.ceil(125/900*screenWidth)
        self.slide.y = math.ceil(150/600*screenHeight)
        self.slide.width = math.ceil(650/900*screenWidth)
        self.slide.height = math.ceil(400/600*screenHeight)
        self.slide.update()

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # Crate grey banner behind buttons
        self.banner = Canvas(self, width=screenWidth, height=math.ceil(screenHeight/6), bg="grey")
        self.banner.pack(side=TOP)

        # create button, link it to clickExitButton()
        standardHeight = math.ceil(screenHeight / 600)
        standardWidth = math.ceil((5 / 900) * screenWidth)
        exitButton = Button(self, text="Exit", command=self.clickExitButton, height=standardHeight, width=standardWidth)

        # buttons
        saveButton = Button(self, text="Save", command=self.saveScreenShot,height=standardHeight, width=standardWidth)
        loadButton = Button(self, text="Load", height=standardHeight, width=standardWidth)
        colorButton = Button(self, text="Color", command=self.chooseColor, height=standardHeight, width=standardWidth)
        self.brushButton = Button(self, text="Pen", command=self.use_pen, height=standardHeight, width=standardWidth)
        latexButton = Button(self, text="LaTex", height=standardHeight, width=standardWidth)
        presentButton = Button(self, text="Present", height=standardHeight, width=math.ceil((12/900) * screenWidth))

        imageButton = Button(self, text="Image", command=self.upload_image, height=standardHeight, width=standardWidth)
        linkButton = Button(self, text="Links", command=self.linker, height=standardHeight, width=standardWidth)
        soundButton = Button(self, text="Sound", command=self.playSound, height=standardHeight, width=math.ceil(6/900 * screenWidth))

        textButton = Button(self, text="Text", command=self.type_text, height=standardHeight, width=standardWidth)

        codeButton = Button(self, text="Code", height=standardHeight, width=standardWidth)
        txtsizeButton = Button(self, text="Text Size", command=self.textSize, height=standardHeight, width=math.ceil((6/900) * screenWidth))

        newSlide = Button(self, text="New Slide", height=standardHeight, width=math.ceil(17/900*screenWidth))
        numSlide = Button(self, text="Number Slides", height=standardHeight, width=math.ceil(17/900*screenWidth))
        remSlide = Button(self, text="Remove Current Slide", height=standardHeight, width=math.ceil(17/900*screenWidth))

        slideColor = Button(self, text="Set Slide Color",
                            command=self.slide_color, height=standardHeight, width=math.ceil(12/900*screenWidth))

        # text
        font = ["Times New Roman", "Comic Sans MS", "Bradley Hand ITC", "Broadway", "Brush Script MT"]
        self.defFont = StringVar(master)
        self.defFont.set(font[0])  # default value
        fontButton = OptionMenu(self, self.defFont, *font)
        fontButton.place(x=math.ceil(480/900*screenWidth), y=math.ceil(65/600*screenHeight))

        # place buttons
        # button columns
        newSlide.place(x=math.ceil(240/900*screenWidth), y=math.ceil(4/600*screenHeight))
        numSlide.place(x=math.ceil(400/900*screenWidth), y=math.ceil(4/600*screenHeight))
        remSlide.place(x=math.ceil(550/900*screenWidth), y=math.ceil(4/600*screenHeight))

        presentButton.place(x=math.ceil(280/900*screenWidth), y=math.ceil(35/600*screenHeight))
        slideColor.place(x=math.ceil(380/900*screenWidth), y=math.ceil(35/600*screenHeight))
        textButton.place(x=math.ceil(480/900*screenWidth), y=math.ceil(35/600*screenHeight))
        self.brushButton.place(x=math.ceil(530/900*screenWidth), y=math.ceil(35/600*screenHeight))
        colorButton.place(x=math.ceil(580/900*screenWidth), y=math.ceil(35/600*screenHeight))

        codeButton.place(x=math.ceil(233 / 900 * screenWidth), y=math.ceil(67 / 600 * screenHeight))
        imageButton.place(x=math.ceil(280 / 900 * screenWidth), y=math.ceil(67 / 600 * screenHeight))
        soundButton.place(x=math.ceil(327 / 900 * screenWidth), y=math.ceil(67 / 600 * screenHeight))
        linkButton.place(x=math.ceil(380 / 900 * screenWidth), y=math.ceil(67 / 600 * screenHeight))
        txtsizeButton.place(x=math.ceil(427 / 900 * screenWidth), y=math.ceil(67 / 600 * screenHeight))
        latexButton.place(x=math.ceil(627 / 900 * screenWidth), y=math.ceil(67 / 600 * screenHeight))

        # Top right corner buttons
        exitButton.place(x=math.ceil(850 / 900 * screenWidth), y=math.ceil(4 / 600 * screenHeight))
        saveButton.place(x=math.ceil(800 / 900 * screenWidth), y=math.ceil(4 / 600 * screenHeight))
        loadButton.place(x=math.ceil(850 / 900 * screenWidth), y=math.ceil(35 / 600 * screenHeight))

        self.slide.bind('<Button>', showxy)

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.brushButton

    def clickExitButton(self):
        exit()

    def chooseColor(self):
        global color  # set color to global so it updates in other function
        col = askcolor()
        color = col[1]

    def use_pen(self):
        self.paint()

    def paint(self, event):
        self.line_width = 5

        global color
        paint_color = color
        if self.old_x and self.old_y:
            self.slide.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


    def upload_image(self):
        file_path = filedialog.askopenfilename()
        photo = ImageTk.PhotoImage(file=file_path)

        global mousePosX
        global mousePosY
        x = mousePosX
        y = mousePosY

        self.slide.create_image(x, y, image=photo, anchor=NW)
        img = Label(image=photo)
        img.image = photo  # reference to image

    def linker(self):
        self.popup("Input Search Term:")
        webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % self.entryValue())

    def type_text(self):
        fontChoice = self.defFont.get()
        global color
        global textsize

        self.popup("Input text")

        global mousePosX
        global mousePosY
        x = mousePosX
        y = mousePosY

        font = Font(family=fontChoice, size=textsize)
        self.slide_id = self.slide.create_text(x, y, anchor="nw", font=font, fill=color)

        self.slide.itemconfig(self.slide_id, text=self.entryValue())

    def textSize(self):
        self.popup("Input text size")
        global textsize
        textsize = int(self.entryValue())

    def popup(self, label):
        self.w = popupWindow(self.master, label)
        self.master.wait_window(self.w.top)

    def entryValue(self):
        return self.w.value

    def slide_color(self):
        global color
        self.slide.configure(bg=color)

    def playSound(self):
        file = openfile()
        button = self.slide.create_rectangle(10, 10, 100, 30, fill="grey40", )
        self.slide.tag_bind(button, "<Button-1>", playsound.playsound(file, True))

    def saveScreenShot(self):
        x = self.slide.x
        y = self.slide.y
        # the 4 here is because of the border the Canvas has
        im = grab(bbox=(self.slide.x, self.slide.y, x+self.slide.width+4, y+self.slide.height+4))

        indexPath = Path(__file__).parent / "Screenshots/index.txt"

        # Check to see if the index File exists
        if not Path.exists(indexPath):
            indexFile = open(indexPath, "w")
            indexFile.write(str(1))  # Create Index File
            index = 1
        else:
            indexFile = open(indexPath, "r+")
            index = indexFile.readline()
            index = int(index)
            index = index + 1

            # Update Index File
            indexFile.close()
            indexFile = open(indexPath, "w")
            indexFile.close()
            indexFile = open(indexPath, "r+")
            indexFile.write(str(index))

        # Save Image
        tempString1 = "Screenshots/slide%s.jpeg" % index
        im.save(tempString1, "JPEG")
        imagePath = Path(__file__).parent / tempString1

        # Making PDF
        tempString2 = "PDFs/PDF%s.pdf" % (index)
        pdfPath = Path(__file__).parent / tempString2
        pdfFile = open(pdfPath, "wb")
        savedImage = Image.open(imagePath)
        pdfBytes = img2pdf.convert(savedImage.filename)
        pdfFile.write(pdfBytes)

        # Close all Files
        indexFile.close()
        pdfFile.close()
        savedImage.close()

        # Potential Fix, change grab resolution to accomdate scaled elements
        '''
        img = grab(bbox=(100, 200, 300, 400))
        # to keep the aspect ratio
        w = 300
        h = 400
        maxheight = 600
        maxwidth = 800
        ratio = min(maxwidth/width, maxheight/height)
        # correct image size is not #oldsize * ratio#
        # img.resize(...) returns a resized image and does not effect img unless
        # you assign the return value
        img = img.resize((h * ratio, width * ratio), Image.ANTIALIAS)
        '''

def paint(event):
    global color
    paint_color = color

    #def savePDF(self):



# Set FullScreen
root.attributes("-fullscreen", True)

# Save Screen Resolution
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

app = Window(root)
print(f"Screen Width: {screenWidth}, Screen Height: {screenHeight}")

# set window title
root.wm_title("Slides")
root.bind('<Motion>', paint)
app.configure(background="black")


# show window
root.mainloop()

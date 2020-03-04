from tkinter import *
from tkinter.colorchooser import askcolor

root = Tk()

class Window(Frame):
    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    global canvas
    canvas = Canvas(root, width=900, height=500)
    canvas.pack()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create button, link it to clickExitButton()
        exitButton = Button(self, text="Exit", command=self.clickExitButton, height=1, width=5)

        # buttons
        saveButton = Button(self, text="Save", height=1, width=5)
        loadButton = Button(self, text="Load", height=1, width=5)
        colorButton = Button(self, text="Color", command=self.chooseColor, height=1, width=5)
        brushButton = Button(self, text="Pen", command=self.paint, height=1, width=5)
        latexButton = Button(self, text="LaTex", height=1, width=5)
        presentButton = Button(self, text="Present", height=1, width=5)

        imageButton = Button(self, text="Image", height=1, width=5)
        linkButton = Button(self, text="Links", height=1, width=5)
        soundButton = Button(self, text="Sound", height=1, width=6)

        textButton = Button(self, text="Text", height=1, width=5)
        codeButton = Button(self, text="Code", height=1, width=5)
        txtsizeButton = Button(self, text="Text Size", height=1, width=6)

        newSlide = Button(self, text="New Slide", height=1, width=17)
        numSlide = Button(self, text="Number Slides", height=1, width=17)
        remSlide = Button(self, text="Remove Current Slide", height=1, width=17)

        # text
        font = ["Times New Roman", "Bengali", "Comic Sans"]
        variable = StringVar(master)
        variable.set(font[0])  # default value
        fontButton = OptionMenu(master, variable, *font)
        fontButton.place(x=55, y=568)

        # place buttons
        # button columns
        brushButton.place(x=0, y=4)
        colorButton.place(x=0, y=35)
        latexButton.place(x=0, y=67)

        textButton.place(x=50, y=4)
        codeButton.place(x=50, y=35)

        imageButton.place(x=100, y=4)
        linkButton.place(x=100, y=35)

        soundButton.place(x=150, y=4)
        txtsizeButton.place(x=150, y=35)

        newSlide.place(x=210, y=4)
        numSlide.place(x=210, y=35)
        remSlide.place(x=210, y=67)

        # bottom right corner buttons
        exitButton.place(x=850, y=4)
        saveButton.place(x=800, y=4)
        loadButton.place(x=800, y=35)
        presentButton.place(x=850, y=35)

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
        self.color = askcolor(color=self.color)[1]

    def paint(self, event):
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y


app = Window(root)

# set window title
root.wm_title("Slides")
root.geometry("900x600")
app.configure(background="grey")

# canvas.create_rectangle(50, 0, 100, 50, fill='red')

# show window
root.mainloop()

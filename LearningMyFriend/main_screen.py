from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.uix.image import Image
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window

# use kivy_venv\Scripts\activate first, when in the folder
# must be ran through command line b/c otherwise kivy refuses to admit that it exists

# sets up canvas + colors
color = (random(), 1, 1)
Window.clearcolor = (0.412, 0.412, 0.412, 1)


# drawing with a super basic pen tool b/c thats all this program is good for right now
class Paint(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            Color(*color, mode='hsv')
            d = 1.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

    def draw_screen(self):
        with self.canvas:
            Color(1, 1, 1, 1)
            Rectangle(pos=(220, 25), size=(550, 450))

# button functions + windows
class Slides(App):

    def build(self):
        parent = Widget()
        self.painter = Paint()

        self.painter.draw_screen()

        # latex button (currently bound to the clear screen function because right now this is a glorified drawing app)
        latex = Button(text='LaTex', pos=(parent.x, parent.height+400))
        latex.bind(on_release=self.clear_canvas)

        #image button
        insertImg = Button(text='Insert Image', pos=(parent.x + 100, parent.height + 400))
        insertImg.bind(on_release=self.insert_image)

        # pen tool, currently just changes the color of the pen randomly
        pen = Button(text='Pen Tool', pos=(parent.x + 200, parent.height+400))
        pen.bind(on_release=self.color_pick)

        # insert link
        link = Button(text='Insert Link', pos=(parent.x + 300, parent.height + 400))

        # number slides
        numSlides = Button(text='Number Slides', pos=(parent.x + 400, parent.height + 400))

        # dropdown button for the text options
        dropdown = DropDown()
        for index in range(1):
            txtbtn = Button(text='Change Font Size', size_hint_y=None, height=44)
            txtbtn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(txtbtn)

            txtbtn = Button(text='Change Font Color', size_hint_y=None, height=44)
            txtbtn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(txtbtn)
        textOpt = Button(text='Text Options', size_hint=(None, None), pos=(parent.x + 500, parent.height + 400))
        textOpt.bind(on_release=dropdown.open)

        # insert sound button, no functionality yet
        sound = Button(text='Insert Sound', pos=(parent.x + 600, parent.height + 400))

        # insert code, no functionality yet
        code = Button(text='Insert Code', pos=(parent.x + 700, parent.height + 400))

        # displays the buttons on the screen. if we need to add more, then just extend the list with the button name
        widgets = [self.painter, latex, insertImg, pen, link, numSlides, textOpt, sound, code]
        for x in widgets:
            parent.add_widget(x)
        return parent

    #  function calls
    # clears canvas
    def clear_canvas(self, obj):
        self.painter.canvas.clear()
        self.painter.draw_screen()

    # color picks
    def color_pick(self, obj):
        global color
        self.col = (random(), 1, 1)
        color = self.col
    # insert image function, doesn't work yet
    def insert_image(selfself, obj):
        img = Image(source='fennec.jpg')
        img.pos = (0, 0)

        s = Widget()
        s.add_widget(img)

        return s



if __name__ == '__main__':
    Slides().run()

from tkinter import filedialog
import playsound


def openfile():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Open Sound File",
                                          filetypes=(("MP3 Files", "*.mp3"),
                                                     ("WAV Files", "*.wav")))
    return filename


def playSound(self):
        file = openfile()
        button = self.slide.create_rectangle(10, 10, 100, 30, fill="grey40", )
        self.slide.tag_bind(button, "<Button-1>", playsound.playsound(file, True))

from tkinter import *
from PIL import ImageTk, Image
from time import sleep
from googletrans import Translator

app = Tk()
app.overrideredirect(True)
app.wm_attributes('-topmost', False)
app.wm_attributes('-disabled', False)
app.wm_attributes('-transparentcolor', 'white')
app.title('Tortuga Translat')
app.geometry('756x560')
"""app2 = Toplevel(app)"""

msg = StringVar()


def quitSoftware(event):
    sleep(0.2)
    app.destroy()


def button_translat(event):
    translat(msg.get())


def translat(txt):

    """Used version pip3 install googletrans==3.1.0a0"""
    translator = Translator()
    translation = translator.translate(txt, dest='pt')
    msg1 = f'{translation.origin} origin ({translation.src})\n ' \
           f'translat to ({translation.dest}) {translation.text}\n'
    labelText.config(labelText, text=msg1.upper())


# Canvas init
canvas = Canvas(
    app, width=756, height=560, bd=0, highlightthickness=0, relief='ridge'
)
canvas.pack()
bgImg = ImageTk.PhotoImage(Image.open('img/Layout.png'))
bg = canvas.create_image(0, 0, image=bgImg, anchor=NW)

# Button Exit
buttonExImg = ImageTk.PhotoImage(Image.open('img/ButtonExit.png'))
buttonExit = canvas.create_image(50, 500, image=buttonExImg)
canvas.tag_bind(buttonExit, '<Button-1>', quitSoftware)

# Button Translate
buttonTranslateImg = ImageTk.PhotoImage(Image.open('img/ButtonTranslate.png'))
buttonTranslate = canvas.create_image(400, 250, image=buttonTranslateImg)
canvas.tag_bind(buttonTranslate, '<Button-1>', button_translat)

# Entry

entryImg = ImageTk.PhotoImage(Image.open('img/Entry.png'))
entryIm = canvas.create_image(400, 100, image=entryImg)
entry = Entry(
    app,
    font=('Helvetica', 24),
    width=8,
    textvariable=msg,
    bg='#000000',
    fg='#F2F2F2',
    bd=0,
    highlightcolor='blue',
)
entryy = canvas.create_window(
    200, 56, anchor='nw', window=entry, width=400, height=85
)

# Label Text
labelText = Label(
    app,
    font=('Hevetica', 15),
    bg='#000000',
    fg='#F2F2F2',
    highlightcolor='blue',
)
labelText1 = canvas.create_window(10, 356, anchor='nw', window=labelText)


app.mainloop()

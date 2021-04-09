import requests
from tkinter import *
from PIL import Image, ImageTk
import urllib
from tkinter import ttk
from googletrans import Translator

def get_full_code():
    translator = Translator()
    date = time_field.get()
    params = {'date': date}
    url = 'https://api.nasa.gov/planetary/apod?api_key=lvW1QUIKXrFXeALxXsv3RqXEiipgtvPNlpK3VnEa'
    output = requests.get(url, params=params)
    data = output.json()
    result = translator.translate(data['explanation'], src='en', dest='ru')
    info_text.delete(1.0, END)
    info_text.insert(1.0, result.text)
    r = urllib.request.urlopen(data['url'])
    with open("thumb.png", "wb") as f:
        f.write(r.read())
    img = Image.open('thumb.png')
    img = img.resize((320, 320), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    panel.config(image = photo)
    panel.image = photo

root = Tk()
root.geometry('960x480')
root.resizable(0,0)

time_help = ttk.Label(root, text = 'Введите данные в формате ГГГГ-ММ-ДД')
time_field = ttk.Entry(root, width = 40)
time_button = ttk.Button(root, text = 'Получить данные', command = get_full_code)
time_help.place(relx=0, y=0)
time_field.place(relx=0.5, y=0, anchor=N)
time_button.place(relx=1, y=0, anchor=NE)

info_text = Text(root, height = 20)
info_text.insert(1.0, 'Здесь появится информация.')
info_text.place(x=0, rely=0.5, width=640, anchor=W)

panel = ttk.Label()
panel.place(x=640, rely=0.5, anchor=W)

root.mainloop()

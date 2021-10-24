import requests
import json
from tkinter import *
import tkinter.ttk
import os
from PIL import Image, ImageTk
extension =""
params = {'p': '9431'}
response = requests.get('https://api.thecatapi.com/v1/images/search',
            params=params)
CatResponse = response.json()
print(CatResponse[0]["url"])



if (CatResponse[0]["url"]).find("jpg") > -1:
    extension = "jpg"
elif (CatResponse[0]["url"]).find("gif") > -1:
    extension = "gif"
elif (CatResponse[0]["url"]).find("png") > -1:
    extension = "png"

with open('Cat.'+extension, 'wb') as handle:
        response2 = requests.get(CatResponse[0]["url"], stream=True)

        if not response2.ok:
            print ("oof")

        for block in response2.iter_content(1024):
            if not block:
                break   

            handle.write(block)


root = Tk()
root.title("Title")
root.geometry('1000x1000')

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

image = Image.open(os.getcwd()+"\\Cat."+extension)
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = tkinter.ttk.Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)

root.mainloop()

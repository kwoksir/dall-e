import os
import openai
from tkinter import *
import requests
from io import BytesIO
from PIL import Image, ImageTk

root = Tk()
root.title("Show Image Demo")
root.geometry("820x600+0+0")
root.configure(bg="grey90")


#openai.api_key = os.getenv("OPENAI_API_KEY")
p = input("Enter your prompt: ")

response = openai.Image.create(
  prompt=p ,
  n=1,
  size="512x512"
)
image_url = response['data'][0]['url']

response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
imgtk = ImageTk.PhotoImage(img)
label = Label(root,image=imgtk, width=800)
label.pack()
btn = Button(root, text="Close", width=20,command=root.destroy)
btn.pack()
root.mainloop()

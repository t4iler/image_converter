import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
canvas01 = tk.Canvas(root, width=450, height=400, bg='azure3', relief='raised')
canvas01.pack()

labl = tk.Label(root, text='Image Converter', bg='azure3')
labl.config(font=('georgia', 30))
canvas01.create_window(240, 150, window=labl)

def PNG():
    global iml
    import_file_path = filedialog.askopenfilename()
    iml = Image.open(import_file_path)

browse_png = tk.Button(text='Select PNG file', command=PNG, bg='royalblue', fg='black', font=('georgia', 14, 'bold'))
canvas01.create_window(230, 220, window=browse_png)

def convert():
    global iml
    export_file_path = filedialog.asksaveasfilename(defaul='.jpg')
    iml.save(export_file_path)

savebutton = tk.Button(text = 'Convert PNG to JPG', command=convert, bg='royalblue', fg='black', font=('georgia', 14, 'bold'))
canvas01.create_window(230, 270, window=savebutton)
root.mainloop()

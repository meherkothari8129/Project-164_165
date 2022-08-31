from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import filedialog 

root = Tk()
root.title("Image Viewer")
root.geometry("500x500")
root.config(bg="black")

label_image = Label(root, bg = "white", highlightthickness=5)
label_image.place(relx = 0.5,rely = 0.5, anchor = CENTER)

img_path = ""

def OpenImage():
    global img_path
    img_path = filedialog.askopenfilename(title = "Open Image file",filetypes = [("Image files","*.jpg *.gif *.png *.jpeg")])
    print(img_path)
    im = Image.open(img_path)
    img = ImageTk.PhotoImage(im)
    label_image["image"] = img
    img.close()
    
def RotateImage():
    global img_path
    im = Image.open(img_path)
    img = ImageTk.PhotoImage(im.rotate(180))
    label_image["image"] = img
    img.close()
    
    
btn = Button(root, text = "Open Image",bg = "gray",fg = "white", command=OpenImage)
btn.place(relx = 0.5, rely=0.1, anchor=CENTER)

btn1 = Button(root, text = "Rotate Image",bg = "gray", fg = "white", command = RotateImage)
btn1.place(relx = 0.5, rely = 0.9, anchor = CENTER)

root.mainloop()

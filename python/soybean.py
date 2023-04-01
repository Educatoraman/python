from tkinter import *
from PIL import Image,ImageTk

class soy_info:
    def __init__(self,root):
      self.root=root
      self.root.title("SOYBEAN")
      self.root.geometry("1000x650+0+0")

      img1=Image.open(r"C:\Users\hp\Desktop\python\image\soybeani.jpg")
      img1=img1.resize((400,450),Image.ANTIALIAS)
      self.photoimg1=ImageTk.PhotoImage(img1)

      lbl=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
      lbl.place(x=300,y=100,width=450,height=550)

      img2=Image.open(r"C:\Users\hp\Desktop\python\image\soybean.jpg")
      img2=img2.resize((350,450),Image.ANTIALIAS)
      self.photoimg2=ImageTk.PhotoImage(img2)

      lbl=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
      lbl.place(x=25,y=125,width=250,height=250)


if __name__=="__main__":
    root = Tk()
    obj=soy_info(root)
    root.mainloop()

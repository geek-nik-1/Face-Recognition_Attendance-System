from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        title_lbl= Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)   

        img_top = Image.open(r"D:\Mini Project\imAGES\Programming.jpeg")
        img_top = img_top.resize((1530, 720))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_top1 = Image.open(r"D:\Mini Project\imAGES\Dhiraj-removebg-preview (1).png")
        img_top1 = img_top1.resize((250, 250))
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl1 = Label(main_frame, image=self.photoimg_top1)
        f_lbl1.place(x=250, y=0, width=250, height=250)

        name_frame1 = Frame(main_frame, bg="blue")
        name_frame1.place(x=250, y=255, width=250, height=30)
        name_label1 = Label(name_frame1, text="Dhiraj Patil", font=("times new roman", 14), bg="blue", fg="white")
        name_label1.pack(fill="both", expand=True)

        img_top2 = Image.open(r"D:\Mini Project\imAGES\Nikhil.png")
        img_top2 = img_top2.resize((250, 250))
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)

        f_lbl2 = Label(main_frame, image=self.photoimg_top2)
        f_lbl2.place(x=0, y=0, width=250, height=250)

        name_frame2 = Frame(main_frame, bg="blue")
        name_frame2.place(x=0, y=255, width=250, height=30)
        name_label2 = Label(name_frame2, text="Nikhil Khot", font=("times new roman", 14), bg="blue", fg="white")
        name_label2.pack(fill="both", expand=True)


        img_top3 = Image.open(r"D:\Mini Project\imAGES\pranav-removebg-preview (1).png")
        img_top3 = img_top3.resize((250, 250))
        self.photoimg_top3 = ImageTk.PhotoImage(img_top3)

        f_lbl3 = Label(main_frame, image=self.photoimg_top3)
        f_lbl3.place(x=0, y=300, width=250, height=250)

        name_frame3 = Frame(main_frame, bg="blue")
        name_frame3.place(x=0, y=555, width=250, height=30)
        name_label3 = Label(name_frame3, text="Pranavsinh Rajput", font=("times new roman", 14), bg="blue", fg="white")
        name_label3.pack(fill="both", expand=True)

        img_top4 = Image.open(r"D:\Mini Project\imAGES\pratik-removebg-preview (1).png")
        img_top4 = img_top4.resize((250, 250))
        self.photoimg_top4 = ImageTk.PhotoImage(img_top4)

        f_lbl4 = Label(main_frame, image=self.photoimg_top4)
        f_lbl4.place(x=250, y=300, width=250, height=250)

        name_frame4 = Frame(main_frame, bg="blue")
        name_frame4.place(x=250, y=555, width=250, height=30)
        name_label4 = Label(name_frame4, text="Pratik Bagul", font=("times new roman", 14), bg="blue", fg="white")
        name_label4.pack(fill="both", expand=True)







if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
from tkinter import *
from tkinter import ttk
import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk
from student import Student 
import os
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from developer import Developer
from help import Help 

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        # First image
        img = Image.open(r"D:\Mini Project\imAGES\clg_logo.jpg")
        img = img.resize((500, 130))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
        
        # Second image
        img1 = Image.open(r"D:\Mini Project\imAGES\clg.jpg")
        img1 = img1.resize((500, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=500, y=0, width=500, height=130)

        # Third image
        img2 = Image.open(r"D:\Mini Project\imAGES\clg_logo.jpg")
        img2 = img2.resize((500, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=1000, y=0, width=500, height=130)

        # Background image
        img3 = Image.open(r"D:\Mini Project\imAGES\snapedit_1709486507018.jpeg")
        img3 = img3.resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl= Label(bg_img, text="FACE RECOGNITION ATTENDENCE SYSTEM", font=("times new roman", 35, "bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        # Student button
        img4 = Image.open(r"D:\Mini Project\imAGES\student_discussion2.jpg")
        img4 = img4.resize((220, 220))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1= Button(bg_img, image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1= Button(bg_img, text="Student Details",cursor="hand2",command=self.student_details,font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b1.place(x=200,y=300,width=220,height=40)

        # Detect Face Button
        img5 = Image.open(r"D:\Mini Project\imAGES\face recanization1.jpg")
        img5 = img5.resize((220, 220))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2= Button(bg_img, image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=220,height=220)

        b2= Button(bg_img, text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b2.place(x=500,y=300,width=220,height=40)

        # Attendence Face Button
        img6 = Image.open(r"D:\Mini Project\imAGES\Attendence3.jpeg")
        img6 = img6.resize((220, 220))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3= Button(bg_img, image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b3.place(x=800,y=100,width=220,height=220)

        b3= Button(bg_img, text="Attendence",cursor="hand2",command=self.attendance_data,font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b3.place(x=800,y=300,width=220,height=40)

        # Help Desk Button
        img7 = Image.open(r"D:\Mini Project\imAGES\helpdesk1.png")
        img7 = img7.resize((220, 220))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4= Button(bg_img, image=self.photoimg7,cursor="hand2",command=self.help)
        b4.place(x=1100,y=100,width=220,height=220)

        b4= Button(bg_img, text="Help Desk",command=self.help,cursor="hand2",font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b4.place(x=1100,y=300,width=220,height=40)

        # Train Data Button
        img8 = Image.open(r"D:\Mini Project\imAGES\Train Data.jpeg")
        img8 = img8.resize((220, 220))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5= Button(bg_img, image=self.photoimg8,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=380,width=220,height=220)

        b5= Button(bg_img, text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b5.place(x=200,y=580,width=220,height=40)

        # Photos Face Button Button
        img9 = Image.open(r"D:\Mini Project\imAGES\photos1.jpg")
        img9 = img9.resize((220, 220))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6= Button(bg_img, image=self.photoimg9,cursor="hand2",command=self.open_img)
        b6.place(x=500,y=380,width=220,height=220)

        b6= Button(bg_img, text="Photos",cursor="hand2",command=self.open_img,font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b6.place(x=500,y=580,width=220,height=40)

         # Developer Button Button
        img10 = Image.open(r"D:\Mini Project\imAGES\development2.jpg")
        img10 = img10.resize((220, 220))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7= Button(bg_img, image=self.photoimg10,cursor="hand2",command=self.developer)
        b7.place(x=800,y=380,width=220,height=220)

        b7= Button(bg_img, text="Developer",cursor="hand2",command=self.developer,font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b7.place(x=800,y=580,width=220,height=40)

         # Exit Button Button
        img11 = Image.open(r"D:\Mini Project\imAGES\exit1.png")
        img11 = img11.resize((220, 220))
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b8= Button(bg_img, image=self.photoimg11,cursor="hand2",command=self.iExit)
        b8.place(x=1100,y=380,width=220,height=220)

        b8= Button(bg_img, text="Exit",cursor="hand2",command=self.iExit,font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b8.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
         os.startfile(r"D:\Mini Project\Data")

    def iExit(self):
          self.iExit=tkinter.messagebox.askyesno("Face Recognition", "Are you Sure",parent=self.root )
          if self.iExit>0:
                self.root.destroy()
          else:
                return

        # Functions Button

    def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app= Student(self.new_window)


    def train_data(self):
            self.new_window=Toplevel(self.root)
            self.app= Train(self.new_window)

    def face_data(self):
            self.new_window=Toplevel(self.root)
            self.app= Face_recognition(self.new_window)

    def attendance_data(self):
            self.new_window=Toplevel(self.root)
            self.app= Attendance(self.new_window)

    def developer(self):
            self.new_window=Toplevel(self.root)
            self.app= Developer(self.new_window)

    def help(self):
          self.new_window=Toplevel(self.root)
          self.app= Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

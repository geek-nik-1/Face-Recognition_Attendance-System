from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        #==variables==
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # First image
        img = Image.open(r"D:\Mini Project\imAGES\slide.jpg")
        img = img.resize((800, 300))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=300)
        
        # Second image
        img1 = Image.open(r"D:\Mini Project\imAGES\Portrait of elementary school.png")
        img1 = img1.resize((800, 280))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=800, y=0, width=800, height=280)

        # Background image
        img3 = Image.open(r"D:\Mini Project\imAGES\snapedit_1709486507018.jpeg")
        img3 = img3.resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)

        title_lbl= Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)

        # Left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)

        img_left = Image.open(r"D:\Mini Project\imAGES\Teacher Online Resource Center.png")
        img_left = img_left.resize((720, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl3 = Label(Left_frame, image=self.photoimg_left)
        f_lbl3.place(x=5, y=0, width=720, height=130)

        left_inside_frame = Frame(Left_frame,bd=2, relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=370)

        #Labels and Entry
        #Attendance id
        attendanceID_label=Label(left_inside_frame,text="AttendanceID:",font=("comicsans 11 bold",11,"bold"),bg="white")
        attendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendance_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendance_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Name
        rollLabel = Label(left_inside_frame,text="Roll:",bg="white", font="comicsans 11 bold")
        rollLabel.grid(row=0,column=2,padx=4,pady=8)

        atten_roll = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font="comicsans 11 bold")
        atten_roll.grid(row=0,column=3,pady=8)

        #name
        nameLabel = Label(left_inside_frame,text="Name:",bg="white",font="comicsans 11 bold")
        nameLabel.grid(row=1,column=0)

        atten_name = ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font="comicsans 11 bold")
        atten_name.grid(row=1,column=1,pady=8)

        #department
        nameLabel = Label(left_inside_frame,text="Department:",bg="white",font="comicsans 11 bold")
        nameLabel.grid(row=1,column=2)

        atten_name = ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_dep,font="comicsans 11 bold")
        atten_name.grid(row=1,column=3,pady=8)

        #time
        nameLabel = Label(left_inside_frame,text="Time:",bg="white",font="comicsans 11 bold")
        nameLabel.grid(row=2,column=0)

        atten_name = ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_time,font="comicsans 11 bold")
        atten_name.grid(row=2,column=1,pady=8)

        #date
        nameLabel = Label(left_inside_frame,text="Date:",bg="white",font="comicsans 11 bold")
        nameLabel.grid(row=2,column=2)

        atten_name = ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date,font="comicsans 11 bold")
        atten_name.grid(row=2,column=3,pady=8)

        #attendance
        attendanceLabel=Label(left_inside_frame,text="Attendance Status",bg="white",font="comicsans 11 bold")
        attendanceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsans 11 bold",state="readonly")
        self.atten_status["values"] = ("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        # buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)

        save_btn=Button(btn_frame,text="Import CSV",command=self.import_CSV,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export CSV",command=self.export_CSV,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=715, height=445)

        label = Label(table_frame, text="Attendance Details", font=("times new roman", 13, "bold"), bg="white")
        label.pack()

        #scroll bar table
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable= ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    def import_CSV(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All files", "*.*")), parent=self.root)
        if not fln:
            messagebox.showerror("Error", "No file selected.")
            return
        try:
            with open(fln, newline="") as myfile:
                csvread = csv.reader(myfile, delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to import CSV: {str(e)}")


    def export_CSV(self):
        try:
            if not mydata:
                messagebox.showerror("No Data", "No data found to export", parent=self.root)
                return

            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File", "*.csv"), ("All files", "*.*")), parent=self.root)
            if not fln:
                return

            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for row in mydata:
                    exp_write.writerow(row)
                messagebox.showinfo("Data Export", f"Your data has been exported to {os.path.basename(fln)} successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export CSV: {str(e)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1]) 
        self.var_atten_name.set(rows[2]) 
        self.var_atten_dep.set(rows[3]) 
        self.var_atten_time.set(rows[4]) 
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6]) 

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("") 
        self.var_atten_name.set("") 
        self.var_atten_dep.set("") 
        self.var_atten_time.set("") 
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        


           
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
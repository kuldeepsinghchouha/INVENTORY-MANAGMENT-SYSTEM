from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        #self.root.resizable(False,FALSE)
        #variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
      
      
        
        
        
        
#TITLE
        self.root.title("Inventory Management Sytem | Developed by Kuldeep")
        self.root.config(bg="white")
        self.root.focus_force()
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)
        lbl_search=Label(SearchFrame,text="Search By Invoice No.",bg="white",font=("times new roman",15))
        lbl_search.place(x=10,y=10)
    
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)
        title=Label(self.root,text="Supplier Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)
       ##Row1
        lbl_supplier_invoice=Label(self.root,text="Invoice No.",font=("goudy old style",15),bg="white").place(x=50,y=150)
        #lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=350,y=150)
        #lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=750,y=150)
        
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15),bg="light yellow").place(x=150,y=150,width=180)
        #txt_gender=Entry(self.root,textvariable=self.var_gender,font=("goudy old style",15),bg="light yellow").place(x=500,y=150,width=180)
      
        
        ## Row 2===============================
        
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="light yellow").place(x=150,y=190,width=180)
       
       ## Row 3===============================
       
       
        lbl_Contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=230)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="light yellow").place(x=150,y=230,width=180)
        
        
       ##Row4=============
        lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=50,y=270)
        
        self.txt_desc=Text(self.root,font=("goudy old style",15),bg="light yellow")
        self.txt_desc.place(x=150,y=270,width=300,height=60)
       # txt_salary=Entry(self.root,textvariable=self.var_salary,font=("goudy old style",15),bg="light yellow").place(x=600,y=270,width=180)
      
        #Button=======================================================
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)
        
##########################employeeee
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)
        
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        
        
        self.supplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill="x")
        scrolly.pack(side=RIGHT,fill="y")
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        
        
        self.supplierTable.heading("invoice",text="Invoice No.")
        self.supplierTable.heading("name",text="Name")
        self.supplierTable.heading("contact",text="Contact")
        self.supplierTable.heading("desc",text="Description")
      
        self.supplierTable["show"]="headings"
    
        self.supplierTable.column("invoice",width=90)
        self.supplierTable.column("name",width=100)
        self.supplierTable.column("contact",width=100)
        self.supplierTable.column("desc",width=100)
      
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)
    
        self.show()
##################################################
    def add(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice Must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Inovice No. already assigned,try different",parent=self.root)
                else:
                    cur.execute("Insert into supplier(invoice,name,contact,desc) values(?,?,?,?)",(
                                               self.var_sup_invoice.get(),
                                               self.var_name.get(),
                                             
                                               self.var_contact.get(),
                                              
                                               self.txt_desc.get('1.0',END),
                                               
                        
                    ))
                    con.commit()
                    messagebox.showinfo("success","Supplier Added successfully",parent=self.root)
                    self.show()       
        
        except Exception as ex:
            
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
     

    def show(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
     
    def get_data(self,ev):
         f=self.supplierTable.focus()
         content=(self.supplierTable.item(f))
         row=content['values']
         #print(row)
         self.var_sup_invoice.set(row[0])
         self.var_name.set(row[1])
         #self.var_email.set(row[2])
         #self.var_gender.set(row[3])
         self.var_contact.set(row[2])
         #self.var_dob.set(row[5])
         #self.var_doj.set(row[6])                           
         #self.var_pass.set(row[7])
         #self.var_utype.set(row[8])
         self.txt_desc.delete('1.0',END)
         self.txt_desc.insert(END,row[3])
         #self.txt_address.set(row[10])
         #self.var_salary.set(row[10])
         
    
    def update(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Supplier Invoice Must be required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
            if row==None:
                    messagebox.showerror("Error","Invalid Supplier INvoice",parent=self.root)
            else:
                    cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=?",(
                                               
                                              self.var_name.get(),
                                              self.var_contact.get(),
                                              self.txt_desc.get('1.0',END),
                                              self.var_sup_invoice.get(),
                                               ))
                    con.commit()
                    messagebox.showinfo("success","Supplier Updated successfully",parent=self.root)
                    self.show()       
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
     
         
    def delete(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                
                messagebox.showerror("Error","Invoice No.  must be required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                     cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                     con.commit()
                     messagebox.showinfo("Delete","Invoice No. Deleted Successfully",parent=self.root)
                     self.show()
        except EXCEPTION as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
            
    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete("1.0",END)
        self.txt_desc.insert("")
        self.txt_searchby.set("")
        
        self,show()
    
    def search(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
        
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Invoice No. should be required",parent=self.root) 
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    
                   self.supplierTable.delete(*self.supplierTable.get_children())
                   self.supplierTable.insert('',END,values=row)
                else:
                    
                    messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
          
                
if __name__=="__main__":
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()

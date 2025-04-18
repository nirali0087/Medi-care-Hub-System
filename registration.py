from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import random
import time
import mysql.connector

class Registration:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Registration System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="black")
        
        # Define variables at the class level
        self.Date_of_Registration = StringVar()
        self.Date_of_Registration.set(time.strftime("%d/%m/%y"))
        self.Ref = StringVar()
        self.Refid = StringVar()
        self.Mobile_no = StringVar()
        self.Pincode = StringVar()
        self.Address = StringVar()
        self.Firstname = StringVar()
        self.Lastname = StringVar()
        self.var1 = StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.var4 = StringVar()
        self.var5 = IntVar()
        self.Membership = StringVar()
        self.Membership.set("0")
        
        self.connection = mysql.connector.connect(
              host="localhost",
              user="root",
              password="Nilu@07_",
              database="patients")
        
        self.cursor = self.connection.cursor()
        print("Connection established: ", self.connection)

        def insert_data(self):
            registration_date = self.Date_of_Registration.get()
            Refid = self.Ref.get()
            first_name = self.Firstname.get()
            last_name = self.Lastname.get()
            mobile_no = self.Mobile_no.get()
            address = self.Address.get()
            pincode = self.Pincode.get()
            gender = self.var4.get() 
            membership = self.Membership.get()

            insert_query = "INSERT INTO patients.patientregistration (registration_date, reference_id, first_name, last_name, mobile_no, address, pincode, gender, membership) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (registration_date, Refid, first_name, last_name, mobile_no, address, pincode, gender, membership)
            self.cursor.execute(insert_query, data)
            self.connection.commit()

            query_all = "SELECT * FROM patients.patientregistration"
            self.cursor.execute(query_all)
            records = self.cursor.fetchall()

            # Clear existing text in detail_text
            self.detail_text.delete("1.0", END)

            # Display the fetched records in the detail_text widget
            for record in records:
                record_text = "\t".join(str(value) for value in record) + "\n"
                self.detail_text.insert(END, record_text)

            tkinter.messagebox.showinfo("Success", "Data inserted into database successfully!")


        def exitbtn():
            exitbtn = tkinter.messagebox.askyesno("Member Registration Form", "Are you sure you want to exit?")
            if exitbtn > 0:
                root.destroy()
                return

        def resetbtn():
            self.Firstname.set("")
            self.Ref.set("")
            self.Refid.set("")
            self.Mobile_no.set("")
            self.Pincode.set("")
            self.Address.set("")
            self.Lastname.set("") 
            self.var1.set("")
            self.var3.set("")
            self.var4.set("")
            self.var5.set("")
            self.Membership.set("0")
            member_gendercmb.current(0)
            member_id_proofcmb.current(0)
            member_memtypecmb.current(0)
            member_paymentwithcmb.current(0)
            member_membershiptxt.configure(state=DISABLED)

        def deletebtn():
            response = tkinter.messagebox.askokcancel("Member Registration Form ", "Are you sure you want to delete the record?")
            if response:
                resetbtn()
                self.detail_text.delete("1.0", END)


        def Reference_number():
            ranumber = random.randint(10000, 999999)
            randomnumber = str(ranumber)
            self.Ref.set(randomnumber)

        def membership_fees():
            if self.var5.get() == 1:
                member_membershiptxt.configure(state=NORMAL)
                item = float(15000)
                self.Membership.set(str(item)+ "Rs")
            elif self.var5.get() == 0:
                member_membershiptxt.configure(state=DISABLED)
                self.Membership.set("0")

        def Receipt():
            Reference_number()
            insert_data(self)
            self.detail_text.insert(END, f"{self.Date_of_Registration.get()}\t{self.Ref.get()}\t{self.Firstname.get()}\t{self.Lastname.get()}\t{self.Mobile_no.get()}\t{self.Address.get()}\t{self.Pincode.get()}\t{member_gendercmb.get()}\t{self.Membership.get()}\n")

        def search_data():
            ref_id = self.Refid.get()

            query = f"SELECT * FROM patients.patientregistration WHERE reference_id = '{ref_id}'"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            fields = [field_md[0] for field_md in self.cursor.description]
            result_2 = [dict(zip(fields, row)) for row in result]

            self.detail_text.delete("1.0", END)

            if result_2:
                for row in result_2:
                    data_row = "\t".join(str(value) for value in row.values()) + "\n"
                    self.detail_text.insert(END, data_row)
            else:
                tkinter.messagebox.showinfo("Search Result", "No record found for the given Reference ID.")

        ############################ Title #############################
        title = Label(self.root, text="Member Registration Form", font=("monotype corsiva", 30, "bold"), bd=5,
                              relief=GROOVE, bg="#E6005C", fg="#000000")
        title.pack(side=TOP, fill=X)

        ################# member frame #################

        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#001a66")
        Manage_Frame.place(x=20, y=100, width=470, height=680)

        ############# text, label, ##########################
        Cus_title = Label(Manage_Frame, text="Customer Details", font=("cambria", 20, "bold"), bg="#001a66", fg="white")
        Cus_title.grid(row=0, columnspan=2, pady=5)

        member_datelbl = Label(Manage_Frame, text="Date", font=("cambria", 15, "bold"), bg="#001a66", fg="white")
        member_datelbl.grid(row=1, column=0, pady=5, padx=10, sticky="w")

        member_datetxt = Entry(Manage_Frame, font=("cambria", 15, "bold"), textvariable=self.Date_of_Registration)
        member_datetxt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        member_reflbl = Label(Manage_Frame, text="Reference ID", font=("cambria", 15, "bold"), bg="#001a66", fg="white")
        member_reflbl.grid(row=2, column=0, pady=5, padx=10, sticky="w")

        member_reftxt = Entry(Manage_Frame, font=("cambria", 15, "bold"), state=DISABLED, text=self.Ref)
        member_reftxt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        member_fnamelbl = Label(Manage_Frame, text="First Name", font=("cambria", 15, "bold"), bg="#001a66", fg="white")
        member_fnamelbl.grid(row=3, column=0, pady=5, padx=10, sticky="w")

        member_fnametxt = Entry(Manage_Frame, font=("cambria", 15, "bold"), textvariable=self.Firstname)
        member_fnametxt.grid(row=3, column=1, pady=5, padx=10, sticky="w")

        member_lnamelbl = Label(Manage_Frame, text="Last Name", font=("cambria", 15, "bold"), bg="#001a66", fg="white")
        member_lnamelbl.grid(row=4, column=0, pady=5, padx=10, sticky="w")

        member_lnametxt = Entry(Manage_Frame, font=("cambria", 15, "bold"), textvariable=self.Lastname)
        member_lnametxt.grid(row=4, column=1, pady=5, padx=10, sticky="w")

        member_mobilelbl = Label(Manage_Frame, text="Mobile No", font=("cambria", 15, "bold"), bg="#001a66", fg="white")
        member_mobilelbl.grid(row=5, column=0, pady=5, padx=10, sticky="w")

        member_mobiletxt = Entry(Manage_Frame, font=("cambria", 15, "bold"), textvariable=self.Mobile_no)
        member_mobiletxt.grid(row=5, column=1, pady=5, padx=10, sticky="w")

        member_addresslbl = Label(Manage_Frame, text="Address", font=("cambria", 15, "bold"), bg="#001a66", fg="white")
        member_addresslbl.grid(row=6, column=0, pady=5, padx=10, sticky="w")

        member_addresstxt = Entry(Manage_Frame, font=("cambria", 15, "bold"), textvariable=self.Address)
        member_addresstxt.grid(row=6, column=1, pady=5, padx=10, sticky="w")

        member_pincodelbl = Label(Manage_Frame, text="Pincode", font=("cambria", 15, "bold"), bg="#001a66", fg="white")
        member_pincodelbl.grid(row=7, column=0, pady=5, padx=10, sticky="w")

        member_pincodetxt = Entry(Manage_Frame, font=("cambria", 15, "bold"), textvariable=self.Pincode)
        member_pincodetxt.grid(row=7, column=1, pady=5, padx=10, sticky="w")

        member_genderlbl = Label(Manage_Frame, text="Gender", font=("cambria", 15, "bold"), bg="#001a66", fg="white")
        member_genderlbl.grid(row=8, column=0, pady=5, padx=10, sticky="w")

        member_gendercmb = ttk.Combobox(Manage_Frame, text=self.var4, state="readonly", font=("cambria", 15, "bold"), width=19)
        member_gendercmb['values'] = ("", "Male", "Female", "Other")
        member_gendercmb.current(0)
        member_gendercmb.grid(row=8, column=1, pady=5, padx=10, sticky="w")

        member_id_prooflbl = Label(Manage_Frame, text="ID Proof", font=("cambria", 15, "bold"), bg="#001a66", fg="white")
        member_id_prooflbl.grid(row=9, column=0, pady=5, padx=10, sticky="w")

        member_id_proofcmb = ttk.Combobox(Manage_Frame, text=self.var3, state="readonly", font=("cambria", 15, "bold"), width=19)
        member_id_proofcmb['values'] = ("", "Adhaar Card", "Passport", "Driving License", "Pan card", "Student ID")
        member_id_proofcmb.current(0)
        member_id_proofcmb.grid(row=9, column=1, pady=5, padx=10, sticky="w")

        member_memtypelbl = Label(Manage_Frame, text="Member Type", font=("cambria", 15, "bold"), bg="#001a66", fg="white")
        member_memtypelbl.grid(row=10, column=0, pady=5, padx=10, sticky="w")

        member_memtypecmb = ttk.Combobox(Manage_Frame, text=self.var2, state="readonly", font=("cambria", 15, "bold"), width=19)
        member_memtypecmb['values'] = ("", "Ayushman Card", "Insurance", "Pay Immediately", "Pay at a leaving")
        member_memtypecmb.current(0)
        member_memtypecmb.grid(row=10, column=1, pady=5, padx=10, sticky="w")

        member_paymentwithlbl = Label(Manage_Frame, text="Payment", font=("cambria", 15, "bold"), bg="#001a66", fg="white")
        member_paymentwithlbl.grid(row=11, column=0, pady=5, padx=10, sticky="w")

        member_paymentwithcmb = ttk.Combobox(Manage_Frame, text=self.var1, state="readonly", font=("cambria", 15, "bold"), width=19)
        member_paymentwithcmb['values'] = ("", "Cash", "Debit Card - Rupay", "Debit Card - Visa", "Card - Mastercard", "Credit Card", "Phonepe", "GooglePay", "Paytm", "Net-Banking")
        member_paymentwithcmb.current(0)
        member_paymentwithcmb.grid(row=11, column=1, pady=5, padx=10, sticky="w")

        member_membership = Checkbutton(Manage_Frame, text="Membership Fees", variable=self.var5, onvalue=1, offvalue=0, font=("cambria", 15, "bold"), bg="#001a66", fg="white", command=membership_fees) 
        member_membership.grid(row=12, column=0, sticky="w")

        member_membershiptxt = Entry(Manage_Frame, font=("cambria", 15, "bold"), state=DISABLED, justify=RIGHT, textvariable=self.Membership)
        member_membershiptxt.grid(row=12, column=1, pady=5, padx=10, sticky="w")

        member_refidtxt = Entry(Manage_Frame, font=("cambria", 15, "bold"), textvariable=self.Refid)
        member_refidtxt.grid(row=13, column=1, pady=5, padx=10, sticky="w")

        ############### Detail Frame #####################
        self.detail_frame = Frame(self.root, relief=RIDGE, bg="#001a66")
        self.detail_frame.place(x=500, y=100, width=900, height=680) 

        self.detail_label = Label(self.detail_frame, font=("cambria", 11, "bold"), pady=10, padx=2, width=95,
                                  text="Date\tRef Id\tFirstname\tLastname\tMobile No\tAddress\tPincode\tGender\tMembership")
        self.detail_label.grid(row=0, column=0, columnspan=4, sticky="w")

        self.detail_text = Text(self.detail_frame, width=95, height=30, font=("cambria", 12))
        self.detail_text.grid(row=1, column=0, columnspan=4, sticky="nsew")

        self.scrollbar = Scrollbar(self.detail_frame, command=self.detail_text.yview)
        self.scrollbar.grid(row=1, column=4, sticky='nse')

        self.detail_text.configure(yscrollcommand=self.scrollbar.set)

        # Buttons
        self.receipt_btn = Button(self.detail_frame, padx=10, bd=8, font=("cambria", 12, "bold"), bg="#ff9966",
                                  width=20, text="Receipt", command=Receipt)
        self.receipt_btn.grid(row=2, column=0)

        self.reset_btn = Button(self.detail_frame, padx=10, bd=8, font=("cambria", 12, "bold"), bg="#ff9966",
                                width=20, text="Reset", command= resetbtn)
        self.reset_btn.grid(row=2, column=1)

        self.delete_btn = Button(self.detail_frame, padx=10, bd=8, font=("cambria", 12, "bold"), bg="#ff9966",
                                 width=20,text="Delete", command= deletebtn)
        self.delete_btn.grid(row=2, column=2)

        self.exit_btn = Button(self.detail_frame, padx=10, bd=5, font=("cambria", 12, "bold"), bg="#ff9966",
                               width=20, text="Exit", command=exitbtn)
        self.exit_btn.grid(row=2, column=3)

        self.search_btn = Button(Manage_Frame, font=("cambria", 12, "bold"), bg="#ff9966", width=20, text="Search", command=search_data)
        self.search_btn.grid(row=13, column=0, pady=5, padx=10, sticky="w")


if __name__ == "__main__":
    root = Tk()
    app = Registration(root)
    root.mainloop()
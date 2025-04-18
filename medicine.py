from datetime import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
import random
import time

class Window3:

    def __init__(self,master):
        self.master=master
        self.master.title("Medicine Stock System")
        self.master.geometry("1350x750+0+0")
        self.master.configure(background="grey")
        self.frame=Frame(self.master)
        self.frame.pack()

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nilu@07_",
            database="medi_db"
)
        cursor = db.cursor()

    
        cmbTablets=StringVar()
        RefNo=StringVar()
        Dose=StringVar()
        IssueDate=StringVar()
        ExpDate=StringVar()
        SideEffects=StringVar()
        PatientID=StringVar()
        PatientName=StringVar()
        DateOfBirth=StringVar()
        PatientAddress=StringVar()
        NHSNo=StringVar()
        StorageAdvice=StringVar()
        FurtherInformation=StringVar()
        UsingMachine=StringVar()
        Medication=StringVar()
        NoofTablets=StringVar()
        Lot=StringVar()
        Strength=StringVar()
        Prescription=StringVar()

        #.......................................................................................................................#

        def iExit():
            iExit = tkinter.messagebox.askyesno("Medicine Stock System", "Confirm if you want to exit")
            if iExit > 0:
                # Close the database connection
                cursor.close()
                db.close()
                self.master.destroy()
                return

        def iReset():
            cmbTablets.set("")
            RefNo.set("")
            Dose.set("")
            IssueDate.set("")
            ExpDate.set("")
            SideEffects.set("")
            PatientID.set("")
            PatientName.set("")
            DateOfBirth.set("")
            PatientAddress.set("")
            NHSNo.set("")
            StorageAdvice.set("")
            FurtherInformation.set("")
            UsingMachine.set("")
            Medication.set("")
            NoofTablets.set("")
            Lot.set("")
            Strength.set("")
            self.txtPrescription.delete("1.0",END)
            return

        def iDelete():
            cmbTablets.set("")
            RefNo.set("")
            Dose.set("")
            IssueDate.set("")
            ExpDate.set("")
            SideEffects.set("")
            PatientID.set("")
            PatientName.set("")
            DateOfBirth.set("")
            PatientAddress.set("")
            NHSNo.set("")
            StorageAdvice.set("")
            FurtherInformation.set("")
            UsingMachine.set("")
            Medication.set("")
            NoofTablets.set("")
            Lot.set("")
            Strength.set("")
            self.txtPrescription.delete("1.0",END)
            self.txtFrameDetail.delete("1.0",END)

            return

        def iReceipt():
            # Get the values from the entry fields
            tablet = cmbTablets.get()
            ref_no = RefNo.get()
            dosage = Dose.get()
            no_of_tablets = NoofTablets.get() or 0  # Default to 0 if the field is empty
            lot = Lot.get()
            issue_date = IssueDate.get()
            exp_date = ExpDate.get()
            strength = Strength.get()
            storage_advice = StorageAdvice.get()
            nhs_no = NHSNo.get()
            patient_name = PatientName.get()
            dob = DateOfBirth.get()
            patient_address = PatientAddress.get()

            # Check if the required fields are filled
            if not tablet or not dosage or not no_of_tablets or not lot or not issue_date or not exp_date or not strength or not storage_advice or not nhs_no or not patient_name or not dob or not patient_address:
                tkinter.messagebox.showerror("Error", "Please fill in all required fields.")
                return

            # Prepare the SQL query
            query = "INSERT INTO medi_db.prescriptions (tablet, ref_no, dosage, no_of_tablets, lot, issue_date, exp_date, strength, storage_advice, nhs_no, patient_name, dob, patient_address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (tablet, ref_no, dosage, no_of_tablets, lot, issue_date, exp_date, strength, storage_advice, nhs_no, patient_name, dob, patient_address)

            # Execute the query
            cursor.execute(query, values)
            db.commit()

            # Display a success message
            tkinter.messagebox.showinfo("Success", "Data inserted successfully.")

            # Clear the entry fields
            iReset()

            return

        def iPrescription():
            self.txtPrescription.insert(END,"Name of Tablet: \t\t\t\t" + cmbTablets.get() + "\n")
            self.txtPrescription.insert(END,"Dose: \t\t\t\t" + Dose.get() + "\n")
            self.txtPrescription.insert(END,"Number of Tablets: \t\t\t\t" + NoofTablets.get() + "\n")
            self.txtPrescription.insert(END,"Lot: \t\t\t\t" + Lot.get() + "\n")
            self.txtPrescription.insert(END,"Issue Date: \t\t\t\t" + IssueDate.get() + "\n")
            self.txtPrescription.insert(END,"Exp. Date: \t\t\t\t" + ExpDate.get() + "\n")
            self.txtPrescription.insert(END,"Strength: \t\t\t\t" + Strength.get() + "\n")
            self.txtPrescription.insert(END,"Possible Side Effects: \t\t\t\t" + SideEffects.get() + "\n")
            self.txtPrescription.insert(END,"Storage Advice: \t\t\t\t" + StorageAdvice.get() + "\n")
            self.txtPrescription.insert(END,"NHS Number: \t\t\t\t" + NHSNo.get() + "\n")
            self.txtPrescription.insert(END,"Extra Information: \t\t\t\t" + FurtherInformation.get() + "\n")

            return


        #.......................................................................................................................#
        

        MainFrame=Frame(self.frame)
        MainFrame.grid()

        TitleFrame=Frame(MainFrame,width=1350,padx=20,bd=20,relief=RIDGE)
        TitleFrame.pack(side=TOP)
        
        self.lblTitle=Label(TitleFrame,font=("arial",40,"bold"),text="Pharmacy Management System",padx=2)
        self.lblTitle.grid()

        FrameDetail=Frame(MainFrame,bd=20,width=1350,height=100,padx=20,relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame=Frame(MainFrame,bd=20,width=1350,height=50,padx=20,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame,bd=20,width=1350,height=400,padx=20,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT=LabelFrame(DataFrame,bd=10,width=800,height=300,font=("arial",12,"bold"),text="Patient Detail:",relief=RIDGE,padx=20)
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT=LabelFrame(DataFrame,bd=10,width=450,height=300,font=("arial",12,"bold"),text="Prescription:",relief=RIDGE,padx=20)
        DataFrameRIGHT.pack(side=RIGHT)

        #..................................................................................................................#

        self.lblTablet=Label(DataFrameLEFT,font=("arial",12,"bold"),text="Tablet:",padx=2,pady=2)
        self.lblTablet.grid(row=0,column=2,sticky=W)

        self.Tablet=ttk.Combobox(DataFrameLEFT,font=("arial",12,"bold"),state="readonly",width=23,textvariable=cmbTablets)
        self.Tablet["value"]=('',"Panadol","Disprin") #............ARRAY
        self.Tablet.current(0)
        self.Tablet.grid(row=0,column=3)

        #..................................................................................................................#

        labels = ["Patient Name:" , "DateOfBirth:" , "NHS No:" , "Patient Address:" , "Patient ID:" , "Lot:" ,
                  "No.of Tablets:" , "Strength:" , "Medication:"] #.............LIST
        counter = 0
        for i in range (len(labels)):
            self.cur_label = "label" + str(i)
            self.cur_label=Label(DataFrameLEFT,font=("arial",12,"bold"),text=labels[i],padx=2,pady=2)
            self.cur_label.grid(row=counter,column=0,sticky=W)

            counter += 1

        entry_box = {"Patient Name:":PatientName , "DateOfBirth:":DateOfBirth , "NHS No:":NHSNo , "Patient Address:":PatientAddress , "Patient ID:":PatientID , "Lot:":Lot
                     , "No.of Tablets:":NoofTablets , "Strength:":Strength , "Medication:":Medication} #.........DICTIONARY

        counter = 0

        for i in entry_box:
            self.cur_entrybox = "entry" + i
            self.cur_entrybox = Entry(DataFrameLEFT,font=("arial",12,"bold"),width=25,textvariable=entry_box[i])
            self.cur_entrybox.grid(row=counter,column=1)
            counter += 1

        labels = ["Dose:" , "Issue Date:" , "Exp Date:" , "Side Effects:" , "Ref No:" , "Storage Advice:" , "Using Machine:" , "Further Information:"]#..LIST
        
        counter = 1
        
        for i in range (len(labels)):
            self.cur_label = "label" + str(i)
            self.cur_label=Label(DataFrameLEFT,font=("arial",12,"bold"),text=labels[i],padx=2,pady=2)
            self.cur_label.grid(row=counter,column=2,sticky=W)

            counter += 1

        entry_box = {"Dose:":Dose , "Issue Date:":IssueDate , "Exp Date:":ExpDate , "Side Effects:":SideEffects , "Ref No:":RefNo ,
                     "Storage Advice:":StorageAdvice , "Using Machine:":UsingMachine , "Further Information:":FurtherInformation}#........DICTIONARY

        counter = 1

        for i in entry_box:
            self.cur_entrybox = "entry" + i
            self.cur_entrybox = Entry(DataFrameLEFT,font=("arial",12,"bold"),width=25,textvariable=entry_box[i])
            self.cur_entrybox.grid(row=counter,column=3)
            counter += 1

        #..........................................................................................................................#

        self.txtPrescription=Text(DataFrameRIGHT,font=("arial",12,"bold"),width=43,height=12,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #..........................................................................................................................#

        self.btnPrescription=Button(ButtonFrame,text="Prescription",font=("arial",12,"bold"),width=24,bd=4,command=iPrescription)
        self.btnPrescription.grid(row=0,column=0)

        self.btnReceipt=Button(ButtonFrame,text="Receipt",font=("arial",12,"bold"),width=24,bd=4,command=iReceipt)
        self.btnReceipt.grid(row=0,column=1)

        self.btnDelete=Button(ButtonFrame,text="Delete",font=("arial",12,"bold"),width=24,bd=4,command=iDelete)
        self.btnDelete.grid(row=0,column=2)

        self.btnReset=Button(ButtonFrame,text="Reset",font=("arial",12,"bold"),width=24,bd=4,command=iReset)
        self.btnReset.grid(row=0,column=3)

        self.btnExit=Button(ButtonFrame,text="Exit",font=("arial",12,"bold"),width=24,bd=4,command=iExit)
        self.btnExit.grid(row=0,column=4)

        #...........................................................................................................................#

        self.lblLabel=Label(FrameDetail,font=("arial",10,"bold"),pady=8,text="Name of Tablet \tReference No. \tDoseage \tNo.of Tablets \tLot \tIssue Date \tExp. Date \tStrength\tStorage Adv. \tNHS Number \tPatient Name\t DOB\t Address",)
        self.lblLabel.grid(row=0,column=0)

        self.txtFrameDetail=Text(FrameDetail,font=("arial",12,"bold"),width=141,height=4,padx=2,pady=4)
        self.txtFrameDetail.grid(row=1,column=0)

if __name__=="__main__":
    root = Tk()
    app = Window3(root)
    root.mainloop()
from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib

def clear():
     
    # deleteing for burger 
    vegburEntry.delete(0,END)
    cheesburEntry.delete(0,END)
    KFCburEntry.delete(0,END)
    alloTikEntry.delete(0,END)
    butterEntry.delete(0,END)
    freshEntry.delete(0,END)
      
    # deleteing for pizza 
    otcEntry.delete(0,END)
    cheesburstEntry.delete(0,END)
    tonPizEntry.delete(0,END)
    alupizEntry.delete(0,END)
    farmHoEntry.delete(0,END)
    lateSEntry.delete(0,END)
    
    
#   places for Shakes
    cokeEntry.delete(0,END)
    fantaEntry.delete(0,END)
    limcaEntry.delete(0,END)
    thumbsEntry.delete(0,END)
    mountDewEntry.delete(0,END)
    minrAEntry.delete(0,END)
    
    # ***************************************************
    #insert 0 at dumy places 
    vegburEntry.insert(0,0)
    cheesburEntry.insert(0,0)
    KFCburEntry.insert(0,0)
    alloTikEntry.insert(0,0)
    butterEntry.insert(0,0)
    freshEntry.insert(0,0)
    
    # inserting 0 at dumy places for pizza 
    otcEntry.insert(0,0)
    cheesburstEntry.insert(0,0)
    tonPizEntry.insert(0,0)
    alupizEntry.insert(0,0)
    farmHoEntry.insert(0,0)
    lateSEntry.insert(0,0)
    
      # inserting 0 at dumy places for pizza 
    cokeEntry.insert(0,0)
    fantaEntry.insert(0,0)
    limcaEntry.insert(0,0)
    thumbsEntry.insert(0,0)
    mountDewEntry.insert(0,0)
    minrAEntry.insert(0,0)
    # ***************************************************
    burgerPriceEntry.delete(0,END)
    pizzaPriceEntry.delete(0,END)
    coldDrinksPriceEntry.delete(0,END)

    # ***************************************************


    burgerTaxEntry.delete(0,END)
    pizzaTaxEntry.delete(0,END)
    coldDrinksTaxEntry.delete(0,END)
    
    # ***************************************************
    
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billEntry.delete(0,END)
    
    
    textArea.delete(1.0,END)
def send_email():
    def send_gmail():
        try:
            # Use the provided sender email and password
            sender_email = "your mail id @gmail.com"
            password = "Your gmail password for mailing that you can generate from google two step verification setting"

            # Connect to the SMTP server
            ob = smtplib.SMTP("smtp.gmail.com", 587)
            ob.starttls()
            ob.login(sender_email, password)

            # Get the recipient email address from the entry widget
            recipient_email = recieverEntry.get()

            # Get the email message from the text area
            email_message = email_textarea.get(1.0, END)
            subject = "Thank you for ordering"
            email_message = f"Subject: {subject}\n\n{email_message}"

            # Send the email
            ob.sendmail(sender_email, recipient_email, email_message)

            # Close the SMTP connection
            ob.quit()

            # Show success message
            messagebox.showinfo("Success", "Bill is sent successfully", parent=root1)
            root1.destroy()

        except Exception as e:
            # Show error message if there's an issue
            messagebox.showerror("Error", f"Something went wrong: {str(e)}", parent=root1)
    
    if textArea.get(1.0,END)=="\n":
        messagebox.showerror("Error","Bill is empty")
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title("Send Email")
        root1.config(bg="gray20")
        root1.resizable(0,0)
        
        recipientFrame=LabelFrame(root1,text="Recipent",font=("arial",16,"bold"),bd=6,bg="gray20",fg="white")
        recipientFrame.grid(row=1,column=0,pady=20,padx=40)
        
        recieverLabel=Label(recipientFrame,text="Email Address",font=("arial",14,"bold"),bd=6,bg="gray20",fg="white")
        recieverLabel.grid(row=0,column=0,pady=8,padx=10)
        
        recieverEntry=Entry(recipientFrame,font=("arial",14,"bold"),bd=2,width=23,relief=GROOVE)
        recieverEntry.grid(row=0,column=1,pady=8,padx=10)
        
        messageLabel=Label(recipientFrame,text="Message",font=("arial",14,"bold"),bd=6,bg="gray20",fg="white")
        messageLabel.grid(row=1,column=0,pady=8,padx=10)
        
        
        email_textarea=Text(recipientFrame,font=("arial",14,"bold"),bd=2,relief=SUNKEN,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textArea.get(1.0,END).replace("=","").replace("-","").replace("\t\t\t","      "))
        
        sendButton=Button(root1,text="Send",font=("arial",14,"bold"),width=15,command=send_gmail)
        sendButton.grid(row=2,column=0,pady=20)
        root1.mainloop()
def print_bill():
    if textArea.get(1.0,END)=="\n":
        messagebox.showerror("Error","Bill is empty ")
    else:
        file=tempfile.mktemp(".txt")
        open(file,"w").write(textArea.get(1.0,END))
        os.startfile(file,"print")    
    
def search_bill():
    for i in  os.listdir("bills/"):
        if i.split(".")[0]==billEntry.get():
            f=open(f"bills/{i}","r")
            textArea.delete(1.0,END)
            for data in f:
                textArea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror("Error","Invalid Bill Number")  

if not os.path.exists("bills"):
    os.mkdir("bills")

def save_bill():
    global billnumber
    result=messagebox.askyesno("Confirm","Do you want to save the bill?")
    if result:
        bill_content=textArea.get(1.0,END)
        file=open(f"bills/{billnumber}.txt","w")
        file.write(bill_content)
        file.close()
        messagebox.showinfo("Success",f"Bill number {billnumber} is saved succesfully")
        billnumber=random.randint(1000,9999)
        
        
billnumber=random.randint(1000,9999)
# Bill button functionally part

def bill_area():
    if nameEntry.get()=="" or phoneEntry.get()=="":
        messagebox.showerror("Error","Customer Details are required")
    elif burgerPriceEntry.get()=="" and pizzaPriceEntry.get()=="" and coldDrinksPriceEntry.get()=="":
        messagebox.showerror("Error","No products are selected")
    elif burgerPriceEntry.get()=="0 Rs" and pizzaPriceEntry.get()=="0 Rs" and coldDrinksPriceEntry.get()=="0 Rs":
        messagebox.showerror("Error","No products are selected")
    else:
        textArea.delete(1.0,END)
        textArea.insert(END,"\t**Welcome to khati house**\n")
        textArea.insert(END,f"\nBill Number: {billnumber}")
        textArea.insert(END,f"\nCustomer Name: {nameEntry.get()}")
        textArea.insert(END,f"\nCustomer Phone : {phoneEntry.get()}")
        textArea.insert(END,"\n======================================= ")
        textArea.insert(END,"\nProduct\t\tQuantity\t\tPrice")
        textArea.insert(END,"\n======================================= ")
        
        # bill printing of burgers
     
        if vegburEntry.get()!="0":
            textArea.insert(END,f" Aloo-Tikki Burger\t\t   {vegburEntry.get()}\t\t {vegburgerprice} Rs\n")
        if cheesburEntry.get()!="0":
             textArea.insert(END,f" Cheese Burger\t\t       {cheesburEntry.get()}\t\t {vegcheseeburgerprice} Rs\n")
        if KFCburEntry.get()!="0":  
            textArea.insert(END,f" KFC Burger\t\t       {KFCburEntry.get()}\t\t {kfcburgerprice} Rs\n")
        if alloTikEntry.get()!="0":
            textArea.insert(END,f" Crispy Corn Burger\t\t  {alloTikEntry.get()}\t\t {allotickyprice} Rs\n")
        if butterEntry.get()!="0":     
            textArea.insert(END,f" Peri-Peri Burger\t\t    {butterEntry.get()}\t\t {butterburgerprice} Rs\n")
        if freshEntry.get()!="0":     
            textArea.insert(END,f" Double-Patty Burger\t\t {freshEntry.get()}\t\t {freshburgerprice} Rs\n")
      
      # bill printing of pizza
      
        if otcEntry.get()!="0":
            textArea.insert(END,f" Marghrita Pizza\t\t     {otcEntry.get()}\t\t {otcpizzprice} Rs\n")
        if cheesburstEntry.get()!="0":
             textArea.insert(END,f" Cheese Burst Pizza\t\t  {cheesburstEntry.get()}\t\t {cheeseburstprice} Rs\n")
        if tonPizEntry.get()!="0":  
            textArea.insert(END,f" Tondori Pizza\t\t       {tonPizEntry.get()}\t\t {tonpizprice} Rs\n")
        if alupizEntry.get()!="0":
            textArea.insert(END,f" Corn-Capsicum Pizza\t\t {alupizEntry.get()}\t\t {alupizzprice} Rs\n")
        if farmHoEntry.get()!="0":     
            textArea.insert(END,f" Farmhouse Pizza\t\t     {farmHoEntry.get()}\t\t {farmpizzprice} Rs\n")
        if lateSEntry.get()!="0":     
            textArea.insert(END,f" Italian Pizza\t\t       {lateSEntry.get()}\t\t {latepizzprice} Rs\n")
        # bill printing of  shakes
      
        if cokeEntry.get()!="0":
            textArea.insert(END,f" Chocolate-Shake\t\t     {cokeEntry.get()}\t\t {cokeprice} Rs\n")
        if fantaEntry.get()!="0":
             textArea.insert(END,f" Strawberry-Shake\t\t    {fantaEntry.get()}\t\t {fantaprice} Rs\n")
        if limcaEntry.get()!="0":  
            textArea.insert(END,f" Kit-Kat Shake\t\t       {limcaEntry.get()}\t\t {limcaprice} Rs\n")
        if thumbsEntry.get()!="0":
            textArea.insert(END,f" Oreo-Shake\t\t       {thumbsEntry.get()}\t\t {thumbsprice} Rs\n")
        if mountDewEntry.get()!="0":     
            textArea.insert(END,f" Blue-Berry Shake\t\t    {mountDewEntry.get()}\t\t {mountdewprice} Rs\n")
        if minrAEntry.get()!="0":     
            textArea.insert(END,f" Butter-Scotch Shake\t\t {minrAEntry.get()}\t\t {mindraprice} Rs\n")
        
         
        textArea.insert(END,"----------------------------------------")
        
       # taxes for Burger
        
        if burgerTaxEntry.get()!="0.0 Rs":
            textArea.insert(END,f"\n Burger Tax\t\t\t{burgerTaxEntry.get()}")          
       # taxes for pizza
       
        if pizzaTaxEntry.get()!="0.0 Rs":
            textArea.insert(END,f"\n Pizza Tax\t\t\t{pizzaTaxEntry.get()}")        
       # taxes for Shakes
       
        if coldDrinksTaxEntry.get()!="0.0 Rs":
            textArea.insert(END,f"\n Shakes Tax\t\t\t{coldDrinksTaxEntry.get()}")        
        textArea.insert(END,"\n----------------------------------------")
        textArea.insert(END,f"\n Total Bill \t\t\t   {totalbill} Rs")
        textArea.insert(END,"\n----------------------------------------")
   
        save_bill()
    
   
        
# total button functionally part
def total():
    global totalbill
    global vegburgerprice,vegcheseeburgerprice,kfcburgerprice,allotickyprice,butterburgerprice,freshburgerprice
    # print("hello")
    vegburgerprice=int(vegburEntry.get())*50
    vegcheseeburgerprice=int(cheesburEntry.get())*60
    kfcburgerprice=int(KFCburEntry.get())*100
    allotickyprice=int(alloTikEntry.get())*70
    butterburgerprice=int(butterEntry.get())*80
    freshburgerprice=int(freshEntry.get())*120
    
   
    totalburgerprice=vegburgerprice+vegcheseeburgerprice+kfcburgerprice+allotickyprice+freshburgerprice+butterburgerprice
    burgerPriceEntry.delete(0,END)
    burgerPriceEntry.insert(0,f"{totalburgerprice} Rs")
    burgertax=totalburgerprice*0.10 # 10% taxes on burgers
    burgerTaxEntry.delete(0,END)
    burgerTaxEntry.insert(0,f"{burgertax} Rs")
    
    # now for pizzazz
    
    
    global otcpizzprice,cheeseburstprice,alupizzprice,tonpizprice,farmpizzprice,latepizzprice
    otcpizzprice=int(otcEntry.get())*100
    cheeseburstprice=int(cheesburstEntry.get())*100
    tonpizprice=int(tonPizEntry.get())*150
    alupizzprice=int(alupizEntry.get())*200
    farmpizzprice=int(farmHoEntry.get())*350
    latepizzprice=int(lateSEntry.get())*450
    
    totalpizzaprice=otcpizzprice+cheeseburstprice+tonpizprice+latepizzprice+farmpizzprice+alupizzprice
    pizzaPriceEntry.delete(0,END)
    pizzaPriceEntry.insert(0,f"{totalpizzaprice} Rs")
    pizzaTax=totalpizzaprice*0.18 # 18% tax on pizza 
    pizzaTaxEntry.delete(0,END)
    pizzaTaxEntry.insert(0,f"{pizzaTax} Rs")
    
    # now for cold drinks 
    global cokeprice,fantaprice,limcaprice,thumbsprice,mountdewprice,mindraprice
    cokeprice=int(cokeEntry.get())*100
    fantaprice=int(fantaEntry.get())*100
    limcaprice=int(limcaEntry.get())*150
    thumbsprice=int(thumbsEntry.get())*180
    mountdewprice=int(mountDewEntry.get())*210
    mindraprice=int(minrAEntry.get())*175
    
    totalcolddrinksprice=cokeprice+fantaprice+limcaprice+thumbsprice+mindraprice+mountdewprice
    coldDrinksPriceEntry.delete(0,END)
    coldDrinksPriceEntry.insert(0,f"{totalcolddrinksprice} Rs")
    coldDrinksTax=totalcolddrinksprice*0.15 #15% tax on shakes 
    coldDrinksTaxEntry.delete(0,END)
    coldDrinksTaxEntry.insert(0,f"{coldDrinksTax} Rs")
    
    
    
    
    
    # now doing taxes as they are important 
    
    
    
    #Total bill down
    
    totalbill=totalburgerprice+totalcolddrinksprice+totalpizzaprice+burgertax+pizzaTax+coldDrinksTax
     
root=Tk()
root.title("Khati House")
root.geometry("1350x815")

#icon will be placed here 
headingLabel=Label(root,text="Khati House Billing System",font=("times new roman",30,"bold"),bg="gray20",fg="gold",bd=14,relief=GROOVE)# can be editable after also will ask from all 
headingLabel.pack(fill=X)
customer_details_frame=LabelFrame(root,text="Customer Details",font=("times new roman",14,"bold"),bd=8,fg="gold",relief=GROOVE,bg="gray20")
customer_details_frame.pack(fill=X)
nameLabel=Label(customer_details_frame,text="Name",font=("times new roman",14,"bold"),bg="gray20",fg="white")
nameLabel.grid(row=0,column=0,padx=20,pady=2)

nameEntry=Entry(customer_details_frame,font=("arial",14),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text="Phone Number",font=("times new roman",14,"bold"),bg="gray20",fg="white")
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=("arial",14),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billLabel=Label(customer_details_frame,text="Bill Number",font=("times new roman",14,"bold"),bg="gray20",fg="white")
billLabel.grid(row=0,column=4,padx=20,pady=2)
billEntry=Entry(customer_details_frame,font=("arial",14),bd=7,width=18)
billEntry.grid(row=0,column=5,padx=8)

seachButton=Button(customer_details_frame,text="SEARCH",font=("arial",14,"bold"),bd=7,width=10,command=search_bill)
seachButton.grid(row=0,column=6,padx=20,pady=2)

productsFrame=Frame(root)
productsFrame.pack()

#***********************************Burgers are starting from here *****************************************
burgerFrame=LabelFrame(productsFrame,text="Burgers",font=("times new roman",14,"bold"),bg="gray20",fg="gold",bd=7)
burgerFrame.grid(row=0,column=0)


vegburLabel=Label(burgerFrame,text="Aloo-Tikki Burger",font=("times new roman",14,"bold"),bg="gray20",fg="white")
vegburLabel.grid(row=0,column=0,pady=9,padx=10,sticky="w")
vegburEntry=Entry(burgerFrame,font=("times new roman",14,"bold"),width=10,bd=5)
vegburEntry.grid(row=0,column=1,pady=9,padx=10,sticky="w")
vegburEntry.insert(0,0)

cheesburLabel=Label(burgerFrame,text="Cheese Burger",font=("times new roman",14,"bold"),bg="gray20",fg="white")
cheesburLabel.grid(row=1,column=0,pady=9,padx=10,sticky="w")
cheesburEntry=Entry(burgerFrame,font=("times new roman",14,"bold"),width=10,bd=5)
cheesburEntry.grid(row=1,column=1,pady=9,padx=10,sticky="w")
cheesburEntry.insert(0,0)

KFCburLabel=Label(burgerFrame,text="KFC Burger",font=("times new roman",14,"bold"),bg="gray20",fg="white")
KFCburLabel.grid(row=2,column=0,pady=9,padx=10,sticky="w")
KFCburEntry=Entry(burgerFrame,font=("times new roman",14,"bold"),width=10,bd=5)
KFCburEntry.grid(row=2,column=1,pady=9,padx=10,sticky="w")
KFCburEntry.insert(0,0)


alloTikLabel=Label(burgerFrame,text="Crispy Corn Burger",font=("times new roman",14,"bold"),bg="gray20",fg="white")
alloTikLabel.grid(row=3,column=0,pady=9,padx=10,sticky="w")
alloTikEntry=Entry(burgerFrame,font=("times new roman",14,"bold"),width=10,bd=5)
alloTikEntry.grid(row=3,column=1,pady=9,padx=10,sticky="w")
alloTikEntry.insert(0,0)


butterLabel=Label(burgerFrame,text="Peri-Peri Burger",font=("times new roman",14,"bold"),bg="gray20",fg="white")
butterLabel.grid(row=4,column=0,pady=9,padx=10,sticky="w")
butterEntry=Entry(burgerFrame,font=("times new roman",14,"bold"),width=10,bd=5)
butterEntry.grid(row=4,column=1,pady=9,padx=10,sticky="w")
butterEntry.insert(0,0)


freshLabel=Label(burgerFrame,text="Double-Patty Burger",font=("times new roman",14,"bold"),bg="gray20",fg="white")
freshLabel.grid(row=5,column=0,pady=9,padx=10,sticky="w")
freshEntry=Entry(burgerFrame,font=("times new roman",14,"bold"),width=10,bd=5)
freshEntry.grid(row=5,column=1,pady=9,padx=10,sticky="w")
freshEntry.insert(0,0)

#***********************************Pizzas are starting from here *****************************************

pizzaFrame=LabelFrame(productsFrame,text="Pizza",font=("times new roman",14,"bold"),bg="gray20",fg="gold",bd=7)
pizzaFrame.grid(row=0,column=1)

otcLabel=Label(pizzaFrame,text="Margherita Pizza",font=("times new roman",14,"bold"),bg="gray20",fg="white")
otcLabel.grid(row=0,column=0,pady=9,padx=10,sticky="w")
otcEntry=Entry(pizzaFrame,font=("times new roman",14,"bold"),width=10,bd=5)
otcEntry.grid(row=0,column=1,pady=9,padx=10,sticky="w")
otcEntry.insert(0,0)

cheesburstLabel=Label(pizzaFrame,text="Cheese Burst Pizza",font=("times new roman",14,"bold"),bg="gray20",fg="white")
cheesburstLabel.grid(row=1,column=0,pady=9,padx=10,sticky="w")
cheesburstEntry=Entry(pizzaFrame,font=("times new roman",14,"bold"),width=10,bd=5)
cheesburstEntry.grid(row=1,column=1,pady=9,padx=10,sticky="w")
cheesburstEntry.insert(0,0)

tonPizLabel=Label(pizzaFrame,text="Tandori Pizza",font=("times new roman",14,"bold"),bg="gray20",fg="white")
tonPizLabel.grid(row=2,column=0,pady=9,padx=10,sticky="w")
tonPizEntry=Entry(pizzaFrame,font=("times new roman",14,"bold"),width=10,bd=5)
tonPizEntry.grid(row=2,column=1,pady=9,padx=10,sticky="w")
tonPizEntry.insert(0,0)

alupizLabel=Label(pizzaFrame,text="Corn-Capsicum Pizza",font=("times new roman",14,"bold"),bg="gray20",fg="white")
alupizLabel.grid(row=3,column=0,pady=9,padx=10,sticky="w")
alupizEntry=Entry(pizzaFrame,font=("times new roman",14,"bold"),width=10,bd=5)
alupizEntry.grid(row=3,column=1,pady=9,padx=10,sticky="w")
alupizEntry.insert(0,0)


farmHoLabel=Label(pizzaFrame,text="Farmhouse Pizza",font=("times new roman",14,"bold"),bg="gray20",fg="white")
farmHoLabel.grid(row=4,column=0,pady=9,padx=10,sticky="w")
farmHoEntry=Entry(pizzaFrame,font=("times new roman",14,"bold"),width=10,bd=5)
farmHoEntry.grid(row=4,column=1,pady=9,padx=10,sticky="w")
farmHoEntry.insert(0,0)


lateSLabel=Label(pizzaFrame,text="Italian Pizza",font=("times new roman",14,"bold"),bg="gray20",fg="white")
lateSLabel.grid(row=5,column=0,pady=9,padx=10,sticky="w")
lateSEntry=Entry(pizzaFrame,font=("times new roman",14,"bold"),width=10,bd=5)
lateSEntry.grid(row=5,column=1,pady=9,padx=10,sticky="w")
lateSEntry.insert(0,0)

#***********************************Cold Drinks are starting from here *****************************************

drinksAs=LabelFrame(productsFrame,text="Shakes",font=("times new roman",14,"bold"),bg="gray20",fg="gold",bd=7)
drinksAs.grid(row=0,column=2)

cokeLabel=Label(drinksAs,text="Chocolate",font=("times new roman",14,"bold"),bg="gray20",fg="white")
cokeLabel.grid(row=0,column=0,pady=9,padx=10,sticky="w")
cokeEntry=Entry(drinksAs,font=("times new roman",14,"bold"),width=10,bd=5)
cokeEntry.grid(row=0,column=1,pady=9,padx=10,sticky="w")
cokeEntry.insert(0,0)


fantaLabel=Label(drinksAs,text="Strawberry",font=("times new roman",14,"bold"),bg="gray20",fg="white")
fantaLabel.grid(row=1,column=0,pady=9,padx=10,sticky="w")
fantaEntry=Entry(drinksAs,font=("times new roman",14,"bold"),width=10,bd=5)
fantaEntry.grid(row=1,column=1,pady=9,padx=10,sticky="w")
fantaEntry.insert(0,0)


limcaLabel=Label(drinksAs,text="Kit-Kat ",font=("times new roman",14,"bold"),bg="gray20",fg="white")
limcaLabel.grid(row=2,column=0,pady=9,padx=10,sticky="w")
limcaEntry=Entry(drinksAs,font=("times new roman",14,"bold"),width=10,bd=5)
limcaEntry.grid(row=2,column=1,pady=9,padx=10,sticky="w")
limcaEntry.insert(0,0)


thumbsLabel=Label(drinksAs,text="Oreo",font=("times new roman",14,"bold"),bg="gray20",fg="white")
thumbsLabel.grid(row=3,column=0,pady=9,padx=10,sticky="w")
thumbsEntry=Entry(drinksAs,font=("times new roman",14,"bold"),width=10,bd=5)
thumbsEntry.grid(row=3,column=1,pady=9,padx=10,sticky="w")
thumbsEntry.insert(0,0)


mountDewLabel=Label(drinksAs,text="Blue-Berry",font=("times new roman",14,"bold"),bg="gray20",fg="white")
mountDewLabel.grid(row=4,column=0,pady=9,padx=10,sticky="w")
mountDewEntry=Entry(drinksAs,font=("times new roman",14,"bold"),width=10,bd=5)
mountDewEntry.grid(row=4,column=1,pady=9,padx=10,sticky="w")
mountDewEntry.insert(0,0)


minrALabel=Label(drinksAs,text="Butter-Scotch",font=("times new roman",14,"bold"),bg="gray20",fg="white")
minrALabel.grid(row=5,column=0,pady=9,padx=10,sticky="w")
minrAEntry=Entry(drinksAs,font=("times new roman",14,"bold"),width=10,bd=5)
minrAEntry.grid(row=5,column=1,pady=9,padx=10,sticky="w")
minrAEntry.insert(0,0)


billFrame=Frame(productsFrame,bd=8,relief=GROOVE)
billFrame.grid(row=0,column=3,padx=10)

billareaLabel=Label(billFrame,text="Bill Area",font=("times new roman",14,"bold"),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)
scrollbar=Scrollbar(billFrame,orient="vertical")
scrollbar.pack(side="right",fill=Y)
textArea=Text(billFrame,height=18,width=
              40,yscrollcommand=scrollbar.set)

textArea.pack()
scrollbar.config(command=textArea.yview)
billmenuFrame=LabelFrame(root,text="Bill Menu",font=("times new roman",14,"bold"),fg="gold",bd=8,relief=GROOVE,bg="gray20")
billmenuFrame.pack()


#*****************Final price of burgers******************
burgerPriceLabel=Label(billmenuFrame,text="Burger Price",font=("times new roman",14,"bold"),bg="gray20",fg="white")
burgerPriceLabel.grid(row=0,column=0,pady=9,padx=10,sticky="w")

burgerPriceEntry=Entry(billmenuFrame,font=("times new roman",14,"bold"),width=10,bd=5)
burgerPriceEntry.grid(row=0,column=1,pady=9,padx=10,sticky="w")

#*****************Final price of pizza******************

pizzaPriceLabel=Label(billmenuFrame,text="Pizza Price",font=("times new roman",14,"bold"),bg="gray20",fg="white")
pizzaPriceLabel.grid(row=1,column=0,pady=9,padx=10,sticky="w")
pizzaPriceEntry=Entry(billmenuFrame,font=("times new roman",14,"bold"),width=10,bd=5)
pizzaPriceEntry.grid(row=1,column=1,pady=9,padx=10,sticky="w")


#*****************Final price of Cold Drinks******************

coldDrinksPriceLabel=Label(billmenuFrame,text="Shakes Price",font=("times new roman",14,"bold"),bg="gray20",fg="white")
coldDrinksPriceLabel.grid(row=2,column=0,pady=9,padx=10,sticky="w")
coldDrinksPriceEntry=Entry(billmenuFrame,font=("times new roman",14,"bold"),width=10,bd=5)
coldDrinksPriceEntry.grid(row=2,column=1,pady=9,padx=10,sticky="w")

#*********************Taxes are very important ***************

#*****************Tax price of burgers******************
burgerTaxLabel=Label(billmenuFrame,text="Burger Tax",font=("times new roman",14,"bold"),bg="gray20",fg="white")
burgerTaxLabel.grid(row=0,column=2,pady=9,padx=10,sticky="w")

burgerTaxEntry=Entry(billmenuFrame,font=("times new roman",14,"bold"),width=10,bd=5)
burgerTaxEntry.grid(row=0,column=3,pady=9,padx=10,sticky="w")

#*****************Final price of pizza******************

pizzaTaxLabel=Label(billmenuFrame,text="Pizza Tax",font=("times new roman",14,"bold"),bg="gray20",fg="white")
pizzaTaxLabel.grid(row=1,column=2,pady=9,padx=10,sticky="w")
pizzaTaxEntry=Entry(billmenuFrame,font=("times new roman",14,"bold"),width=10,bd=5)
pizzaTaxEntry.grid(row=1,column=3,pady=9,padx=10,sticky="w")


#*****************Final price of Cold Drinks******************

coldDrinksTaxLabel=Label(billmenuFrame,text="Cold Drinks Tax",font=("times new roman",14,"bold"),bg="gray20",fg="white")
coldDrinksTaxLabel.grid(row=2,column=2,pady=9,padx=10,sticky="w")
coldDrinksTaxEntry=Entry(billmenuFrame,font=("times new roman",14,"bold"),width=10,bd=5)
coldDrinksTaxEntry.grid(row=2,column=3,pady=9,padx=10,sticky="w")


buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text="Total",font=("arial",16,"bold"),bg="gray20",fg="white",bd=5,width=9,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)
# *********************button**********
billButton=Button(buttonFrame,text="Bill",font=("arial",16,"bold"),bg="gray20",fg="white",bd=5,width=9,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)
# *******************email***************
emailButton=Button(buttonFrame,text="Email",font=("arial",16,"bold"),bg="gray20",fg="white",bd=5,width=9,pady=10,command=send_email)
emailButton.grid(row=0,column=2,pady=20,padx=5)
# ************Print**************
printButton=Button(buttonFrame,text="Print",font=("arial",16,"bold"),bg="gray20",fg="white",bd=5,width=9,pady=10,command=print_bill)
printButton.grid(row=0,column=3,pady=20,padx=5)
# ************clear**************
clearButton=Button(buttonFrame,text="Clear",font=("arial",16,"bold"),bg="gray20",fg="white",bd=5,width=9,pady=10,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=5)


root.mainloop()

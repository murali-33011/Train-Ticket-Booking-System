from tkinter import *
import sys
import string
import random
import mysql.connector
from time import sleep
import pandas as pd
import matplotlib.pyplot as plt

#GENERAL

print("WELCOME TO TRAIN TICKET BOOKING SERVICE")
print("________________________________________")
print("\nDefault location set to: Chennai")
print("Kindly answer all the following questions with proper format.\n")
mydb = mysql.connector.connect(host="localhost",user="root",password="murali")
cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS train")
cursor.execute("use train")
table="CREATE TABLE IF NOT EXISTS details(pnr VARCHAR(100),transaction_ID VARCHAR(100),name VARCHAR(100),phone int(20),password VARCHAR(100),train_name VARCHAR(100),deptime varchar(10),departure varchar(20),destination VARCHAR(20),traveldate DATE)"
cursor.execute(table)
#-----------------------------------------------------------------------------------------------
print("Select LOGIN if you'd like to view your ticket details\n")
sleep(0.50)
print("Select SIGNUP if you want to book a new ticket\n")
sleep(0.50)
ask=input("Would you like to Login or Signup: ")
for i in ask:
    if ask[0]=="L"or ask[0]=="l":
        username = input("Enter your username: ") 
        password = input("Enter your password: ")
        pnr = input("Enter your PNR no.")
        q="select * from details where name = %s and password = %s and pnr = %s"
        c=(username,password,pnr)
        cursor.execute(q,c)
        result = cursor.fetchall()
        if not result:
            print()
            print("Incorrect Credentials")
            print()
            
            ask=input("Would you like to Login/Signup: ")
            continue
        else:
            for x in result:
                print(x)
            break
        ask2=input("would you like to book another ticket") 
        if ask2[0]=="Y" or ask2[0]=="y":
            continue
        else:
            print("You are now exiting the program.")
            sys.exit()
            
#TICKET DETAILS!
            
name=input("Enter your name: ")
phone = int(input("Enter Phone no. (+91): "))
emailid=input("Enter your email adress: ")
password=input("Enter your password: ")
edd=input("Enter departure date (yyyy-mm-dd)~[eg. 2024-12-12]: ")  
print("|=======================|")
sleep(0.50)

#----=========-------------=========-----------============----------==========-----------============-----
citrain = {  "Mumbai" : ["1.Shatabdi Express","2.Rajdhani Express","3.Vande Bharat Express","4.Deccan Odyssey","5.Navyug Express"],
"Delhi" : ["1.Rajdhani Express", "2.Vande Bharat Express"],
"Banglore" : ["1.Shatabdi Express", "2.Rajdhani Express", "3.Vande Bharat Express", "4.Guruvayur Express","5.Navyug Express"],
"Kolkata" : ["1.Coromandel Express","2.Howrah SF Express"],
"Hyderabad" : ["1.Navyug Express", "2.Charminar Express"],
"Allahabad" : ["1.Navyug Express", "2.Howrah Express"],
"Jaipur" : ["1.Golden Chariot Express", "2.Jaipur SF Express"],
"Varanasi" : ['1.Guruvayur Express','2.Deccan Odyssey'],
"Kochi" : ["1.Guruvayur Express",'2.Ernakulam SF express'],
"Amritsar" : ["1.Navyug Express"],
"Kanyakumari" : ['1.Kanyakumari Vivek Express'] }

#------================------------==========----------===========----==========-----------=============----   
cdname,adname=[],[]

cdn=int(input("Enter no. of children (under 12 years of age) : "))
for i in range(1,cdn+1):
    cd1=input("Enter the name: ")
    cdname.append(cd1)
adno=int(input("Enter no. of adults: "))
for i in range(1,adno+1):
    adna=input("Enter the name: ")
    adname.append(adna)
print("|===============|")
sleep(0.50)
cities = ["Mumbai", "Delhi", "Bangalore", "Kolkata", "Hyderabad", "Allahabad", "Jaipur", "Varanasi", "Kochi", "Amritsar", "Kanyakumari"]
city_series = pd.Series(cities, index=["->"] * len(cities))
print(city_series)
while True:
    arci = input("Enter the city you intend to visit: ")
    arci = arci.lower()  # Convert the input to lowercase for case-insensitivity
    if arci[0:3] == "mum":
        arci = "Mumbai"
        break
    elif arci[0:3] == "del":
        arci = "Delhi"
        break
    elif arci[0:3] == "ban":
        arci = "Bangalore"
        break
    elif arci[0:3] == "kol":
        arci = "Kolkata"
        break
    elif arci[0:3] == "koc":
        arci = "Kochi"
        break
    elif arci[0:3] == "hyd":
        arci = "Hyderabad"
        break
    elif arci[0:3] == "all":
        arci = "Allahabad"
        break
    elif arci[0:3] == "jai":
        arci = "Jaipur"
        break
    elif arci[0:3] == "var":
        arci = "Varanasi"
        break
    elif arci[0:3] == "amr":
        arci = "Amritsar"
        break
    elif arci[0:3] == "kan":
        arci = "Kanyakumari"
        break
    else:
        print("Please type appropriately.")
print("You intend to visit:", arci)
trains=["Shatabdhi Express","Rajdhani Express","Vande Bharat Express","Deccan Odyssey","Golden Chariot Express","Guruvayur Express","Kanyakumari Vivek Express","Himsagar Express", "Navyug Express",
        "Coromandel Express","Howrah SF Express","Charminar Express","Jaipur SF Express","Ernakulam SF Express"]
train_series = pd.Series(citrain[arci], index=["->"] * len(citrain[arci]))

if arci in citrain:
    train_series = pd.Series(citrain[arci], index=["->"] * len(citrain[arci]))
    print(train_series)

    slctrain = int(input("Amongst the available trains, enter the corresponding number for the train you prefer:"))

    if slctrain >= 1 and slctrain <= len(citrain[arci]):
        selected_train = citrain[arci][slctrain - 1]
        print("You intend to take the train:", selected_train)
    else:
        print("Invalid train selection. Please choose a valid number.")
else:
    print("City not found in the list.")
slctrain = selected_train

print("|===============|")
sleep(0.50)
foodcst={"Dosa":40,"Idli":20,"Chapati":40,"Sandwich":30,"Special veg. Thali":100}
food = ["Dosa","Idli","Chapati","Sandwich","Special veg. Thali"]
foodslc={"Dosa":0,"Idli":0,"Chapati":0,"Sandwich":0,"Special veg. Thali":0}
foodtot={"Dosa":0,"Idli":0,"Chapati":0,"Sandwich":0,"Special veg. Thali":0}
print("Menu List: ")
food_cost_data = {"Food Name": ["Dosa", "Idli", "Chapati", "Sandwich", "Special veg. Thali"],"Cost": [40, 20, 40, 30, 100]}
food_df = pd.DataFrame(food_cost_data)
food_df.index = ['->'] * len(food_df)
print(food_df)
for i in food:
    print()
    print(i)
    foodslc[i]=int(input("How many of the item would you like ? ")) 
for i in food:
    foodtot[i] = (foodslc[i] * foodcst[i])
print()
sleep(0.50)
print("Processing your inputs.\n")
print("A 200 rupees payment will get you any requested beverage.")
sleep(0.50)
data = {"☕ Coffee": " ☕️","🍵 Tea": "      🍵","🥤 Soft Drink": "       🥤","💧 Water": "          💧"}
emoji_df = pd.DataFrame(data, index=["->"])
print(emoji_df)
print("To accept or reject the offer, enter yes or no, accordingly.")
bevask=input("Would you like to take up the offer? ")
if bevask[0]=="y" or bevask[0]=="Y" or bevask[0]=="o" or bevask[0]=="O":
    bev=40
    print("Beverage offer accepted (Amount will be directly added to the Bill). ")
else:
    bev=0
    print("Beverage offer declined (No extra Amount will be added to Bill). ")
print("|===============|")
normalcst={"Mumbai":540,"Delhi":1155,"Banglore":240,"Kolkata":710,"Hyderabad":300,"Allahabad":1700,"Agra":1200,"Jaipur":740,"Varanasi":800,"Kochi":220,"Amritsar":1100,"Kanyakumari":310}
print("Cost for Normal Sleeper Berth: ")
print(arci,normalcst[arci])
accst={"Mumbai":1460,"Delhi":2065,"Banglore":1880,"Kolkata":2200,"Hyderabad":1700,"Allahabad":3450,"Agra":1700,"Jaipur":1240,"Varanasi":1300,"Kochi":710,"Amritsar":1600,"Kanyakumari":800}
print("Cost for A/C Sleeper Berth:")
print(arci,accst[arci])
print()
sleep(0.50)
print("To choose a normal or air-conditioned sleeper berth, type accordingly.")
clas=input("would you like to travel in normal sleeper or A/C sleeper?")

if clas[0] == "n" or clas[0] == "N":
    bs1="Normal Sleeper"
    citycst=normalcst
elif clas[0]=="a" or clas[0] == "A":
    bs1="A/C Sleeper"
    citycst=accst
print(bs1,"Selected")

#PRINTING DETAILS

print( "Please wait for your inputs to be processed.")
sleep(1.00)
print("System operating")
print("Loading a bill page in")
for i in range(3,0,-1):
    sleep(1)
    print(i)
print("======================================================")
print("Please confirm the entire cost of your bill.")
sleep(1)
print("======================================================")
print("TICKET HOLDER NAME: ", name)
print("Date of Departure : ", edd)
print("Train Selected : ", slctrain)
print("City of Departure : Chennai")
print("City of Arrival : ", arci)
print()
print("No. of adults: ",adno)
for i in adname:
    print(i)
print("No. of childrens: ",cdn)
for i in cdname:
    print(i)
print()
s=0
for i in foodtot:
    print (i,":",foodtot[i])
for i in foodtot:
           tot=foodtot[i]
           s=s+tot
sleep(0.50)         
print("Food Total: ",s+bev)
print()
print("Total of Children ticket(s):")
print("No. of Children X Children Cost Tickets")
slcitycst=citycst[arci]
if cdn!=0:
    cdamount=((cdn) * (slcitycst) - 100)
else:
    cdamount=((cdn) * (slcitycst)) 
print( cdamount )
print("Total of Adults ticket(s):")
print("No. of Adults X Adult Cost Tickets")
adamount= (adno) * (slcitycst)  
print( adamount )
print()
sleep(1)
print("TRAIN TICKET TOTAL")
print()
sleep(0.50)
print("Total Food Amount + Children Tickets + Adult Tickets")
print((s+bev) + (cdamount) +(adamount), "Rs.")

#TKINTER BILLING PAGE

window=Tk()
window.title("Payment page")
window.config(width=500,height=500)
lbl=Label(window, text= "Choose method of payment",font=("Helvetica",21))
lbl.place(x=60,y=50)
amt ="Amount : ₹" , (s+bev) + (cdamount) +(adamount)
def net():
    window2=Tk()
    window2.title("Net Banking")
    window2.config(width=500,height=500)
    am = Label(window2, text =  amt,font = ("Helvetica",18))
    am.place(x=170,y=350)
    acc= Label(window2, text = "Account No.")
    ba = Label(window2, text = "Bank Name :")
    na = Label(window2, text = "User Name :")
    pa = Label(window2, text = "Password : ")
    acc.place(x=125,y=100)
    ba.place(x=130,y=150)
    na.place(x=130,y=200)
    pa.place(x=140,y=250)
    e1=Entry(window2)
    e2=Entry(window2)
    e3=Entry(window2)
    e4=Entry(window2)
    e1.place(x=200,y=100)
    e2.place(x=200,y=150)
    e3.place(x=200,y=200)
    e4.place(x=200,y=250)
    con = Button(window2, text = "Next",command=next)
    con.place(x=420,y=450)
  
def upi():
    window3=Tk()
    window3.title(" 🪪 Unified Payment Services")
    window3.config(width=300,height=300)
    am = Label(window3, text =  amt ,font = ("Helvetica",15))
    am.place(x=60,y=180)
    upid = Label(window3, text = "Enter UPI ID :")
    pa = Label(window3, text = "Password :")
    upid.place(x=25,y=100)
    pa.place(x=25,y=150)
    e1=Entry(window3)
    e2=Entry(window3)
    e1.place(x=100,y=100)
    e2.place(x=100,y=150)
    con = Button(window3, text = "Next",command=next)
    con.place(x=250,y=270)

def card():
    window4=Tk()
    window4.title("💳 Card")
    window4.config(width=500,height=500)
    am = Label(window4, text =  amt,font = ("Helvetica",18))
    am.place(x=170,y=350)
    na = Label(window4, text  = "Name: ")
    cno = Label(window4,text = "Card no.")
    cvv = Label(window4, text = "CVV no.")
    exp = Label(window4, text = "Expiry date: ")
    na.place(x=125,y=100)
    cno.place(x=125,y=150)
    cvv.place(x=125,y=200)
    exp.place(x=125,y=250)
    e1 = Entry(window4)
    e2 = Entry(window4)
    e3 = Entry(window4)
    e4 = Entry(window4)
    e1.place(x=200,y=100)
    e2.place(x=200,y=150)
    e3.place(x=200,y=200)
    e4.place(x=200,y=250)
    con = Button(window4, text = "Next",command=next)
    con.place(x=420,y=450)

def next():
     window5=Tk()
     window5.title("☑ Payment Succesfull")
     window5.config(width=500,height=500)
     tick = Label(window5, text = " ✅",font=("Helvetica",48))
     tick.place(x=200,y=200)

bt1 = Button(window, text=" 🏦 Net Banking", fg= "Black",command = net)
bt1.place(x=200,y=190)
bt2=Button(window, text = " 🪪 UPI", fg="Orange",command = upi)
bt2.place(x=225,y=240)
bt3=Button(window, text = " 💳 Card",fg="Blue",command = card )
bt3.place(x=220,y=290) 
line = Label(window, text = "__________________________________________________________________________________________________________")
line.place(x=0,y=450)
Ban1 = Label(window, text = "Powered by", font = ("calibri",8))
Ban1.place(x=20,y=468)
Ban2 = Label(window, text = "Tkinter",font = ("Helvetica",8))
Ban2.place(x=85,y=480)
Ban3 = Label(window, text = "✅ Norton",font = ("Helvetica",10))
Ban3.place(x=410,y=468)
window.mainloop()

#PRINTING TICKET

h = random.randint(1, 25)
m = random.randint(10, 59)
hm_str = str(h) + ":" + str(m)
print("Printing your Ticket")
sleep(0.50)

print("|===========================================|")
print("\t\t\t\t\t\t","HAVE A SAFE TRIP")
print("\t\t\t\t\t\t","_______________")
print()
print("mail: ",emailid)
print("phone no. : ",phone)
print()
N = 9
res = ''.join(random.choices(string.ascii_uppercase , k=N))
res=str(res)
print("\t\t\t\t\t\t\t\t\t","FROM: ")
print("PNR NO. : "  + res,"\t\t\t\t\t\t\t", "Chennai")
r1 = random.randint(92351672, 99273617127)
r1=str(r1)
print("TRANSACTION ID : " + r1)
print()
print("TICKET HOLDER")
print(name)
print("\t\t\t\t\t\t\t\t\t\t","TO:")
print("Passengers name:","\t\t\t\t\t\t\t\t\t",arci)
for i in cdname:
    print(i)
for i in adname:
    print(i)
print()
print("TOTAL BILL: ",((s+bev) + (cdamount) +(adamount)),"Rs.","\t\t\t\t\t\t\t\t","Date of departure: ",edd)
print()
print("TRAIN NAME: ",slctrain, "{",  bs1  ,"}")
print("Departure Time :",hm_str )
print()
print("🚄🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐🚐")

tnames=adname+cdname
depcity="chennai"   
sql = "INSERT INTO details (pnr,transaction_ID,name,phone,password,train_name,deptime,departure,destination ,traveldate ) VALUES (%s,%s,%s, %s, %s,%s,%s,%s,%s,%s)"
for i in tnames:
    val = (res, r1, i, phone, password, slctrain, hm_str, depcity, arci, edd)
    cursor.execute(sql,val)
mydb.commit()
sleep(0.50)
print("Here are some statistics of")
print("Travel Trends: Passenger Count by Destination in the Last 2 Months")
cursor.execute("USE train")
query = "SELECT destination, COUNT(*) AS passenger_count FROM details GROUP BY destination"
cursor.execute(query)
data = cursor.fetchall()
df = pd.DataFrame(data, columns=["Destination", "Passenger Count"])
plt.figure(figsize=(10, 6))
plt.bar(df["Destination"], df["Passenger Count"])
plt.xlabel("Destination City")
plt.ylabel("Passenger Count (in thousands)")
plt.title("Passenger Count by Destination City")
plt.xticks(rotation=45, ha="right")
plt.show()

print("You are now exiting the program")
print("Thank you")
sleep(1)
sys.exit()
#END OF PROGRAM

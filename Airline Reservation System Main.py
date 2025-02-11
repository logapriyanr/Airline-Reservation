import random
import mysql.connector
conn=mysql.connector.connect(host='localhost',user="root",passwd='root',database='Airline')
mycursor=conn.cursor(buffered=True)

#Function To Create Tables

def create_tables():                                             # this function creates all the tables in the database airline, if they are not already created.

    qury='''create table flights(SerialNo int, Departure varchar(20), Arrival varchar(20), DepartureDate varchar(20),
    ArrivalDate varchar(20), DepartureTime varchar(10), ArrivalTime varchar(10), Price int)'''
    try:
        mycursor.execute(qury)
    except:
        pass

    qury0='''create table passenger(PNR int, SerialNo int, Name varchar(10), Age int, Gender varchar(10),Mobile int)'''
    try:
        mycursor.execute(qury0)
    except:
        pass
    mycursor.execute("select * from flights")
    check = mycursor.fetchall()                               # taking legth of data in table Flights
    
    if len(check) == 0:                                       # if table flights is empty uploading the flight list, else pass
        qury1="""insert into flights values(1,'Abu Dhabi','Delhi','2021-01-01','2021-01-01','07:20','09:35', 1700),
        (2,'Abu Dhabi','New York','2021-02-05','2021-02-06','13:50','15:25',2700),
        (3,'Abu Dhabi','London','2021-04-19','2021-04-20','21:35','14:10',2000),
        (4,'Rio','Cape Town','2021-06-30','2021-07-01','18:15','12:35',2350),
        (5,'Chicago','Paris','2021-08-19','2021-08-19','01:20','08:12',2100),
        (6,'New York','London','2021-02-21','2021-02-22','02:00','12:20',3150),
        (7,'Wasgington','Las Vegas','2021-12-16','2021-12-16','11:55','18:10',3280),
        (8,'Italy','Abu Dhabi','2021-07-18','2021-07-18','02:30','14:10',4100),
        (9,'Dubai','Maldives','2021-05-05','2021-05-06','21:30','06:25',2400),
        (10,'Madrid','Rome','2021-02-14','2021-02-14','08:30','11:00',1300)"""
        mycursor.execute(qury1)
    else:
        pass

    conn.commit()

create_tables()

e = []

#Function to Register/Log-In

def Loginpage():
    print()
    print("<<<<<<<< Welcome to Jet Sky Airways >>>>>>>>".center(48))
    print()
    print("╔═════════════════════════╗".center(47))
    print("  1. Login".center(30))
    print("  2. Register".center(34))
    print("╚═════════════════════════╝".center(47))
    print()
    
    acc = input("Enter Your Choice (1/2): ")
    while True:
        if acc=='2':
            nam = input("Please Enter Your Name: ")
            mob = int(input("Please Enter Your Mobile No: "))
            mail = input("Please Enter Your Email: ")
            e.append(mail)
            passwd = input("Please Enter Your Password: ")

            print("\n-------YOUR ACCOUNT IS CREATED SUCCESSFULLY-------")
            print()
            break
                
        else:
            email = input("Please Enter Your Email: ")
            e.append(email)
            pas = input("Please Enter Your Password: ")
            if pas=='123' or passwd:
                print("\n-------LOGIN SUCCESSFUL-------")
                print()
                break
            else:
                print("Wrong Password... ")
                print("Please Try Again")
                print()
            
#Menu Function  

def Menu():
    print("╔══════════════════════《✧》══════════════════════╗")
    print("","*"*49)
    print(" WELCOME TO JET SKY AIRWAYS ".center(50))
    print("","*"*49)
    print()
    print(" MAIN MENU")
    print()
    print(" 1. Book Flights")
    print(" 2. Manage Booking")
    print(" \t a. View Booking")
    print(" \t b. Cancel Booking")
    print(" 3. Check Your Flight Status")
    print(" 4. Help")
    print(" 5. Exit")
    print()
    print("","*"*49)
    print("╚══════════════════════《✧》══════════════════════╝")
    

def MenuManage():
    print("a. View Booking")
    print("b. Cancel Booking")
    print("c. Back to Main Menu")

dep=[]
arr=[]
passenger=[]
n=[]
nam=[]
ag=[]
gend=[]
mob=[]
PNR=random.randint(10000,99999)
depp= []
arrt= []
depd=[]
arrd=[]
payment=[]
cabin=[]
pas=[]

#Function to Book Reservation

def Bookflights():

    #Searching For Flights To Book
    
    def booking():
        print("-"*55)
        print("OUR ORIGIN:   Abu Dhabi   /  Paris   / New Zealand /    Rio    / Chicago / New York  / Washington DC /   Italy   /  Dubai   / Madrid /")
        print("OUR DESTINATIONS:  Delhi / New York /    London   / Cape Town /  Paris  /   London  /   Las Vegas   / Abu Dhabi / Maldives /  Rome  /")
        print("-"*55)
        
        flights=[]
        print('    ',"Please Choose Your Desired Origin and their Corresponding Destination")
        print()
        departure = input("Enter your Departure: ").title()
        arrival = input("Enter your Arrival: ").title()
        mycursor.execute("select * from flights where Departure= %s and Arrival= %s ",(departure,arrival))
        d=mycursor.fetchall()
        for i in d:
            flights.append(list(i))

        if len(flights) == 0:
                print('\n \t *** Sorry... no flights available this route *** \n \t You may consider connecting flights to the destination')
                booking()
        else:
            print("\nHere are the Details of Your Flight: \n")
            for flight in flights:
                print("SL.No| Departure| Arrival| DepartureDate| ArrivalDate| DepartureTime| ArrivalTime| Price")
                print()
                print("   ",flight)
                print()
        
        contr=input("Would you like to proceed(Yes/No): ")     # .lower() function gets the input string converted into lower case....
        if contr == 'no':
            booking()
        elif contr == 'yes':
            pass
            
        dep.append(departure)
        arr.append(arrival)
        
        conn.commit()
            
    booking()

    print()
    #contu=input("Would you like to Confirm your booking(Yes/No): ")
    #for i in contu:
     #   if contu=='no' or contu=='No':
      #      booking()
       # else:
        #    break

    #Creation Of Passenger Details
    
    def pass_data():
        for i in range (passen):
            no=int(input("Enter Serial No of passenger: "))
            name=input("Enter the name of the passenger: ").title()
            age=int(input("Enter the age of the passenger: "))
            gender=input("Male/Female: ").title()
            mobile=input("Enter Mobile No.: ")
            d=[no,name,age,gender,mobile]
            passenger.append(d)

            n.append(no)
            nam.append(name)
            ag.append(age)
            gend.append(gender)
            mob.append(mobile)
            data=[PNR,no,name,age,gender,mobile]
            qu="insert into passenger values(%s,%s,%s,%s,%s,%s)"
            mycursor.execute(qu,data)
        q= 0
        print()
        print("The Details of the passengers are: ")
        print()
        print("Total Ticket: ",passen)
        for p in range(1,passen+1):
            print('*'* 45)
            print("\n\t Ticket: ",p)
            print("\n\t Name: ",nam[q])                                # if q is 0, selects 0th value from 'nam'
            print("\n\t Age: ", ag[q])
            print("\n\t Gender: ",gend[q])                             # if q is 0, selects 0th value from 'gend'
            print("\n\t Mobile No.: ",mob[q])
            print('*'* 45)
            q+=1
            
        conn.commit()
    
    passen=int(input("Enter No. of Passesngers: "))    
    pass_data()

    pas.append(passen)

    #Updating of Passenger Details

    def updatepass():
        try:
            q="select * from passenger"
            mycursor.execute(q)
            data=mycursor.fetchall()
            print(data)
            A= input("Enter name of passenger you wish to update")
            for i in data:
                i=list(i)
                if i[1]==A:
                    y=input("Enter Section to rectify(Name/Age/Gender/Mob): ")
                    if y=="Name":
                        i[1]=input("Enter New Name: ")
                        i[1]=i[1].upper()
                    if y=="Age":
                        i[2]=input("Enter New Age: ")
                    elif y=="Gender":
                        i[3]=input("Enter New Gender: ")
                        i[3]=i[3].upper()
                    elif y=="Mob":
                        i[4]=input("Enter New MobileNo: ")
                    else:
                        print("Invalid option")
            
                cmd="update passenger set Name=%s, Age=%s, Gender=%s, Mobile=%s where Name=%s"
                vale=(i[1],i[2],i[3],i[4],i[1])
                mycursor.execute(cmd,vale)
                
                conn.commit()
                
            print()
            q1="select * from passenger"
            mycursor.execute(q1)
            data1=mycursor.fetchall()
            print(data1)
        except:
            print("Error")

        print()
        
        conti=input("Would you like to proceed(Yes/No): ")
        for i in conti:
            if conti=='no' or conti=='No':
                break
            else:
                break
        
    print()
    
    conti=input("Would you like to Confirm(Yes/No): ")
    for i in conti:
        if conti=='no' or conti=='No':
            updatepass()
        else:
            break

    #Cabin Selection

    print("\nChoose your Cabin: ")
    print("-"*45)
    print("   1.Economy Class")
    print("   2.Business Class (+20% CHARGES)")
    print("   3.First Class (+40% CHARGES)")

    print()


    def fl_time():
        mycursor.execute("Select DepartureDate from flights where Departure= %s and Arrival= %s ",(dep[0],arr[0]))
        for q in mycursor:
            depd.append(list(q))
        mycursor.execute("Select ArrivalDate from flights where Departure= %s and Arrival= %s ",(dep[0],arr[0]))
        for b in mycursor:
            arrd.append(list(b))
        mycursor.execute("Select DepartureTime from flights where Departure= %s and Arrival= %s ",(dep[0],arr[0]))
        for g in mycursor:
            depp.append(list(g))
        mycursor.execute("Select ArrivalTime from flights where Departure= %s and Arrival= %s ",(dep[0],arr[0]))
        for h in mycursor:
            arrt.append(list(h))
            
        conn.commit()

    cab=input("Enter your Cabin(Economy/Business/First): ")

    print()


    if cab=='Economy' or cab=='Economy Class':
        fl_time()
        mycursor.execute("Select (Price) * %s from flights where Departure= %s and Arrival = %s ",(passen,dep[0],arr[0]))
        q= 0
        print("The Details of the passengers are: ")
        print()
        print("Total Ticket: ",pas[0])
        print()
        for p in range(1,(pas[0]+1)):
            print("Ticket: ",p)
            print()
            print("Name:",nam[q],'   ',"Age:", ag[q],'   ',"Gender:",gend[q],'   ',"Mobile No.:",mob[q],'   ',"Departure Date= ",depd[0])
            print()
            print("Departure=",dep[0],'   ','Arrival=',arr[0],'   ','Departure Time=',depp[0],'   ','Arrival Time=',arrt[0],'   ',"Arrival Date=",arrd[0])
            print()
            print("Cabin= Economy Class")
            print()
            q+=1
            
        for f in mycursor:
            payment.append(f)
            print("Your Final Charges is: AED",f)
        print()
            

    elif cab=='Business' or cab=='Business Class':
        fl_time()
        mycursor.execute("Select (Price + Price*0.20) * %s from flights where Departure= %s and Arrival = %s ",(passen,dep[0],arr[0]))
        q= 0
        print("The Details of the passengers are: ")
        print()
        print("Total Ticket: ",pas[0])
        print()
        for p in range(1,(pas[0]+1)):
            print("Ticket: ",p)
            print()
            print("Name:",nam[q],'   ',"Age:", ag[q],'   ',"Gender:",gend[q],'   ',"Mobile No.:",mob[q],'   ',"Departure Date= ",depd[0])
            print()
            print("Departure=",dep[0],'   ','Arrival=',arr[0],'   ','Departure Time=',depp[0],'   ','Arrival Time=',arrt[0],'   ',"Arrival Date=",arrd[0])
            print()
            print("Cabin= Business Class")
            print()
            q+=1
            
        for f in mycursor:
            payment.append(f)
            print("Your Final Charges is: AED",f)
        print()
            

    elif cab=='First' or cab=='First Class':
        fl_time()
        mycursor.execute("Select (Price + Price*0.40) * %s from flights where Departure= %s and Arrival = %s ",(passen,dep[0],arr[0]))
        q= 0
        print("The Details of the passengers are: ")
        print()
        print("Total Ticket: ",pas[0])
        print()
        for p in range(1,(pas[0]+1)):
            print("Ticket: ",p)
            print()
            print("Name:",nam[q],'   ',"Age:", ag[q],'   ',"Gender:",gend[q],'   ',"Mobile No.:",mob[q],'   ',"Departure Date= ",depd[0])
            print()
            print("Departure=",dep[0],'   ','Arrival=',arr[0],'   ','Departure Time=',depp[0],'   ','Arrival Time=',arrt[0],'   ',"Arrival Date=",arrd[0])
            print()
            print("Cabin= First Class")
            print()
            q+=1
            
        for f in mycursor:
            payment.append(f)
            print("Your Final Charges is: AED",f)
        print()

    cabin.append(cab)

    #Payment
    
    print('\n')
    print('-'*45)
    print('\t *** Payment page ***')
    print("\nSelect Your Payment Method")
    print("1. Google Pay")
    print("2. Credit Card")
    print("3. Debit Card")
    print()

    pay1 = int(input("Enter Your Payment Method(1/2/3): "))
    print()

    if pay1==1:
        print("~~~~~~~~~~~~~~  Google Pay  ~~~~~~~~~~~~~~~~")
        print("Pay AED",payment[0])
        pay2= input("To continue press (P): ")
        otp= int(input("Enter the recieved otp: "))
        print("---------Transaction Successful------------")
        print("**************THANK YOU**************")
        print()

    if pay1==2 or pay1==3:
        print("||||||||||||||||  Card Payment  |||||||||||||||||")
        print("Pay AED",payment[0])
        cardno= int(input("Enter Your Card No: "))
        cvv= int(input("Enter Your CVV: "))
        otp1= int(input("Enter the recieved otp: "))
        print("---------Transaction Successful------------")
        print("**************THANK YOU**************")
        print()


    see=input("If you want to recieve the ticket(Y/N): ")
    if see=='Y':
        print('-'*45)
        print("\nYour Ticket will be sent to",e[0],'\n')
        print('-'*45)
    else:
        pass

    print()

    #Displaying Of The Final Reservation
    
    q= 0
    print("The Details of the passengers are: ")
    print()
    print("Your Reservation Number is -",PNR)
    print()
    print("Total Ticket: ",passen)
    print()
    for p in range(1,passen+1):
        print("Ticket: ",p)
        print()
        print("Name:",nam[q],'   ',"Age:", ag[q],'   ',"Gender:",gend[q],'   ',"Mobile No.:",mob[q],'   ',"Departure Date= ",depd[0])
        print()
        print("Departure=",dep[0],'   ','Arrival=',arr[0],'   ','Departure Time=',depp[0],'   ','Arrival Time=',arrt[0],'   ',"Arrival Date=",arrd[0])
        print()
        print("Cabin=",cab)
        print()
        q+=1
    print("Total Amount: AED",payment[0])

    print('\n   Thank You for traveling with us')
    
    print("\n     *** JET SKY AIRWAYS ***\n\n\tYour Magic Carpet ")
    
    print("\n\t HAVE A NICE DAY \n\n")
    
    print('-'*100)
    print('-'*100)
    print()
    print()
    
    user=input(("TO CONTINUE PRESS 'ENTER'"))
    
    conn.close

#Function To View The Reservation

def Viewbooking():
    if pas!=[]:
    
        pnr=int(input("Enter Your Reservation Reference:"))
        print()
        depart=input("Enter Your Depature Destionation:")
        print()
        arrive=input("Enter Your Arrival Destionation:")

        print()

        q= 0
        print("The Details of the passengers are: ")
        print()
        print("Your Reservation Number is -",PNR)
        print()
        print("Total Ticket: ",pas[0])
        print()
        for p in range(1,(pas[0]+1)):
            print("Ticket: ",p)
            print()
            print("Name:",nam[q],'   ',"Age:", ag[q],'   ',"Gender:",gend[q],'   ',"Mobile No.:",mob[q],'   ',"Departure Date= ",depd[0])
            print()
            print("Departure=",dep[0],'   ','Arrival=',arr[0],'   ','Departure Time=',depp[0],'   ','Arrival Time=',arrt[0],'   ',"Arrival Date=",arrd[0])
            print()
            print("Cabin=",cabin[0])
            print()
            q+=1
        print("Total Amount: AED",payment[0])
    else:
        print("   ","Sorry, No Bookings Available")
    
    print()

#Function To Delete Your Reservation

def Cancelbooking():
    
    user=input("Do you Wish to Cancel the Reservation(Yes/No):")
    print()
    if user=='yes' or user=='Yes':
        print("We Are Sorry To See You Leave")
        print("Your Cancelation Of your Ticket Will Be Sent To Your Mail-",e[0])
        print("Have A Nice Day :))")
        print()
    else:
        print("Having Second Thoughts???")
        print()
        print("No Problem....")
        print()
        print("You Will Be Redirected to Our Main Page")
        print()
    
#Function To Search Whether Flights are Deyaled Or ON-Time

def Flightstatus():
    depart = input("Please Enter Your Departure: ")
    mycursor.execute('''select SerialNo,Departure,Arrival,DepartureDate,
ArrivalDate,DepartureTime,ArrivalTime from flights where Departure = %s ''',(depart,))
    print("Here are the details of your Flight-----")
    for a in mycursor:
        print(a)
    print()

    conn.commit()
    conn.close()


#Help Function 

def Help():
    print('\n We reccoment you to Check for available flights first.\n\n Then book your flight by selecting " Book Flights" option')
    print('\n If you still have any Queries')
    print("\n Contact us - 02-555-9999")
    print("\n           OR".center(20))
    print("\n Mail Us - helpline@JSAirways.com\n\n")


# Menu Program To Call All Functions

Loginpage()
while True:
    Menu()
    ch=input("Enter your Choice (1/2/3/4/5): ")
    if ch=="1":
        Bookflights()
    elif ch=="2":
        while True:
            MenuManage()
            ch1=input("Enter choice a/b/c: ")
            if ch1 in ['a','A']:
                Viewbooking()
            elif ch1 in ['b','B']:
                Cancelbooking()
            elif ch1 in ['c','C']:
                print("Back to the main menu")
                break
            else:
                print("Invalid choice")
    elif ch=="3":
        Flightstatus()
    elif ch=="4":
        Help()
    elif ch=="5":
        print('\n  Visit us when you plan to Travel')
        print("\n     *** JET SKY AIRWAYS ***\n\n\tYour Magic Carpet ")
        print("\n\t HAVE A NICE DAY \n\n")
        print('-'*100)
        print('-'*100)
        break
    else:
        print("Wrong Choice Entered")

import mysql.connector
import textwrap
pass1 = "yashmayash"   #enter your password

con=mysql.connector.connect(host="localhost",password=pass1,user="root",database = "BOOKMYBED")
cursor=con.cursor()

# validations:
lyes = ["YES","Yes","Y","y","yes","yeah","Yep","yep","Yeah"]
lno = ["NO","N","n","no","No","Nope","nope"]

def reportgov():
        
    import numpy as np
    import matplotlib.pyplot as plt
    cursor.execute("select Center_Name, beds from quarantine_centers")
    result = cursor.fetchall
    Centre_Name = []
    Beds = []
    for i in cursor:
        Centre_Name.append(i[0])
        Beds.append(i[1])

    plt.bar(Centre_Name, Beds)
    plt.xlabel("Centre Name")
    plt.ylabel("NO. OF BEDS AVAILABLE")
    plt.show()

# def reportpat():
#     pass

def idgenerator():
        try:
            f = open("patientidcache.txt","r")
            t = int(f.read())
            t +=1
            f.close()
            f = open("patientidcache.txt","w")
            f.write(str(t))
            f.close()
            return t
        except IOError:
            f = open("patientidcache.txt","w")
            t = 1
            f.write(str(t))
            f.close()
            return t

def QCentres():

    con=mysql.connector.connect(host="localhost",password=pass1,user="root",database = "BOOKMYBED")
    cursor=con.cursor()

    cursor.execute("select * from QUARANTINE_CENTERS order by CENTER_ID asc")
    result = cursor.fetchall()

    print()
    print("List of Quarantine Centres : ")
    print("{:^10}".format(""))
    print("="*163)
    print("{:^10}{:^36}{:^50}{:^11}{:^20}{:^18}{:^16}".format("Center ID","Place Name","Address","Mobile No","Person in charge","No. of beds available","Starting Price"))
    print("="*163)
    for i in result:
        x,y,z,d,e,f,v=i
        z = textwrap.shorten(z, width=45, placeholder="...")
        print("{:^10}{:^36}{:^50}{:^10}{:^20}{:^18}{:^16}".format(x,y,z,d,e,f,v))            #163 spaces
    print("="*163)
    con.close()

def addPat():
    con=mysql.connector.connect(host="localhost",password=pass1,user="root",database = "BOOKMYBED")
    cursor=con.cursor()
    try:
        e = input("Enter the Center ID where you want a Bed: ")
        z = "select beds from quarantine_centers where center_id ='{}'".format(e)
        cursor.execute(z)
        result = cursor.fetchall()
        bedno = (int(result[0][0]))
        if bedno == 0:
            print("No free beds ... sorry ")
            print("Please choose another center.")
            addPat()
        else:
            while True:
                x = input("Enter the Patient's Name: ")
                y = int(input("Enter the Patient's Mobile No.: "))
                if len(str(y)) != 10:
                    print(" Please enter valid Mobile No. ")
                    print()
                    print("Kindly re-enter the details")
                    print()
                    continue

                p = input("Enter the Guardian Name: ")
                d = int(input("Enter the Guardian's Mob no: "))
                if len(str(d)) != 10:
                    print(" Please enter valid Mobile No. ")
                    print()
                    print("Kindly re-enter the details")
                    print()
                    continue
                break

            
            print()    
            print("Please recheck the Details you have entered!")
            print()    
            print("If you have checked the details, type Yes.")
            check = input("If you want to re*enter, type No : ")
            i = 1
            while i != 0:
                if check in lyes:
                    i=0
                elif check in lno:
                    print("Kindly re*enter the details")
                    addPat()
                else:
                    "Please enter valid Data"
            l = "P" + str(idgenerator())   
            def decreasingbed(center_id):
                
                z = "select beds from quarantine_centers where center_id ='{}'".format(center_id)
                cursor.execute(z)
                result = cursor.fetchall()
                bedno = (int(result[0][0]))
                bedno -= 1
                cursor.execute("update quarantine_centers set beds= '{:d}' where center_id = '{}'".format(bedno,center_id))

                con.commit()
            

            decreasingbed(e)
            t = "insert into patient values('{}','{}','{}','{}','{}','{}','{}')".format(l,x,y,p,d,e,"Registered")
            cursor.execute(t)
            con.commit()

            patID = l                
            PatientID(patID)
    except:
            print("Wrong Centre ID")
            print("Please enter again")
            addPat()

    
def PatientID(patID):
    
    print()
    print()
    print("$"*163)
    print("$"*163)

    print("$"*50,end = "")
    print(" "*63,end = "")
    print("$"*50)
    print("$"*50,end = "")
    print(" "*63,end = "")
    print("$"*50)

    patientid = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                     Your PATIENT ID = {s}                     $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$".format(s = patID)
    print(patientid)

   
    print("$"*50,end = "")
    print(" "*63,end = "")
    print("$"*50)
    print("$"*50,end = "")
    print(" "*63,end = "")
    print("$"*50)
    print("$"*163)
    print("$"*163)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def myDetails():
    
    con=mysql.connector.connect(host="localhost",password=pass1,user="root",database = "BOOKMYBED")
    cursor=con.cursor()
    try:
        


        x = input("Enter Patient ID to see your details: ")

        t = "select * from QUARANTINE_CENTERS,patient where patient.Center_Id = QUARANTINE_CENTERS.Center_Id and patient_id = '{}'".format(x)
        
        cursor.execute(t)
        result = cursor.fetchall()
        # print(result)
        # print()
        x,y,address,d,e,f,h,PId,i,j,k,l,a,b=result[0]

        print("""
                                                
                                                ███╗   ███╗██╗   ██╗    ██████╗ ███████╗████████╗ █████╗ ██╗██╗     ███████╗
                                                ████╗ ████║╚██╗ ██╔╝    ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██║██║     ██╔════╝
                                                ██╔████╔██║ ╚████╔╝     ██║  ██║█████╗     ██║   ███████║██║██║     ███████╗
                                                ██║╚██╔╝██║  ╚██╔╝      ██║  ██║██╔══╝     ██║   ██╔══██║██║██║     ╚════██║
                                                ██║ ╚═╝ ██║   ██║       ██████╔╝███████╗   ██║   ██║  ██║██║███████╗███████║
                                                ╚═╝     ╚═╝   ╚═╝       ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝
                                                                                                                            

        """)

        print()
        print()
        print("="*163)
        print("{:1}{:^11}{:^20}{:^10}{:^20}{:^20}{:^8}{:^15}{:^10}{:^15}{:^15}{:^17}{:1}".format("|","Center Id","Place Name","Mobile No","Person in charge","No.of beds available","Price","Name","Mobile No","Guardian","Guardian Mob","Status","|"))
        print("="*163)
        
        print("{:1}{:^11}{:^20}{:^10}{:^20}{:^20}{:^8}{:^15}{:^10}{:^15}{:^15}{:^17}{:1}".format("|",x,y,d,e,f,h,i,j,k,l,b,"|"))
        print("-"*163)
        print()
        con.close()
    except:
        print("Wrong Patient ID")
        print("Please enter again")
        myDetails()

    # patreport = input("Please type yes if you want a report of your details: ")
    # if patreport in lyes:
    #     reportpat()

def updatePat():
    con=mysql.connector.connect(host="localhost",password=pass1,user="root",database = "BOOKMYBED")
    cursor=con.cursor()
    d1 = {"1":"Patient_Name","2":"Patient_Mobile_No","3":"Guardian_Name","4":"Guardian's_Mob_no"}
    def patdetailentry():
        x = input("Enter the patient_id: ")
        t = "select center_id from patient where patient_id ='{}'".format(x)
        cursor.execute(t)
        r1 =  cursor.fetchall()
        if r1 == []:
                print("Wrong Patient ID")
                print("Please enter again")
                patdetailentry()
        else:
                print("""What do you want to change
                1.Patient Name
                2.Patient Mobile No
                3.Guardian's Name
                4.Guardian's Mobile No""")
                t = input("Enter your option: ")
                if t in d1:
                        y = input("Enter new Entry: ")
                        if t == "1" or "3":
                            j = "update patient set {} = '{}' where patient_id = '{}'".format(d1[t],y,x)
                        elif t == "2" or "4":
                            j = "update patient set {} = '{:d}' where patient_id = '{}'".format(d1[t],y,x)
                        else: 
                            print("Enter a valid option!")
                            patdetailentry()
                        cursor.execute(j)
                        con.commit
                        print("""
                                                                            
                                                    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██████╗ 
                                                    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
                                                    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║  ██║
                                                    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ██║  ██║
                                                    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██████╔╝
                                                    ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═════╝ 
                                                                                                                        

                        """)
                        cursor.execute("select * from patient where patient_id = '{}'".format(x))
                        result = cursor.fetchall()
                        print("{:^60}".format(""))

                        print("{:^163}".format("  ======================================================================================================================"))
                        print("{:>25}{:^13}{:^25}{:^18}{:^25}{:^25}{:^10}{:20}".format("|","Patient ID","Patient Name","Patient Mobile No","Guardian Name","Guardian Mob no","Center ID","|"))
                        print("{:^163}".format("  ======================================================================================================================"))
                        x,y,z,d,e,f,h=result[0]
                        print("{:>25}{:^13}{:^25}{:^18}{:^25}{:^25}{:^10}{:20}".format("|",x,y,z,d,e,f,"|"))
                        print("{:^163}".format("  ----------------------------------------------------------------------------------------------------------------------"))
                        print()

                        con.close()
                else:
                        print("wrong input")
                        patdetailentry()
    patdetailentry()


def initmenu():
    print("="*163)
    print('{:^163}'.format("WELCOME TO "))
    print("""

                                        ██████╗  ██████╗  ██████╗ ██╗  ██╗    ███╗   ███╗██╗   ██╗    ██████╗ ███████╗██████╗ 
                                        ██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝    ████╗ ████║╚██╗ ██╔╝    ██╔══██╗██╔════╝██╔══██╗
                                        ██████╔╝██║   ██║██║   ██║█████╔╝     ██╔████╔██║ ╚████╔╝     ██████╔╝█████╗  ██║  ██║
                                        ██╔══██╗██║   ██║██║   ██║██╔═██╗     ██║╚██╔╝██║  ╚██╔╝      ██╔══██╗██╔══╝  ██║  ██║
                                        ██████╔╝╚██████╔╝╚██████╔╝██║  ██╗    ██║ ╚═╝ ██║   ██║       ██████╔╝███████╗██████╔╝
                                        ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═╝     ╚═╝   ╚═╝       ╚═════╝ ╚══════╝╚═════╝ 



    """)
    
    
    print('{:^163}'.format("Book my Bed provides credible information with sky-high efficiency to help the patients find their Quarantine bed in no time."))
    print("="*163)
initmenu()

def menu(): 
    while True:                 
        print("\n\n\n")
        
        print("="*163)
        print('{:^62}'.format('Serial No.'),'{:^101}'.format('Options'))
        print("="*163)

        print('{:^62}'.format("1."),'{:^101}'.format("Quarantine Centres list"))
        print('{:^62}'.format("2."),'{:^101}'.format("Registering Patient details"))
        print('{:^62}'.format("3."),'{:^101}'.format("Display my Details"))      
        print('{:^62}'.format("4."),'{:^101}'.format('Patient detail Modification'))      
        print('{:^62}'.format("5."),'{:^101}'.format('Graph Report of A Quarantine centre'))  
        print('{:^62}'.format("6."),'{:^101}'.format('Exit'))


        print("\n\n")
        choice=int(input('Enter your CHOICE: '))
        if choice == 1:
            QCentres()
        elif choice == 2:
            addPat()
        elif choice == 3:    
            myDetails()
        elif choice == 4:
            updatePat()
        elif choice == 5:
            reportgov()
        elif choice == 6:
            print("""
                 
                                            ██████╗ ██╗   ██╗███████╗    ██████╗ ██╗   ██╗███████╗
                                            ██╔══██╗╚██╗ ██╔╝██╔════╝    ██╔══██╗╚██╗ ██╔╝██╔════╝
                                            ██████╔╝ ╚████╔╝ █████╗      ██████╔╝ ╚████╔╝ █████╗  
                                            ██╔══██╗  ╚██╔╝  ██╔══╝      ██╔══██╗  ╚██╔╝  ██╔══╝  
                                            ██████╔╝   ██║   ███████╗    ██████╔╝   ██║   ███████╗
                                            ╚═════╝    ╚═╝   ╚══════╝    ╚═════╝    ╚═╝   ╚══════╝
            """)
            break
menu()

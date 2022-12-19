import tkinter
from tkinter import ttk
import tkinter.messagebox
import datetime



###############################################################FIFTH WINDOW########################################################################
def settingswindow():
       second_window.destroy() 
       global settings_window
       settings_window = tkinter.Tk()
       settings_window.attributes('-fullscreen',True)
       settings_window.config(background = 'white')
       settings_window.title('***Settings***')

       label = tkinter.Label(settings_window, text = 'Settings', font=('Algerian',50),relief = 'groove',bd = 10,fg= 'white',bg ='blue')
       label.pack(fill = 'x')

       def check():
              file1 = open('pswd.txt','r')
              file2 = open('name_user.txt','r')
              file1data= file1.read()
              file2data = file2.read()
              if file1data == str(passwd_e.get()):
                     file1.close()
                     new_window1()
              else:
                     tkinter.messagebox.showerror('ERROR','INVALID PASSWORD')
       frame1 = tkinter.Frame(settings_window,width = 1370, height = 800,bg ='red',relief = 'groove',bd = 10)
       frame1.place(x = 0,y=80)
       frame1.pack(fill = 'x')

       frame2 = tkinter.Frame(frame1,width = 550, relief = 'raised',bd =10,height = 310,bg ='blue')
       frame2.place(x = 480, y = 200)

       username = tkinter.Label(frame2, text = 'User Name',font = ('Airal',30),fg = 'white',bg= 'blue')
       username.place(x = 170,y = 0)

       usnm_e = tkinter.Entry(frame2, font = ('Airal',23),relief = 'raised',bd = 5,width = 30 ,justify = 'center',fg ='black',bg = 'white')
       usnm_e.place(x = 6,y = 60)
       
       passwd = tkinter.Label(frame2, text = 'Password',font = ('Airal',30),fg = 'white',bg= 'blue')
       passwd.place(x = 170,y = 120)

       passwd_e = tkinter.Entry(frame2, font = ('Airal',23),relief = 'raised',bd = 5,width = 30 ,justify = 'center',show = '*',fg ='black',bg = 'white')
       passwd_e.place(x = 6,y = 180)

       login = tkinter.Button(frame2,text = 'Login',font = ('arial',18),width = 36, relief = 'raised',bd =5,fg = 'white', bg= 'blue',command= lambda: check())
       login.place(x = 3,y =230)

       backbutton = tkinter.Button(frame1,text = 'back', font = ('arial',15,'bold'),relief ='raised',bd = 5, fg = 'white',bg = 'red',command = lambda : [settings_window.destroy(),startsecondwindow()])
       backbutton.place(x = 0,y = 0)


       def new_window1():
              global option_window
              settings_window.destroy()
              option_window = tkinter.Tk()
              option_window.attributes('-fullscreen',True)
              option_window.config(background = 'red')
              option_window.title('***Settings***')

              label1 = tkinter.Label(option_window, text = 'Settings', font=('Algerian',40),relief = 'groove',bd = 10,fg= 'white',bg ='blue')
              label1.pack(fill = 'x')

              option_frame = tkinter.Frame(option_window, width = 900 , height= 400 ,bg ='blue',relief = 'groove' , bd= 10)
              option_frame.place(x = 270,y = 220)

              passbutton = tkinter.Button(option_frame,text = 'Change Password',height =5, font = ('arial',20),relief  = 'groove',bd = 10,fg= 'white',bg= 'red',command = lambda : Password_window())
              passbutton.place(x = 150,y =90)
              
              userbutton = tkinter.Button(option_frame,text = 'Change User Name',height = 5, font = ('arial',20),relief  = 'groove',bd = 10,fg= 'white',bg= 'red',command= lambda : UserName_window())
              userbutton.place(x = 420,y =90)

              closebutton = tkinter.Button(option_window,text = 'close', font = ('arial',15),relief ='raised',bd = 5, fg = 'white',bg = 'red',command = lambda : [option_window.destroy(),startsecondwindow()])
              closebutton.place(x = 0,y = 80)
       
       def Password_window():
           option_window.destroy()
           update1_window = tkinter.Tk()
           update1_window.attributes('-fullscreen',True)
           update1_window.config(background = 'white')
           update1_window.title('***Settings***')

           def update1():
               if confpasswd_e.get() != '' and passwd_e.get()  != '':
                   if passwd_e.get() == confpasswd_e.get() :
                         file = open('pswd.txt','w')
                         file.write(passwd_e.get())
                         file.close()
                         tkinter.messagebox.showinfo('UPDATED','YOUR PASSWORD HAS BEEN UPDATED')
                         update1_window.destroy()
                         startsecondwindow()
                   else:
                         tkinter.messagebox.showerror('ERROR','PASSWORDS DOES NOT MATCH')
               else:
                  tkinter.messagebox.showerror('ERROR','PASSWORD NOT ENTERED')
           label1 = tkinter.Label(update1_window, text = 'Settings', font=('Algerian',40),relief = 'groove',bd = 10,fg= 'white',bg ='blue')
           label1.pack(fill = 'x')

           frame1 = tkinter.Frame(update1_window,width = 1370, height = 800,bg ='red',relief = 'groove',bd = 10)
           frame1.place(x = 0,y=80)
           frame1.pack(fill = 'x')

           frame2 = tkinter.Frame(frame1,width = 550, height = 320,bg ='blue',relief = 'groove',bd = 10)
           frame2.place(x = 480, y = 200)

           passwd = tkinter.Label(frame2, text = 'New Password',font = ('Airal',30),fg = 'white',bg= 'blue')
           passwd.place(x = 170,y = 0)

           passwd_e = tkinter.Entry(frame2, font = ('Airal',23),width = 30 ,relief = 'raised',bd = 5,show = '*',justify = 'center',fg ='black',bg = 'white')
           passwd_e.place(x = 6,y = 60)

           confpasswd = tkinter.Label(frame2, text = 'Confirm Password',font = ('Airal',30),fg = 'white',bg= 'blue')
           confpasswd.place(x = 140,y = 120)

           confpasswd_e = tkinter.Entry(frame2, font = ('Airal',23),relief = 'raised',bd = 5,width = 30 ,show = '*',justify = 'center',fg ='black',bg = 'white')
           confpasswd_e.place(x = 6,y = 180)

           change1 = tkinter.Button(frame2,text = 'Update',font = ('arial',18),width = 36,relief = 'raised',bd = 5,fg = 'white', bg= 'blue',command = lambda : update1())
           change1.place(x = 5,y =240)

           backbutton = tkinter.Button(frame1,text = 'Quit', font = ('arial',15),relief ='raised',bd = 5, fg = 'white',bg = 'red',command = lambda : [update1_window.destroy(),startsecondwindow()])
           backbutton.place(x = 0,y = 0)

       def UserName_window():
           option_window.destroy()
           update2_window = tkinter.Tk()
           update2_window.attributes('-fullscreen',True)
           update2_window.config(background = 'red')
           update2_window.title('***Settings***')

           def update2():
               if confusername_e.get() != '' and username_e.get()  != '':
                  if username_e.get() == confusername_e.get():
                         file = open('name_user.txt','w')
                         file.write(username_e.get())
                         file.close()
                         tkinter.messagebox.showinfo('UPDATED','YOUR USER NAME HAS BEEN UPDATED')
                         update2_window.destroy()
                         startsecondwindow()
                  else:
                         tkinter.messagebox.showerror('ERROR','USER NAME DOES NOT MATCH')
               else:
                  tkinter.messagebox.showerror('ERROR','USER NAME NOT ENTERED') 
                  
           label1 = tkinter.Label(update2_window, text = 'Settings', font=('Algerian',40),relief = 'groove',bd = 10,fg= 'white',bg ='blue')
           label1.pack(fill = 'x')

           frame1 = tkinter.Frame(update2_window,width = 1370, height = 800,bg ='red',relief = 'groove',bd = 10)
           frame1.place(x = 0,y=80)
           frame1.pack(fill = 'x')

           frame2 = tkinter.Frame(frame1,width = 550, height = 320,bg ='blue',relief = 'groove',bd = 10)
           frame2.place(x = 480, y = 200)

           username = tkinter.Label(frame2, text = 'New User Name',font = ('Airal',30),fg = 'white',bg= 'blue')
           username.place(x = 150,y = 0)

           username_e = tkinter.Entry(frame2, font = ('Airal',23),width = 30 ,justify = 'center',fg ='black',bg = 'white')
           username_e.place(x = 6,y = 60)

           confusername = tkinter.Label(frame2, text = 'Confirm User Name',font = ('Airal',30),fg = 'white',bg= 'blue')
           confusername.place(x = 100,y = 120)

           confusername_e = tkinter.Entry(frame2, font = ('Airal',23),width = 30 ,justify = 'center',fg ='black',bg = 'white')
           confusername_e.place(x = 6,y = 180)

           change2 = tkinter.Button(frame2,text = 'Update',font = ('arial',18),width = 36,relief = 'raised',bd = 5,fg = 'white', bg= 'blue',command = lambda : update2())
           change2.place(x = 5,y =240)

           backbutton = tkinter.Button(frame1,text = 'Quit', font = ('arial',15),relief ='raised',bd = 5, fg = 'white',bg = 'red',command = lambda : [update2_window.destroy(),startsecondwindow()])
           backbutton.place(x = 0,y = 0)


#########################################################FOURTH WINDOW################################################################
def startfourthwindow():
    def about() :
        about_window = tkinter.Tk()
        about_window.geometry('700x250')
        about_window.resizable(False,False)
        about_window.title('About Developers')
        about_window.config(background = 'yellow')
        label = tkinter.Label(about_window,text = 'This Project is an integrated efforts by : \n Aaditva Vijay Vats  \n Ayush Jain \n Satvik Jain \n Pratham Vardaan.',font =( 'Courier',15),relief = 'groove' , bd = 10,fg = 'red', bg = 'lightblue')
        label.place(x = 50, y = 50)

    def bib():
        bib_window = tkinter.Tk()
        bib_window.geometry('800x350')
        bib_window.resizable(False,False)
        bib_window.title('About Developers')
        bib_window.config(background = 'yellow')
        t = '''To make this project we have taken help from
the following sources :
1. Our textbook Computer Science with Python
     by Sumitra Arora
2. Byte Learning - Youtube Channel On Byte we
     learned many informations needed to make
     this project
    And with the utmost guidance of our Computer
    Science teacher Sir Vivek Duneja'''
        label = tkinter.Label(bib_window,text = t,font = ('Courier', 15),relief  = 'groove',justify = 'left', bd = 10,fg= 'red',bg = 'lightblue')
        label.place(x = 50, y = 50)

    fourth_window=tkinter.Tk()
    fourth_window.attributes('-fullscreen',True)
    fourth_window.title("About the Developers")
    fourth_window.configure(bg="powderblue")

    label_top=tkinter.Label(fourth_window,text="MOBIWORLD",bg="red",fg="white",font=("algerian",42),padx=10,pady=25,borderwidth=10,relief='ridge')
    label_top.pack(fill = 'x')

    frame_buttons=tkinter.Frame(fourth_window,bg="white",borderwidth=15,width=100,relief='ridge')
    frame_buttons.pack()

    frame_exit=tkinter.Frame(fourth_window,bg="white",borderwidth=10,width=100,relief='ridge')
    frame_exit.pack(side="bottom",fill="x")

    frame_buttons.place(y=300,x=200)

    tkinter.Button(frame_buttons,text="About US",font="courier 25 bold",width=7,bg="yellow",fg="firebrick1",padx=150,pady=15,relief='ridge',command=about).grid(row=5,column=1)

    tkinter.Button(frame_buttons,text="Bibliography",font="courier 25 bold",width=7,bg="yellow",fg="firebrick1",padx=150,pady=15,relief='ridge',command=bib).grid(row=5,column=5)

    tkinter.Button(frame_exit,text="Exit",font="courier 25 bold",width=7,bg="yellow",fg="firebrick1",padx=150,pady=15,relief='ridge',command=fourth_window.destroy).pack(fill="x")

#################################################################THIRD WINDOW############################################################
def startthirdwindow():
    global serial,amountpayable,r,product_purchased_list,product_purchased_cost_list,product_quantity_list,product_cgst,product_sgst,net_cost_list
    serial = 0
    amountpayable = 0
    r = ''
    product_purchased_list = [ ]
    product_purchased_cost_list = []
    product_quantity_list = []
    product_cgst = []
    product_sgst = []
    net_cost_list = []

    
    third_window = tkinter.Tk()
    third_window.attributes('-fullscreen',True)
    third_window.title('MOBILE MANAGEMENT SYSTEM')
    third_window.resizable(False,False)



    #frames
    frame1 = tkinter.Frame(bg = 'darkblue', cursor = 'hand2',relief = 'groove',bd = 10, height = 865,width = 735 )
    frame1.place(x = 0,y = 0)

    frame2 = tkinter.Frame(bg = 'darkblue', cursor = 'hand2',relief = 'groove',bd = 10, height = 865,width = 800 )
    frame2.place(x = 735,y = 0)




    #time
    a = datetime.date.today()
    timer = tkinter.Label(frame1 , text = 'Date :-'+str(a) ,font = ('arial',16),bg = 'darkblue',fg= 'white')
    timer.place(x =400,y = 70)



    #bill number
    y = str(a.year)
    mo = str(a.month)
    d = str(a.day)
    hh = datetime.datetime.now()
    h = str(hh.hour)
    m = str(hh.minute)


    billno = 'UC'+y+'A'+mo+'A'+d+'P'+h+'S'+m
    invoice = tkinter.Label(frame1,text = 'Invoice No :'+billno, font = ('arial',16,'bold'),bg = 'darkblue',fg = 'white')
    invoice.place(x= 0, y= 70)



    #model names
    model_name_list=['Select Model Name','Galaxy N20','Galaxy M51','Galaxy S20','Galaxy Z Flip','Galaxy S10 Lite',
                     'iPhone XR','iPhone XS','iPhone XS Max','iPhone 11','iPhone 11 Pro','iPhone 11 Pro Max','iPhone SE','Lenovo K10 Plus',
                     'Lenovo A6 Note','Lenovo Z6 Pro','Lenovo Z5','Lenovo K9','Vivo S1 Prime','Vivo X50 Pro','Vivo Y50','Vivo Y20i','Vivo V19',
                     'OPPO F17 Pro','OPPO Reno 4 Pro','OPPO Reno3 Pro','OPPO F17','OPPO A52']
    model_name_dictionary={'Select Model Name':'','Galaxy N20':104999.00,'Galaxy M51':50000.00,'Galaxy S20':45999.00,'Galaxy Z Flip':108999.00,'Galaxy S10 Lite':70000.00,
                     'iPhone XR':30000.00,'iPhone XS':47000.00,'iPhone XS Max':50000.00,'iPhone 11':96000.00,'iPhone 11 Pro':102000.00,'iPhone 11 Pro Max':95000.00,'iPhone SE':85000.00,
                    'Lenovo K10 Plus':25000.00,'Lenovo A6 Note':13000.00,'Lenovo Z6 Pro':15000.00,'Lenovo Z5':20000.00,'Lenovo K9':23500.00,
                    'Vivo S1 Prime':13000.00,'Vivo X50 Pro':14500.00,'Vivo Y50':16500.00,'Vivo Y20i':22500.00,'Vivo V19':17500.00,
                     'OPPO F17 Pro':11500.00,'OPPO Reno 4 Pro':24000.00,'OPPO Reno3 Pro':33500.00,'OPPO F17':16500.00,'OPPO A52':40500.00}



    def personal_details():
        global name_e, phone_e,email_e,modelname_e,quantity_e,sgst_e,cgst_e,gstin_uin_e
        heading = tkinter.Label(frame1 , text = "CUSTOMER'S DETAILS" ,relief = 'groove',bd = 5,font = ('arial',20,'bold underline'),bg = 'darkblue',fg= 'white')
        heading.place(x = 150,y = 5)

        gstin_uin  = tkinter.Label(frame1 , text = 'GSTIN / UIN ',font = ('arial',16),bg = 'darkblue',fg= 'white')
        gstin_uin.place(x = 5,y = 100)

        gstin_uin_e = tkinter.Entry(frame1,width  = 25, font = ('arial',14))
        gstin_uin_e.place(x = 5,y = 130)

        email  = tkinter.Label(frame1 , text = 'E-mail',font = ('arial',16),bg = 'darkblue',fg= 'white')
        email.place(x = 5,y = 170)

        email_e = tkinter.Entry(frame1,width  = 25, font = ('arial',14))
        email_e.place(x = 5,y = 200)

        name = tkinter.Label(frame1 , text = 'Name',font = ('arial',16),bg = 'darkblue',fg= 'white')
        name.place(x = 5,y = 230)

        name_e = tkinter.Entry(frame1,width  = 25, font = ('arial',14))
        name_e.place(x = 5,y = 260)

        phone = tkinter.Label(frame1 , text = 'Phone Number',font = ('arial',16),bg = 'darkblue',fg= 'white')
        phone.place(x = 5,y = 290)

        phone_e = tkinter.Entry(frame1,width  = 25, font = ('arial',14))
        phone_e.place(x = 5,y = 320)

        modelname = tkinter.Label(frame1 , text = 'Model Name',font = ('arial',16),bg = 'darkblue',fg= 'white')
        modelname.place(x = 5,y = 350)

        modelname_e = ttk.Combobox(frame1,width = 29,font = ('arial',13),values = model_name_list,state='readonly' )
        modelname_e.place(x = 5,y = 380)
        modelname_e.current(0)

        price = tkinter.Label(frame1 , text = 'Price',font = ('arial',16),bg = 'darkblue',fg= 'white')
        price.place(x = 5,y = 410)

        price_e = tkinter.Label(frame1,text = '',width  = 25, font = ('arial',14))
        price_e.place(x = 5,y = 440)
###########################

        def autopopulate():
            p = (model_name_dictionary[modelname_e.get()])
            n = int(quantity_e.get())
            cg =( cgst_e.get())
            sg = (sgst_e.get())
            if p != '' and cg != '' and sg != '':
                price_e.config(text = p)
                gtotal_e.config(text = round(n*((p) + (p*int(cg)/100)+ (p*int(sg)/100)),2))
                
        cgst = tkinter.Label(frame1, text = 'CGST(%)',font = ('aria',15),bg = 'darkblue',fg = 'white')
        cgst.place(x =305 , y = 410)

        cgst_e = tkinter.Entry(frame1,width = 5,font = ('arial',16),justify = 'center',bg = 'white',fg = 'blue')
        cgst_e.place(x =310 , y = 440)

        sgst = tkinter.Label(frame1, text = 'SGST(%)',font = ('arial',15),bg = 'darkblue',fg = 'white')
        sgst.place(x =425 , y = 410)

        sgst_e = tkinter.Entry(frame1,width = 5,font = ('arial',16),justify = 'center',bg = 'white',fg = 'blue')
        sgst_e.place(x =430 , y = 440)
        
        quantity = tkinter.Label(frame1 , text = 'Quantity',font = ('arial',16),bg = 'darkblue',fg= 'white')
        quantity.place(x = 5,y = 470)

        quantity_e = tkinter.Spinbox(frame1,width  = 24,from_ =1,to = 20, font = ('arial',14))
        quantity_e.place(x = 5,y = 500)

        gtotal = tkinter.Label(frame1 , text = 'Grand Total',font = ('arial',16),bg = 'darkblue',fg= 'white')
        gtotal.place(x = 5,y = 530)

        gtotal_e = tkinter.Label(frame1,relief = 'groove',bd = 5,width = 23,font = ('arial',16),bg = 'white',fg= 'blue')
        gtotal_e.place(x = 5,y = 560)

        submit = tkinter.Button(frame1, text = 'Submit', font = ('arial',16),command = lambda : [autopopulate(),check()])
        submit.place(x=200 ,y = 620)
    personal_details()



    def check():
        global count_error
        count_error = 0
        a = name_e.get()
        if a.isspace() or len(a) == 0 or a.isalnum():
            tkinter.messagebox.showerror('Invalid Name',"Enter the valid Name")
            count_error+=1
        b = phone_e.get()
        if not b.isdigit() or len(b)!= 10:
            tkinter.messagebox.showerror('Invalid Phone Number',"Enter the valid Phone number")
            count_error+=1
        if modelname_e.get() == '':
            tkinter.messagebox.showerror('Product not selected','Kindly Select A Product')
            count_error+=1
        Generate_bill()
    ############################################################FRAME - 2##############################################
    heading2= tkinter.Label(frame2,text = 'BILL ', font = ('arial',20,'bold underline'),relief = 'groove',bd = 5,bg = 'darkblue',fg= 'white')
    heading2.place(x = 290,y = 0)
#########################################################FRAME######################################################
    frame3 = tkinter.Frame(frame2,bg = 'white', cursor = 'cross',relief = 'groove',bd = 5, height = 660,width = 660 )
    frame3.place(x = 60,y = 50)
     

######################################################################################################################
    def Generate_bill():
        global serial,amountpayable,r,product_purchased_list,product_purchased_cost_list,product_quantity_list,product_cgst,product_sgst,net_cost_list
        if count_error == 0:
            cname = tkinter.Label(frame3,text= 'Mobi World Pvt. Ltd.',font = ('times new roman',14),bg = 'white',fg= 'black')
            cname.place(x = 220,y = 0)

            caddress = tkinter.Label(frame3,text = 'Address :- 20/2953 - B, Delhi Road,Saharanpur, U.P. ',font = ('times new roman',12),bg = 'white',fg= 'black')
            caddress.place(x = 150,y = 20)

            ccontact = tkinter.Label(frame3,text = 'Contact No. : +91700800321',font = ('times new roman',12),bg = 'white',fg= 'black')
            ccontact.place(x = 0,y = 40)

            cgstin = tkinter.Label(frame3,text = 'GSTIN/UIN: 789654132103',font = ('times new roman',12),bg = 'white',fg= 'black')
            cgstin.place(x = 410,y = 40)

            dashes = tkinter.Label(frame3,text  = '-'*90,font = ('times new roman',16),bg = 'white',fg= 'black')
            dashes.place(x = 5,y = 60)            

            billdate = tkinter.Label(frame3,text  ='Date :- '+str(a),font = ('times new roman',11),bg = 'white',fg= 'black')
            billdate.place(x = 350,y = 90)

            billnumber = tkinter.Label(frame3,text= 'Bill ID :- '+billno,font = ('times new roman',11),bg = 'white',fg= 'black')
            billnumber.place(x = 0,y = 90)

            emailid =tkinter.Label(frame3,text= 'Email ID :- '+ email_e.get(),font = ('times new roman',11),bg = 'white',fg= 'black')
            emailid.place(x = 0,y = 120)

            gstin = tkinter.Label(frame3,text = 'GSTIN / UIN :- ' + gstin_uin_e.get(), font = ('times new roman',11),bg = 'white',fg= 'black')
            gstin.place(x = 350,y = 120)

            
            coname = tkinter.Label(frame3,text  = "Customer's Name :- "+(name_e.get()).title(),font = ('times new roman',11),bg = 'white',fg= 'black')
            coname.place(x = 0,y = 150)

            contactno = tkinter.Label(frame3,text  = 'Phone no:- '+phone_e.get(),font = ('times new roman',11),bg = 'white',fg= 'black')
            contactno.place(x = 350,y = 150)

            dashes = tkinter.Label(frame3,text  = '-'*90,font = ('times new roman',16),bg = 'white',fg= 'black')
            dashes.place(x = 5,y = 180)
########################################################################################################################################################
            sno = tkinter.Label(frame3,text = 'S.No.',font = ('times new roman',11),bg = 'white',fg = 'black')
            sno.place(x=0,y=210)

            pname = tkinter.Label(frame3,text = 'Product Name',font = ('times new roman',11),bg = 'white',fg = 'black')
            pname.place(x=40,y=210)

            quant= tkinter.Label(frame3,text = 'Qty.',font = ('times new roman',11),bg = 'white',fg = 'black')
            quant.place(x=165,y=210)

            price= tkinter.Label(frame3,text = 'Cost/unit',font = ('times new roman',11),bg = 'white',fg = 'black')
            price.place(x=200,y=210)       

            gsts= tkinter.Label(frame3,text = 'SGST',font = ('times new roman',11),bg = 'white',fg = 'black')
            gsts.place(x=265,y=210)

            gstsa= tkinter.Label(frame3,text = 'SGST Amt.',font = ('times new roman',11),bg = 'white',fg = 'black')
            gstsa.place(x=310,y=210)
            
            gstc= tkinter.Label(frame3,text = 'CGST',font = ('times new roman',11),bg = 'white',fg = 'black')
            gstc.place(x=390,y=210)

            gstca= tkinter.Label(frame3,text = 'CGST Amt.' ,font = ('times new roman',11),bg = 'white',fg = 'black')
            gstca.place(x=450,y=210)
            
            price2= tkinter.Label(frame3,text = 'Net Cost',font = ('times new roman',11),bg = 'white',fg = 'black')
            price2.place(x=560,y=210)     
            serial += 1 
#############################################################################################################################3
            wsno = tkinter.Label(frame3,text = serial ,font = ('times new roman',11),bg = 'white',fg = 'black')
            wsno.place(x=10,y=210+serial*30)

            wname = tkinter.Label(frame3,text = modelname_e.get() ,font = ('times new roman',11),bg = 'white',fg = 'black')
            wname.place(x=40,y=210+serial*30)

            wquantity = tkinter.Label(frame3,text = quantity_e.get(),font = ('times new roman',11),bg = 'white',fg = 'black')
            wquantity.place(x=175,y=210+serial*30)
################list
            product_purchased_list.append(modelname_e.get())
            product_purchased_cost_list.append(model_name_dictionary[modelname_e.get()])
            product_quantity_list.append(quantity_e.get())
            product_cgst.append(cgst_e.get())
            product_sgst.append(sgst_e.get())
###############
            wprice= tkinter.Label(frame3,text = model_name_dictionary[modelname_e.get()],font = ('times new roman',11),bg = 'white',fg = 'black')
            wprice.place(x=200,y=210+serial*30)
            
            wgsts= tkinter.Label(frame3,text = sgst_e.get()+'%' ,font = ('times new roman',11),bg = 'white',fg = 'black')
            wgsts.place(x=275,y=210+serial*30)
            
            wgstsa= tkinter.Label(frame3,text = model_name_dictionary[modelname_e.get()] * float(sgst_e.get())/100 ,font = ('times new roman',11),bg = 'white',fg = 'black')
            wgstsa.place(x=320,y=210+serial*30)

            wgstc= tkinter.Label(frame3,text = cgst_e.get()+'%',font = ('times new roman',11),bg = 'white',fg = 'black')
            wgstc.place(x=400,y=210+serial*30)
            
            wgstca= tkinter.Label(frame3,text = model_name_dictionary[modelname_e.get()] * float(sgst_e.get())/100 ,font = ('times new roman',11),bg = 'white',fg = 'black')
            wgstca.place(x=460,y=210+serial*30)            

            wprice2= tkinter.Label(frame3,text = round((model_name_dictionary[modelname_e.get()]+float(sgst_e.get())*model_name_dictionary[modelname_e.get()]/100 + float(cgst_e.get())*model_name_dictionary[modelname_e.get()]/100) * float(quantity_e.get()),2) ,font = ('times new roman',11),bg = 'white',fg = 'black')
            wprice2.place(x=560,y=210+serial*30)
################################
            net_cost_list.append(round((model_name_dictionary[modelname_e.get()]+float(sgst_e.get())*model_name_dictionary[modelname_e.get()]/100 + float(cgst_e.get())*model_name_dictionary[modelname_e.get()]/100) * float(quantity_e.get()),2))
#############################
            amountpayable += round((model_name_dictionary[modelname_e.get()]+float(sgst_e.get())*model_name_dictionary[modelname_e.get()]/100 + float(cgst_e.get())*model_name_dictionary[modelname_e.get()]/100) * float(quantity_e.get()))

            wamountpayable = tkinter.Label(frame3,text = 'Grand Total:-' + str(amountpayable)+' /-Rs.',relief = 'groove',bd = 4,font = ('times new roman',14),bg = 'white',fg = 'black')
            wamountpayable.place(x=430,y=480)
##############################################################################################################################
            r = ''
            grandtotallabel = tkinter.Label(frame3,font = ('arial',12,'bold'),relief = 'raised' , bd = 4,width = 60,fg = 'black',bg = 'white')
            grandtotallabel.place(x = 30,y = 520)

            thnx = tkinter.Label(frame3,text = 'Thank You for shopping',font = ('arial',14,'bold'),fg = 'black',bg = 'white')
            thnx.place(x = 210,y = 560)

            dictionary  =  {1 : ' one', 2 : ' two',3 : ' three',4 : ' four',5 : ' five', 6 : ' six',7 : ' seven',
8 : ' eight', 9 :' nine',0:' zero', 10 : ' ten' ,11 : ' eleven', 12  : ' twelve', 13 : ' thirteen', 14  : ' fourteen', 15 : ' fifteen',
16 : ' sixteen', 17 : ' seventeen', 18 : ' eighteen', 19 : ' nineteen', 20 : ' twenty', 30  : ' thirty', 40 : ' forty',
50 :  ' fifty' , 60  : ' sixty', 70 : ' seventy', 80 : ' eighty' , 90 : ' ninety'}
            number = amountpayable
            #list of digits 
            digits = [ ]
            while number > 0:
                digit = number % 10
                digits.append(str(digit))
                number = number // 10
            #reversing the list        
            digits = digits[ : : -1]
            
            def lakh():
                global r
                l = len(digits)
                if l % 2 != 0 and int(digits[0]) != 0:
                    n = int(digits[0] + digits[1])
                    if n in dictionary:
                       r += dictionary[n] + ' lakh'
                    else:
                        r += dictionary[int(digits[0])*10]
                        r += dictionary[int(digits[1])] + ' lakh'
                    digits.pop(0)
                    digits.pop(0)
                else:
                    if int(digits[0]) == 0:
                        digits.pop(0)
                        if int(digits[0]) != 0: 
                            r += dictionary[int(digits[0])] + ' lakh'
                            digits.pop(0)
                        else:
                            digits.pop(0)
                    else:
                        r += dictionary[int(digits[0])] + ' lakh'
                        digits.pop(0)
                thousand()
                
            def thousand():
                global r
                l = len(digits)
                if l % 2 != 0 and int(digits[0]) != 0:
                    n = int(digits[0] + digits[1])
                    if n in dictionary:
                       r += dictionary[n] + ' thousand'
                    else:
                        r += dictionary[int(digits[0])*10]
                        r += dictionary[int(digits[1])] + ' thousand'
                    digits.pop(0)
                    digits.pop(0)
                else:
                    if int(digits[0]) == 0:
                        digits.pop(0)
                        if int(digits[0]) != 0:
                            r += dictionary[int(digits[0])] + ' thousand'
                            digits.pop(0)
                        else:
                            digits.pop(0)
                    else:
                        r += dictionary[int(digits[0])] + ' thousand'
                        digits.pop(0)
                hundred()
            def hundred():
                global r
                if int(digits[0]) != 0 :
                    number = int(digits[0])
                    number = dictionary[number] +  " hundred"
                    digits.pop(0)
                    r += number
                    two_digits()
                else:
                    digits.pop(0)
                    two_digits()
            def two_digits():
                global r
                n = int(digits[0] + digits[1])
                if n in dictionary:
                    if n!= 0:
                        r += dictionary[n]
                else:
                   r += dictionary[int(digits[0])*10]
                   r += dictionary[int(digits[1])]
            def one_digit():
                global r
                r += dictionary[int(digits[0])]
            #comparing the lengths of the number
            l = len(digits)
            if l == 1:
                one_digit()
            elif l == 2 :
                two_digits()
            elif l == 3:
                hundred()
            elif l == 4 or l == 5:
                thousand()
            elif l==6 or l== 7:
                lakh()
            else:
                if len(digits)==0:
                    r+='zero'
            grandtotallabel.config(text =r.title()+ ' Only')
#################################################writing data in file#######################################################################
        def write_data():
            filename = open(billno+'.txt','w')
            filename.write('=================================BILL========================================='+'\n')
            filename.write('                                                        Mobi World Pvt. Ltd.'+'\n')
            filename.write('                                     Address :- 20/2953 - B, Delhi Road,Saharanpur, U.P.'+'\n')
            filename.write('Contact No. : +91700800321                                      GSTIN/UIN: 789654132103'+'\n')
            filename.write("---------------------------------------------------Customer's Details-----------------------------------------------------------"+'\n')
            filename.write('Bill No. :- ' + billno+'                             '+'Dated :- '+str(a)+'\n')
            filename.write('Email :- '+email_e.get()+'                              ' +'GSTIN/UIN  :- ' + gstin_uin_e.get()+'\n')
            filename.write("Customer's Name :- " + name_e.get().title() + '                     '+'Phone No. :- ' + phone_e.get()+'\n' )
            filename.write('-------------------------------------------------------------------------------------------------------------------------------------------'+'\n')
            filename.write('S.no  Product Name       Cost/unit  Qty.   CGST   CGST Amt.  SGST   SGST Amt.     Net Cost' +'\n')
            for i in range (len(product_purchased_list)):
                filename.write(str(i+1) +'       '+ str(product_purchased_list[i])+'          '+str(product_purchased_cost_list[i])+'     '+ str(product_quantity_list[i])+'        '+str(product_cgst[i])+'         '+str(float(product_cgst[i])*float(product_purchased_cost_list[i])/100)+'               '+str(product_sgst[i])+ '         '+str(float(product_sgst[i])*float(product_purchased_cost_list[i])/100)+'        ' +str(net_cost_list[i])+'\n')
            filename.write('Total Amount :- ' +'Rs. '+str(amountpayable)+'.00/-'+'\n')
            filename.write('IN WORDS:- '+'Rupees '+r.title()+' Only'+'\n')
            filename.write("Receiver's signature                                                  Authorised Signatory"+'\n')
            filename.write('-------------------------------------------------------------------------------------------------------------------------------------------'+'\n')
            filename.write("""Terms & Conditions
                     1. Goods once sold will not be taken back
                     2. Interest @ 18% p.a. will be changed if the payment
                          is not made within the stipulated time.
                     3. Subject to Saharanpur Jurisdiction only.""")
            filename.close()
            tkinter.messagebox.showinfo('Succesfully Saved', 'Bill has been saved')
        def write_data2():
            filename2 = open(r""+phone_e.get()+'.txt','w')
            filename2.write('=================================BILL========================================='+'\n')
            filename2.write('                                                       Mobi World Pvt. Ltd.'+'\n')
            filename2.write('                                  Address :- 20/2953-B, Delhi Road,Saharanpur, U.P.'+'\n')
            filename2.write('Contact No. : +91700800321                                        GSTIN/UIN: 789654132103'+'\n')            
            filename2.write("--------------------------------------------------Customer's Details-----------------------------------------------------------"+'\n')
            filename2.write('Bill No. :- ' + billno+'                             '+'Dated :- '+str(a)+'\n')
            filename2.write('Email :- '+email_e.get()+'                              ' +'GSTIN/UIN  :- ' + gstin_uin_e.get()+'\n')
            filename2.write("Customer's Name :- " + name_e.get().title() + '                     '+'Phone No. :- ' + phone_e.get()+'\n' )
            filename2.write('-------------------------------------------------------------------------------------------------------------------------------------------'+'\n')
            filename2.write('S.no  Product Name       Cost/unit  Qty.   CGST   CGST Amt.  SGST   SGST Amt.     Net Cost' +'\n')
            for i in range (len(product_purchased_list)):
                filename2.write(str(i+1) +'       '+ str(product_purchased_list[i])+'          '+str(product_purchased_cost_list[i])+'     '+ str(product_quantity_list[i])+'        '+str(product_cgst[i])+'         '+str(float(product_cgst[i])*float(product_purchased_cost_list[i])/100)+'               '+str(product_sgst[i])+ '         '+str(float(product_sgst[i])*float(product_purchased_cost_list[i])/100)+'        ' +str(net_cost_list[i])+'\n')
            filename2.write('Total Amount :- ' +'Rs. '+str(amountpayable)+'.00/-'+'\n')
            filename2.write('IN WORDS:- '+'Rupees '+r.title()+' Only'+'\n')
            filename2.write("Receiver's signature                                                  Authorised Signatory"+'\n')
            filename2.write('-------------------------------------------------------------------------------------------------------------------------------------------'+'\n')            
            filename2.write("""Terms & Conditions
                     1. Goods once sold will not be taken back
                     2. Interest @ 18% p.a. will be changed if the payment
                          is not made within the stipulated time.
                     3. Subject to Saharanpur Jurisdiction only.""")
            filename2.close()
            
        write_data_button = tkinter.Button(frame2,text = 'Save',font = ('arial',14),fg = 'white',bg = 'darkblue',command = lambda: [write_data(),write_data2(),new_bill()])
        write_data_button.place(x =530 ,y =5 )        
        def new_bill():
            third_window.destroy()
            startthirdwindow()
        newbill_button = tkinter.Button(frame2,text = 'New Bill',font = ('arial',14),fg = 'white',bg = 'darkblue',command = lambda:new_bill())
        newbill_button.place(x =610 ,y =5 )           
##################################################################opening an existing bill################################################################
    def openbill():
        billwindow = tkinter.Tk()
        billwindow.geometry('370x350')
        billwindow.resizable(False,False)
        billwindow.title('Browse Bill')
        billwindow.config(background = 'dark blue',cursor = 'hand2')

        headinglabel = tkinter.Label(billwindow, text = 'Enter the Bill Number', font = ('arial',20),relief = 'raised',fg = 'white',bg ='dark blue')
        headinglabel.place(x = 25, y = 50)
        
        billnumber = tkinter.Entry(billwindow, width = 25,font = ('arial' , 16),relief = 'raised',fg=  'blue', bg = 'white')
        billnumber.place(x =25,y = 100 )

        orlabel = tkinter.Label(billwindow, text = 'OR', font = ('arial',16),relief = 'raised',fg = 'white',bg ='dark blue')
        orlabel.place(x = 150, y = 150)


        headinglabel2 = tkinter.Label(billwindow, text = 'Enter the Phone Number', font = ('arial',20),relief = 'raised',fg = 'white',bg ='dark blue')
        headinglabel2.place(x = 25, y = 200)
        
        phonenumber = tkinter.Entry(billwindow, width = 25,font = ('arial' , 16),relief = 'raised',fg=  'blue', bg = 'white')
        phonenumber.place(x =25,y = 250 )
        
        def viewbill():
            b = billnumber.get()
            c = phonenumber.get()
            if b =='' and c != '':
                bill = r""+c #yaha par path change kiya hai taki new laptop me chal jaye
            else:
                bill = b
            try:
                existingfilename = open(bill+'.txt','r')
                
                billwindow2 = tkinter.Tk()
                billwindow2.geometry('660x670')
                billwindow2.resizable(False,False)
                billwindow2.title('Bill Number :-  ' + b)
                billwindow2.config(background = 'dark blue',cursor = 'hand2')
                
                data = existingfilename.readlines()
                frame4 = tkinter.Frame(billwindow2, bg = 'white', cursor = 'hand1', height = 660,width = 620)
                frame4.place(x =20, y= 18)
                count = 0
                for i in data:
                    datalabel = tkinter.Label(frame4 , text = i,font = ('times new roman',11), fg= 'black', bg = 'white')
                    datalabel.place(x =0, y = count * 30)
                    count+=1
            except:
                tkinter.messagebox.showinfo('Unkown Bill no.','Bill Number does not exist')
                billwindow.destroy()

        showbill = tkinter.Button(billwindow,text = 'Open Bill', font = ('arial',16),fg = 'white',bg = 'dark blue',command = lambda : viewbill())
        showbill.place(x = 120, y = 300)

    browse  = tkinter.Button(frame1,text = 'Open Bill', font = ('arial',16),fg = 'white',bg = 'dark blue',command = lambda : openbill())
    browse.place(x = 300, y = 620)
    logoutbutton = tkinter.Button(frame1,text = 'Log Out',font = ('arial',13),fg= 'white',bg = 'red',command = lambda :[third_window.destroy(),startsecondwindow()])
    logoutbutton.place(x = 5,y =5)

############################################SECOND WINDOW#######################################################
def startsecondwindow():
    global count_chance,second_window,image2
    count_chance = 0
    second_window=tkinter.Tk()
    second_window.title("USERNAME AND PASSWORD ")
    second_window.attributes('-fullscreen',True)
    second_window.config(background="red",cursor = 'hand2')

    image2 = tkinter.PhotoImage(file = 'LOGO2.gif')

    ##################################################################
    def check():
        global count_chance
        if username.get()=="" or password.get()=="" :
            tkinter.messagebox.showerror("Error","Please enter the Username and Password")
        else :
            file1 = open('pswd.txt','r')
            file2 = open('name_user.txt','r')
            file1data = file1.read()
            file2data = file2.read()
            file1.close()
            file2.close()
            if file1data == password.get() and username.get() == file2data:
                tkinter.messagebox.showinfo("Done","You have successfully login ")
                second_window.destroy()
                startthirdwindow()
            else:
                tkinter.messagebox.showerror("Error","Incorrect Username or Password")
                count_chance+=1
                if count_chance == 5:
                    tkinter.messagebox.showinfo('Try Again Later','5 Incorrect Attempts')
                    second_window.destroy()
    ###############################################################
    company_name = tkinter.Label(second_window,text = 'WELCOME TO MOBIWORD',font = ('algerian',50),relief = 'raised' , bd =10 , fg = 'white', bg = 'blue')
    company_name.place(x=0,y = 0)
    company_name.pack(fill = 'x')
    ###############################
    login_frame = tkinter.Frame(second_window, width = 800,height = 410,cursor = 'hand1', relief = 'raised',bd =5,bg = 'blue')
    login_frame.place(x = 360,y = 250)
    
    photolabel2 = tkinter.Label(login_frame,image = image2,relief = 'raised')
    photolabel2.place(x = 558,y = 80)
    ##############################
    label1 = tkinter.Label(login_frame,text = 'EMPLOYEE LOGIN', font = ('elephant',27,'bold'),fg = 'white', bg ='blue')
    label1.place(x =160 , y=0 )

    label2 =  tkinter.Label(login_frame,text = 'User Name', font = ('Comic Sans MS',23,'bold'),fg = 'white', bg ='blue')
    label2.place(x =20 , y=100 )

    username = tkinter.Entry(login_frame,font = ('Comic Sans MS',20,'bold'),width = 20, relief = 'raised' ,bd =5,fg = 'black', bg ='white')
    username.place(x = 220,y = 105)

    label3 =  tkinter.Label(login_frame,text = 'Password', font = ('Comic Sans MS',23,'bold'),fg = 'white', bg ='blue')
    label3.place(x =20 , y=180 )

    password = tkinter.Entry(login_frame,font = ('Comic Sans MS',20,'bold'),width = 20, show = '*',relief = 'raised' ,bd =5,fg = 'black', bg ='white')
    password.place(x = 220,y = 180)

    login = tkinter.Button(login_frame, text = 'Login', font = ('arial',20),width = 26,relief = 'raised',bd = 5,bg = 'blue',fg = 'white',command= lambda : check())
    login.place(x = 70,y = 285)
    
    devbutton = tkinter.Button(second_window, text = 'About Developers', font = ('arial',20,'bold'),width = 17,relief = 'raised',bd = 8,bg = 'blue',fg = 'white',command= lambda : startfourthwindow())
    devbutton.place(x = 0,y = 98)

    setting = tkinter.Button(second_window, text = 'Settings', font = ('arial',20,'bold'),width = 17,relief = 'raised',bd = 8,bg = 'blue',fg = 'white',command= lambda : settingswindow())
    setting.place(x = 1225,y = 98)

    # stock = tkinter.Button(second_window, text = 'Stock', font = ('arial',20,'bold'),width = 17,relief = 'raised',bd = 8,bg = 'blue',fg = 'white',command= lambda : stock_window())
    # stock.place(x = 0,y = 798)

    def message():
           answer = tkinter.messagebox.askyesno('EXIT','ARE YOU SURE YOU WANT TO QUIT')
           if answer == True:
                  second_window.destroy()
                  backwindow.destroy()

    close_button = tkinter.Button(second_window, text = 'Quit', font = ('arial',20,'bold'),width = 17,relief = 'raised',bd = 7,bg = 'blue',fg = 'white',command= lambda : message())
    close_button.place(x = 1227,y = 798)
# def stock_window():
#        second_window.destroy()
#        global image3
#        swindow = tkinter.Tk()
#        swindow.attributes('-fullscreen',True)
#        swindow.config(background = 'blue')

#        sheading = tkinter.Label(swindow,text = "STOCK WINDOW", font = ('algerian', 34),  fg  = 'black',bg = 'blue')
#        sheading.place(x = 250, y = 0)

#        stockfile = open('stock.txt','r')
#        data = stockfile.read().split(',')
#        stocklist = ['Select the Product']


#        label = tkinter.Label(text = 'SELECT THE PRODUCT', font = ('arial',23),fg = 'black',bg = 'blue')
#        label.place(x = 0 , y = 80)

#        slabel = tkinter.Label(swindow, width = 24 ,font= ('arial', 22), fg = 'white',bg = 'red',relief = 'raised' , bd = 5)
#        slabel.place(x =0 , y = 170)
#        stock_dictionary = {'Select the Product':'Kindly select product'}

#        image3 = tkinter.PhotoImage(file = 'LOGO.gif')
#        imagelabel = tkinter.Label(swindow, image = image3,relief = 'raised',bd =10)
#        imagelabel.place(x = 760,y = 0)

#        def do():
#               entry = cbox.get()
#               slabel.config(text = stock_dictionary[entry])
              
#        for i in data:
#               stocklist.append(i[0:-3])
#               stock_dictionary[i[0:-3]] = int(i[-2 : :])
#        cbox = ttk.Combobox(swindow, width = 25,font = ('arial',22),values = stocklist )
#        cbox.place(x = 0, y = 120)
#        cbox.current(0)

#        sub = tkinter.Button(swindow,text = 'submit', font = ('arial',15), fg = 'white', bg = 'red',relief = 'raised',bd = 5 , command = lambda : [do()])
#        sub.place(x = 350 , y = 220)

#        stockfile.close()
#        backbutton = tkinter.Button(swindow,text = 'back', font = ('arial',15),relief ='raised',bd = 5, fg = 'white',bg = 'red',command = lambda : [swindow.destroy(),startsecondwindow()])
#        backbutton.place(x = 0,y = 0)
###############################################################FIRST WINDOW################################################################
def destroy_and_start():
       window.destroy()
       startsecondwindow()
window = tkinter.Tk()
window.attributes('-fullscreen',True)
backwindow = tkinter.Tk()
backwindow.attributes('-fullscreen',True)
backwindow.config(background = 'red')
backwindow.title('MOBILE MANAGEMENT SYSTEM')
image1 = tkinter.PhotoImage(file = 'LOGO.gif')
photolabel = tkinter.Button(window,image = image1,relief = 'ridge', bd  = 15, activebackground = 'red',bg = 'blue',command = lambda : destroy_and_start())
photolabel.pack(fill = 'both')
tkinter.mainloop()

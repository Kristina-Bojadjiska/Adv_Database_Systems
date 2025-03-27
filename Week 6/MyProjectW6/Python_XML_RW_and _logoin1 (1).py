from tkinter import *
from tkinter import messagebox
from functools import partial
import sqlite3
import hashlib




# Window
tkWindow = Tk()  
tkWindow.geometry('400x250')  
tkWindow.title('Tkinter SQLite Login Form example ')

# importing element tree
# under the alias of ET

import xml.etree.ElementTree as ET

def read_XML():
        
        # Passing the path of the
        # xml document to enable the
        # parsing process
        tree = ET.parse('login_details.xml')
 
        # getting the parent tag of
        # the xml document
        root = tree.getroot()
 
        # printing the root (parent) tag
        # of the xml document, along with
        # its memory location
        print(root)
 
        # printing the attributes of the
        # first tag from the parent 
        print(root[0].attrib)
 
        # printing the text contained within
                
        # the parent
        for row in root[0]:
                print(row.text)
               



def write_xml():

        connection_obj = sqlite3.connect("db1")
        cursor_obj = connection_obj.cursor()
        cursor_obj.execute("SELECT * FROM login_details;")
        get_login_details=cursor_obj.fetchall()
        # This is the parent (root) tag 
        # onto which other tags would be
        # created
        data = ET.Element('user')
         
        # Adding a subtag named `login`
        # inside our root tag
        element1 = ET.SubElement(data, 'login_dartais')
         
        # Adding subtags under the `login`
        # subtag 
        for row in get_login_details:
                s_elem1 = ET.SubElement(element1, 'login')
                s_elem2 = ET.SubElement(element1, 'password')
         
                # Adding attributes to the tags under
                # `items`
                #s_elem1.set('type', 'login')
                #s_elem2.set('type', 'Declined')
         
                # Adding text between the `E4` and `D5` 
                # subtag
                s_elem1.text = row[0]
                s_elem2.text = row[1]
         
        # Converting the xml data to byte object,
        # for allowing flushing data to file 
        # stream
        b_xml = ET.tostring(data)
         
        # Opening a file under the name `items2.xml`,
        # with operation mode `wb` (write + binary)
        with open("login_details.xml", "wb") as f:
            f.write(b_xml)


       
       

write_xml()


read_XML()
def validateLogin(username, password):
	
        connection_obj = sqlite3.connect("db1")
        cursor_obj = connection_obj.cursor()

        value_username=username.get()
        value_password=str(password.get())


        password_hash_result = hashlib.sha256(value_password.encode())
        
        cursor_obj.execute("SELECT * FROM login_details WHERE User_Login='"+value_username+"'"+" AND User_password='"+
                           str(password_hash_result.hexdigest())+"'")
        output1=cursor_obj.fetchall()

        if len(output1)>0:
                print("hi")
                messagebox.showinfo("showinfo", "correct login and password")
        else:
                print("no")
                messagebox.showwarning("Warning","Incorrect login or password")
                
        for row in output1:
                print(row)
  
        connection_obj.commit() 
  
        # Close the connection 
        connection_obj.close()
       

def register_customer(username, password):
	
        connection_obj = sqlite3.connect("db1")
        cursor_obj = connection_obj.cursor()
        value_username=username.get()
        value_password=str(password.get())
        #encrypton
        #encode(value_password, password = 'mypass')
        
        #value_password.encode()



        ####
          
        # encoding value_password using encode() 
        # then sending to SHA256() 

        #password_hash_result = hashlib.sha256(value_password.encode())

        #Python String encode() converts a string value into a collection of bytes, using an encoding scheme specified by the user
  
        # printing the equivalent hexadecimal value. 
        #print("The hexadecimal equivalent of SHA256 is : ")
        #print(password_hash_result.hexdigest()) 

        #####
        
        if len(value_password)>=5 and len(value_username)>=5:
                #cursor_obj.execute("insert into login_details values('"+value_username+"', '"+str(encvalue_password)+"')")
                cursor_obj.execute("insert into login_details values('"+value_username+"', '"+value_password+"')")
                #cursor_obj.execute("insert into login_details values('"+value_username+"', '"+str(password_hash_result.hexdigest())+"')")
                messagebox.showinfo("showinfo", "user registred")
        else:
                messagebox.showwarning("Warning","Incorrect length of password and login - min 5 symbols")
                
        connection_obj.commit() 
  
        # Close the connection 
        connection_obj.close()
       

# Username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

# Password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

# Login button
loginButton1 = Button(tkWindow, text="Login", command=validateLogin).grid(row=3, column=0)

register_customer = partial(register_customer, username, password)
#register
loginButton2 = Button(tkWindow, text="Register", command=register_customer).grid(row=3, column=1)

 


tkWindow.mainloop()

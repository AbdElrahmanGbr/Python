#!/usr/bin/env python3
import re # regular expressions
import MySQLdb # MySQL database

mydb = MySQLdb.connect(
  host="localhost",
  user="root",
  password="",
  database="python-database"
)

cur = mydb.cursor() # create a cursor object to execute queries and fetch results from the database
cur.execute('''CREATE TABLE IF NOT EXISTS employee(
            id int primary key not null,
            full_name varchar(50) not null,
            salary int not null,
            is_manager int
            );''')
mydb.commit() # commit the changes to the database


class Person: # Person class to store general information about a person (employee or manager)
   def __init__(self, full_name, money,sleepmood,healthRate): # constructor method for Person class
      self.full_name = full_name
      self.money = money
      self.sleepmood = sleepmood
      self.healthRate = healthRate

  
   def sethealthRate(self, healthRate): # setter method for healthRate attribute of Person class
       if healthRate>=0 and healthRate<=100:
          self.healthRate=healthRate
       else:
          print('out of range')

   def sleep(self,hours): # setter method for sleep attribute of Person class
      if hours==7: # if hours is 7 then sleepmood is 100 and so on
          self.sleepmood = 'happy'
          print('your sleepmood changed to happy')
      elif hours > 7:
          self.sleepmood = 'lazy'
          print('your sleepmood changed to lazy')
      elif hours < 7:
          self.sleepmood = 'tired'
          print('your sleepmood changed to tired')
      return self.sleepmood

   def eat(self,meals): # setter method for eat attribute of Person class
       if meals<=3 and meals>=1:
            if meals==3: # if meals is 3 then healthRate is 100 and so on
                self.healthRate = '100'
                print('your healthRate changed to 100')
            elif meals==2:
                self.healthRate = '75'
                print('your healthRate changed to 75')
            elif meals==1:
                self.healthRate = '50'
                print('your healthRate changed to 50')
            return self.healthRate
       else:
           print('out of range')

   def buy(self,items): # setter method for buy attribute of Person class
      if items==1:
          self.money-=10
          print('Your money decreased by 10')


class Employee(Person): # Employee class to store employee information

   def __init__(self,full_name, money,sleepmood,healthRate, id, email, workmood,salary,is_manager): # constructor method for Employee class
      Person. __init__(self, full_name, money,sleepmood,healthRate) # call the constructor of the Person class to initialize the attributes of the Employee class

      self.id = id
      self.email = email
      self.workmood = workmood
      self.salary = salary
      self.is_manager = is_manager

      sql="INSERT INTO employee (id, full_name, salary,is_manager) Values " \
            "(%s,%s,%s,%s)"
      val = (self.id,self.full_name, self.salary, self.is_manager)
      cur.execute(sql, val)
      print("employee added")  
      mydb.commit()

    
   def setsalary(self, salary): # setter method for salary attribute of Employee class
       if(salary>=10000):
          self.salary = salary
       else:
          print('out of range')
    
   def getsalary(self): # getter method for salary attribute of Employee class
       return self.salary

   def setemail(self, email): # setter method for email attribute of Employee class
      if(re.search('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', email)): # regular expression to check if the email is valid
         self.email = email # if the email is valid, set the email attribute of the Employee class
      else:
         print("Invalid Email")



   def work(self,hours): # setter method for work attribute of Employee class
      if hours==8: # if the hours are 8, set the workmood attribute of the Employee class to 'happy' and so on
          self.workmood = 'happy'
          print('your workmood changed to happy')
      elif hours < 8:
          self.workmood = 'lazy'
          print('your workmood changed to lazy')
      elif hours > 8:
          self.workmood = 'tired'
          print('your workmood changed to tired')
      return self.workmood

   def sendemail(self,to,subject,sender): # setter method for sendemail attribute of Employee class
      f=open('email.txt','w') # open the email.txt file in write mode
      # write the email to the file
      f.write(f'This email is sent to : {to} \n')
      f.write(f'This email subject is :{subject} \n')
      f.write(f'This email sender is : {sender} \n')
      f.close()# close the file


class Office: # Office class to store office information

   def __init__(self): # constructor method for Office class
       pass
  
   def get_all_employees(self): # getter method for get_all_employees attribute of Office class
       cur.execute('select * from employee') # execute the query to get all the employees
       rows = cur.fetchall() # fetch the results from the database
       for row in rows: # print the results
            print(row)
       mydb.commit()
   
   def get_employee(self,num): # getter method for get_employee attribute of Office class
            cur.execute(f'select * from employee where id={num}') # execute the query to get the employee with the given id
            rows = cur.fetchall() # fetch the results from the database
            for row in rows: # print the results
                print(row)
            mydb.commit()


   def hire(self,id,full_name,salary,is_manager): # setter method for hire attribute of Office class
      sql="INSERT INTO employee (id, full_name, salary,is_manager) Values " \
      "(%s,%s,%s,%s)" # insert the employee with the given id, full_name, salary and is_manager to the database
      val = (id,full_name,salary,is_manager) # set the values of the employee
      cur.execute(sql, val) # execute the query
      print("employee hired") # print the message
      mydb.commit()

   def fire(self,num): # setter method for fire attribute of Office class
      cur.execute(f'delete from employee where id={num}') # execute the query to delete the employee with the given id
      print("employee fired")
      mydb.commit()

# o=Office()
# print(o.get_all_employees())
# print(o.get_employee('1'))
# print(o.hire(3,'sherif',10000,1))
# # print(o.fire('3'))


flag=True
while flag: # loop to keep the program running
    print ("""
    1.Add a Employees
    2.Get All Employees
    3.Exit/Quit
    """)
    flag=input("What would you like to do? ")  # ask the user what they would like to do
    print("==========================================================")
    if flag=="1": # if the user wants to add a employee
       newEmployee=Office() # create an object of the Office class and then ask for the user inputs

       id = input("Enter your id: ")
       name = input("Enter your name: ")
       salary = input("Enter your salary: ")
       is_manager = input("Enter your is_manager: ")
       newEmployee.hire(id,name,salary,is_manager)# call the hire method of the Office class to add the employee to the database
    elif flag=="2": # if the user wants to get all the employees
       newEmployee=Office()# create an object of the Office class
       newEmployee.get_all_employees()# call the get_all_employees method of the Office class to get all the employees from the database
    elif flag=="3":# if the user wants to exit
      print("\n Goodbye") # print this message
      flag=False # set the flag to False
    elif flag !="": # if the user enters something other than 1,2,3
      print("\n Not Valid Choice Try again") # print this message
      
      
      
mydb.close() # close the database
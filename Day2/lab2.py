#!/usr/bin/env python3
import re  # regular expressions
import MySQLdb  # MySQL database

mydb = MySQLdb.connect(
    host="localhost",
    user="root",
    password="",
    database="python-database"
)

# create a cursor object to execute queries and fetch results from the database
cur = mydb.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS employee(
            id int primary key not null,
            full_name varchar(50) not null,
            salary int not null,
            is_manager int
            );''')
# create email table
cur.execute("create table if not exists email (mailto varchar(255), subject varchar(255), sender varchar(255))")
mydb.commit()  # commit the changes to the database


# Person class to store general information about a person (employee or manager)
class Person:
    # constructor method for Person class
    def __init__(self, full_name, money, sleepmood, healthRate):
        self.full_name = full_name
        self.money = money
        self.sleepmood = sleepmood
        self.healthRate = healthRate

    # setter method for healthRate attribute of Person class
    def sethealthRate(self, healthRate):
        if healthRate >= 0 and healthRate <= 100:
            self.healthRate = healthRate
        else:
            print('out of range')

    def sleep(self, hours):  # setter method for sleep attribute of Person class
        if hours == 7:  # if hours is 7 then sleepmood is 100 and so on
            self.sleepmood = 'happy'
            print('your sleepmood changed to happy')
        elif hours > 7:
            self.sleepmood = 'lazy'
            print('your sleepmood changed to lazy')
        elif hours < 7:
            self.sleepmood = 'tired'
            print('your sleepmood changed to tired')
        return self.sleepmood

    def eat(self, meals):  # setter method for eat attribute of Person class
        if meals <= 3 and meals >= 1:
            if meals == 3:  # if meals is 3 then healthRate is 100 and so on
                self.healthRate = '100'
                print('your healthRate changed to 100')
            elif meals == 2:
                self.healthRate = '75'
                print('your healthRate changed to 75')
            elif meals == 1:
                self.healthRate = '50'
                print('your healthRate changed to 50')
            return self.healthRate
        else:
            print('out of range')

    def buy(self, items):  # setter method for buy attribute of Person class
        if items == 1:
            self.money -= 10
            print('Your money decreased by 10')


class Employee(Person):  # Employee class to store employee information

    # constructor method for Employee class
    def __init__(self, full_name, money, sleepmood, healthRate, id, email, workmood, salary, is_manager):
        # call the constructor of the Person class to initialize the attributes of the Employee class
        Person. __init__(self, full_name, money, sleepmood, healthRate)

        self.id = id
        self.email = email
        self.workmood = workmood
        self.salary = salary
        self.is_manager = is_manager

        sql = "INSERT INTO employee (id, full_name, salary,is_manager) Values " \
            "(%s,%s,%s,%s)"
        val = (self.id, self.full_name, self.salary, self.is_manager)
        cur.execute(sql, val)
        print("employee added")
        mydb.commit()

    def setsalary(self, salary):  # setter method for salary attribute of Employee class
        if(salary >= 10000):
            self.salary = salary
        else:
            print('out of range')

    def getsalary(self):  # getter method for salary attribute of Employee class
        return self.salary

    def work(self, hours):  # setter method for work attribute of Employee class
        if hours == 8:  # if the hours are 8, set the workmood attribute of the Employee class to 'happy' and so on
            self.workmood = 'happy'
            print('your workmood changed to happy')
        elif hours < 8:
            self.workmood = 'lazy'
            print('your workmood changed to lazy')
        elif hours > 8:
            self.workmood = 'tired'
            print('your workmood changed to tired')
        return self.workmood


class Office:  # Office class to store office information

    def __init__(self):  # constructor method for Office class
        pass

    # getter method for get_all_employees attribute of Office class
    def get_all_employees(self):
        # execute the query to get all the employees
        cur.execute('select * from employee')
        rows = cur.fetchall()  # fetch the results from the database
        for row in rows:  # print the results
            print(row)
        mydb.commit()

    def get_employee(self, num):  # getter method for get_employee attribute of Office class
        # execute the query to get the employee with the given id
        cur.execute(f'select * from employee where id={num}')
        rows = cur.fetchall()  # fetch the results from the database
        for row in rows:  # print the results
            print(row)
        mydb.commit()

    # setter method for hire attribute of Office class
    def hire(self, id, full_name, salary, is_manager):
        sql = "INSERT INTO employee (id, full_name, salary,is_manager) Values " \
            "(%s,%s,%s,%s)"  # insert the employee with the given id, full_name, salary and is_manager to the database
        # set the values of the employee
        val = (id, full_name, salary, is_manager)
        cur.execute(sql, val)  # execute the query
        print("employee hired")  # print the message
        mydb.commit()

    def fire(self, num):  # setter method for fire attribute of Office class
        # execute the query to delete the employee with the given id
        cur.execute(f'delete from employee where id={num}')
        print("employee fired")
        mydb.commit()

    def update_employee(self, id, full_name, salary, is_manager):
        # execute the query to update the employee with the given id
        cur.execute(f"update employee set full_name='{full_name}', salary={salary}, is_manager={is_manager} where id={id}")
        print("employee updated")
        mydb.commit()

    def send_email(self, mailto, subject, sender):
        # validation for the email with regex
        if re.match(r'^[a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+\.[a-zA-Z]{2,5}$', mailto or sender):
            # execute the query to insert the email to the database
            cur.execute(f"insert into email (mailto, subject, sender) values ('{mailto}', '{subject}', '{sender}')")
            print("email sent")
            mydb.commit()
            f = open('email.txt', 'a')  # open the email.txt file in append mode
            f.write(f'To: {mailto}\n')  # write the To: email address to the file
            f.write(f'Subject: {subject}\n')  # write the Subject: email address to the file
            f.write(f'From: {sender}\n')  # write the From: email address to the file
            f.write('\n')  # write a new line to the file
            f.close()  # close the file
        else:
            print("invalid email")
            

flag = True
while flag:  # loop to keep the program running
    print("""
    1.Hire a new Employee
    2.Display All Employees
    3.Display Employee by ID
    4.Fire Employee
    5.Update Employee
    6.Send Email
    7.Exit/Quit
    """)
    flag = input(
        "What would you like to do? ")  # ask the user what they would like to do
    print("==========================================================")
    if flag == "1":  # if the user wants to add a employee
        # create an object of the Office class and then ask for the user inputs
        newEmployee = Office()

        id = input("Enter your id: ")
        full_name = input("Enter your full name: ")
        salary = input("Enter your salary: ")
        is_manager = input(
            "Is this employee a manager? (1 for yes, 0 for no): ")
        # call the hire method of the Office class to add the employee to the database
        newEmployee.hire(id, full_name, salary, is_manager)
    elif flag == "2":  # if the user wants to get all the employees
        newEmployee = Office()  # create an object of the Office class
        # call the get_all_employees method of the Office class to get all the employees from the database
        newEmployee.get_all_employees()
    elif flag == "3":  # if the user wants to get an employee by id
        newEmployee = Office()  # create an object of the Office class
        id = input("Enter your id: ")
        # call the get_employee method of the Office class to get an employee from the database
        newEmployee.get_employee(id)
    elif flag == "4":  # if the user wants to fire an employee
        newEmployee = Office()  # create an object of the Office class
        id = input("Enter your id: ")
        # call the fire method of the Office class to fire an employee from the database
        newEmployee.fire(id)
    elif flag == "5":  # if the user wants to update an employee
        newEmployee = Office()  # create an object of the Office class
        id = input("Enter your id: ")
        full_name = input("Enter your full name: ")
        salary = input("Enter your salary: ")
        is_manager = input(
            "Is this employee a manager? (1 for yes, 0 for no): ")
        # call the update_employee method of the Office class to update an employee from the database
        newEmployee.update_employee(id, full_name, salary, is_manager)
    elif flag == "6":  # if the user wants to send an email
        newEmployee = Office()  # create an object of the Office class
        mailto = input("Enter the email address of the recipient: ")
        subject = input("Enter the subject of the email: ")
        sender = input("Enter your email address: ")
        # call the sendemail method of the Office class to send an email
        newEmployee.send_email(mailto, subject, sender)
    elif flag == "7":  # if the user wants to exit the program
        print("Thank you for using our program")
        flag = False  # set the flag to false to exit the loop
    elif flag != "":  # if the user enters something other than 1,2,3
        print("\n Not Valid Choice Try again")  # print this message


mydb.close()  # close the database

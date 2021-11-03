# 1- Workbench IDE ile schooldb isminde bir database oluşturup Student tablosunu ekleyiniz.
    # Id,StudentNumber,Name,Surname,Birthdate,Gender

# 2- Database bağlantısını oluşturunuz. (connection.py)

# 3- Aşağıdaki bilgiler için insert sorguları oluşturup kayıtları ekleyiniz.

    # ("301","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
    # ("302","Ali","Can",datetime(2005, 6, 17),"E"),
    # ("303","Canan","Tan",datetime(2005, 7, 7),"K"),
    # ("304","Ayşe","Taner",datetime(2005, 9, 23),"K"),
    # ("305","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
    # ("306","Ali","Cenk",datetime(2003, 8, 25),"E")
import mysql.connector
from datetime import datetime
from conschooldb import connection
import pandas as pd
class Student:
    connection = connection
    mycursor=connection.cursor()

    def __init__(self,studentnumber,name,surname,birtday,gender) -> None:
        self.studentnumber=studentnumber
        self.name=name
        self.surname=surname
        self.birtday=birtday
        self.gender=gender

    def saveStudent(self):
        sql="INSERT INTO students(StudentNumber,Name,Surname,Birtday,Gender) VALUES(%s,%s,%s,%s,%s)"
        value = (self.studentnumber,self.name,self.surname,self.birtday,self.gender)

        Student.mycursor.execute(sql,value)
        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} kayıt eklendi")
        except mysql.connector.Error as err:
            print("hata: ",err)
        finally:
            Student.connection.close()    
    
    @staticmethod
    def saveStudents(students):
        sql="INSERT INTO students(StudentNumber,Name,Surname,Birtday,Gender) VALUES(%s,%s,%s,%s,%s)"
        values = students

        Student.mycursor.executemany(sql,values)
        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} kayıt eklendi")
        except mysql.connector.Error as err:
            print("hata: ",err)
        finally:
            Student.connection.close()   

ahmet=Student(620,"ahmet","ahmet",datetime(1990,5,25),"E")
ahmet.saveStudent()

ögrenciler=[("401","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
    ("402","Ali","Can",datetime(2005, 6, 17),"E"),
    ("403","Canan","Tan",datetime(2005, 7, 7),"K"),
    ("404","Ayşe","Taner",datetime(2005, 9, 23),"K"),
    ("405","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
    ("406","Ali","Cenk",datetime(2003, 8, 25),"E")]

# Student.saveStudents(ögrenciler)
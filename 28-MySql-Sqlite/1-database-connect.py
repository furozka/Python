import mysql.connector

#ilgili databaseye loval server uzerinden bağlanma
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql05.",
    database="mydatabase"
) 

#script kullanmamıza yarayan cursor
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE databasem") #database oluşturma scripti
mycursor.execute("SHOW DATABASES") #database göstertme scripti for dongusu ile kullanıyorsun
for x in mycursor:
    print(x)

#ilgili databasede tablo oluşturma scripti
mycursor.execute("CREATE TABLE customers(name VARCHAR(255),adress VARCHAR(255))")
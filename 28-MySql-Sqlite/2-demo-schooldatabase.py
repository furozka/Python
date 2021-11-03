#uygulama school database
#schooldb adında workbench ten database oluştur
#student adında tablo oluştur
#columnlar id,name,surname,birthday,gender olsun
#connect ile bağla
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql05.",
    database="schooldb"
)

mycursor=mydb.cursor()
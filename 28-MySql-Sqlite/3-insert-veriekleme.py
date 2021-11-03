import mysql.connector

#bir kayıt ekleme
def insertProduct(name,price,imageUrl,description):
    connection=mysql.connector.connect(host="localhost",user="root",password="Mysql05.",database="node.app")

    cursor=connection.cursor()

    sql="INSERT INTO products(name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"
    values = (name,price,imageUrl,description)

    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi") #eklenen row sayısı
        print(f"Eklenen son kaydın id numarası: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata", err)
    finally:
        connection.close()
        print("Database closed")

#çoklu ekleme
def insertProducts(liste):
    connection=mysql.connector.connect(host="localhost",user="root",password="Mysql05.",database="node.app")

    cursor=connection.cursor()

    sql="INSERT INTO products(name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"
    values = liste

    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi") #eklenen row sayısı
        print(f"Eklenen son kaydın id numarası: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata", err)
    finally:
        connection.close()
        print("Database closed")

liste=[]
while True:

    name=input("ürün adı: ")
    price=float(input("ürün fiyatı: "))
    imageUrl=input("ürün resmi: ")
    description=input("ürün açıklaması: ")
    liste.append((name,price,imageUrl,description))

    result=input("devam etmek istiyormusunuz e-h: ")
    if result=="h":
        print("kayıtlarınız aktarılıyor...")
        print(liste)
        insertProducts(liste)
        break
# insertProduct(name,price,imageUrl,description)
import csv
# def add_user(firstname,lastname):
#     with open("users.csv",mode="a", encoding="UTF-8", newline="") as f:
#         csv_writer=csv.writer(f)
#         csv_writer.writerow([firstname,lastname])

# add_user("Furkan","Özkan")
# add_user("Süleyman","Özbey")

# def get_users():
#     with open("users.csv",mode="r",encoding="UTF-8",newline="") as f:
#         csv_reader=csv.DictReader(f)
#         for p in csv_reader:
#             print(f'{p["FirstName"]} {p["LastName"]}')

# get_users()

# def find_user(firstname,lastname):
#     with open("users.csv",mode="r",encoding="UTF-8") as f:
#         csv_reader=csv.reader(f)
#         # next(csv_reader)
#         for (index,row) in enumerate(csv_reader):
#             if(row[0]==firstname) and (row[1]==lastname):
#                 return index
#         return -1

# print(find_user("Furkan","Özkan"))

def update_users(firstname,lastname,newfname,newlname):
    with open("users.csv",mode="r",encoding="UTF-8",newline="") as f:
        csv_reader=csv.reader(f)
        users=list(csv_reader)
    count=0
    with open("users.csv",mode="w",encoding="UTF-8",newline="") as f2:
        csv_writer=csv.writer(f2)
        for p in users:
            if p[0]==firstname and p[1]==lastname:
                csv_writer.writerow([newfname,newlname])
                count+=1
            else:
                csv_writer.writerow(p)
    return f"{count} tane kayıt güncellendi"

print(update_users("Furkan","Özkan","Mühendis","Çalışkan"))

def delete_user(firstname,lastname):
    with open("users.csv",mode="r",encoding="UTF-8",newline="") as f:
        csv_reader=csv.reader(f)
        users=list(csv_reader)
    count=0
    with open("users.csv",mode="w",encoding="UTF-8",newline="") as f2:
        csv_writer=csv.writer(f2)
        for p in users:
            if p[0]==firstname and p[1]==lastname:
                count+=1
            else:
                csv_writer.writerow(p)
    return f"{count} tane kayıt silindi"

print(delete_user("Süleyman","Özbey"))
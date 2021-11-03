#int
#float
#string
#bool
x=int(input("x: "))
y=int(input("y: "))
toplam=x+y
print(toplam)
print(type(x))
print(type(y))
age=4
weight=12.5
name="çınar"
isStudent=True
print("age , weight name isstudent types:")
print(type(age))
print(type(weight))
print(type(name))
print(type(isStudent))
print("ageyi floata ceviriyoruz int di")
result=float(age)
print(result)
print(type(result))
print("weighti integere ceviriyoruz 12.5 di floattı")
result=int(weight)
print(result)
print(type(result))
print("bool türündeki isStudenti stringe çeviriyoruz")
print("is student türü",type(isStudent))
result=str(isStudent)
print(isStudent)
print(type(result))
print("print(int(True))")
print(int(True))
print("print(int(False))")
print(int(False))
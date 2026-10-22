#پروژه دوم
#دفترچه مخاطبین
#دیکشنریهایی داخل یک دیکشنری جامع
def contacts():
    name=input ("name:")
    number=input("number:")
    while not number.isdigit():
        print("invalid input")
        number=input("number:")
    print("valid input")
    age=int(input("age:"))
    city=input("city:")
    each={
        "name":name ,
        "number": number ,
        "age": age,
        "city":city
    }
    return each

i=int(input("how many contacts do you have?:"))

all_contacts={}
for x in range (i):
    person=contacts()
    all_contacts[person["name"]]=person
print(all_contacts)
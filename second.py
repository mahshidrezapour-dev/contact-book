#پروژه دوم
#دفترچه مخاطبین
#دیکشنریهایی داخل یک دیکشنری جامع
def contacts():
    while True:
        name=input ("name:")
        if name:
            break
        print("Name cannot be empty")
    while True:
        number=input("number:").strip()
    if number.isdigit() and 7 < len(number) < 11 :
        break
    print("enter valid phone number")
    while True:
        try:
            age=int(input("age:"))
            if age <0:
                print("age cannot be negative.")
            else:
                break
        except ValueError:
            print("please enter a valid integer.")
    city=input("city:")
    each={
        "name":name ,
        "number": number ,
        "age": age,
        "city":city
    }
    return each
while True:
    try:
        i=int(input("how many contacts do you have?:"))
        if i <0:
            print("number of contacts cannot be negative")
        else:
            break
    except ValueError:
        print("please enter a valid integer")
all_contacts={}
for x in range (i):
    person=contacts()
    while prson["name"] in all_contacts:
        print("this contact already exists.")
        person["name"]=input("enter another name: ").strip()
    all_contacts[person["name"]]=person
print(all_contacts)

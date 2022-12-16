import json

#the user can have more than one number, realise this function with add , make function that take phone numbers from user until he types: "stop", it brings phones spisok.

def load():
            # загрузить из json
            fname='phonebook1.json' #открываем файл
            with open(fname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
                BD_local = json.load(fh)  # загружаем из файла данные в словарь data
            print('БД успещно загружена')
            return BD_local

def save():
            # сохранить в json
            with open('phonebook1.json', 'w', encoding='utf-8') as fh:  # открываем файл на запись
                fh.write(json.dumps(phonebook1,
                                    ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
            print('БД успещно сохранена')

try:
    phonebook1 = load()
except:
    phonebook1 = {"Mikael":{"birthyear":2007,"city":"Yavne","phones":[103123,123124,315133]},
                  "Timur":{"birthyear":1999,"city":"Moscow","phones":[1231422,532562,253256]}}

print("Im chat bot , i will answer your questions")

while True:
    command = input("write command: ")
    if command == "show":
        for i,g in phonebook1.items():
            print(i,g)
    elif command == "exit":
        break
    elif command == "add":
        command1 = input("add the name of contact: ")
        command2 = int(input("add the telephone number: "))
        command3 = int(input("add the birth year: "))
        command4 = input("add city: ")
        phonebook1[command1] = {"birthyear":command3,"phones":[command2],"city":command4}
        print("The contact was saved succesfully!")
        
    elif command == "add phone":
            phones = []
            name = input("enter someones name to add him phone numbers or write exit to get out: ")
            while True:
                phones1 = input("enter phone number or write exit to get out: ")
                if phones1 == "exit":
                    phonebook1[name]["phones"] += phones
                    print("phone numbers were added succesfully")
                    break
                else:
                    phones.append(int(phones1))
                
                
            
    elif command == "save":
        save()
    elif command == "load":
        phonebook1 = load()
    elif command == "find contact":
        command4 = input("Enter your contact for search: ")
        for contact in phonebook1:
            if command4 in contact:
                print(phonebook1[contact])
    elif command == "find city":
        command5 = input("Enter city for search: ")
        for i,g in phonebook1.items():
            if command5 == g["city"]:
                print(i,g)
    elif command == "find birthyear":
        command6 = int(input("Enter birthyear for search: "))
        for i,g in phonebook1.items():
            if command6 == g["birthyear"]:
                print(i,g)
        
    else:
        print("i dont understand you")
    

import csv
while True:
    print("-"*20,"ContactMaster","-"*20)
    print("""
            Press 1 for 'Add Contact'
            Press 2 for 'Delete Contact'
            Press 3 for 'Search Contact'
            Press 4 for 'Display Contact'
            Press 5 for 'Exit'    """)
    try:
        user = int(input(''))
        if user == 1:
            print("-"*10,"Adding Contact","-"*10)
            print()
            name_status = False
            ph_status = False
            while 1:
                try:
                    name = input("Enter Name : ")
                    if name.isdigit():
                        print("A Name Cann't Be A Number")
                        name_status = False
                    elif name == '' or name.isspace():
                        print('Name Never contains Space')
                        name_status = False
                    else:
                        name_status = True
                        break
                except Exception:
                    print("Something Entered Wrong ")
            while 1:       
                try:
                    ph = int(input("Enter Phone Number : "))
                    test_ph = str(ph)
                    if len(test_ph) ==10:
                        ph_status = True
                        break
                    else:
                        print("Phone Number Must Have 10 Digits")
                        ph_status = False
                except Exception:
                    print("Something Entered Wrong")
                
            if name_status == True and ph_status == True:
                contact_add = {
                'Name':name,
                'Phone':ph
                }
            try:
                with open('contact.csv','a',newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=contact_add.keys())
                    if file.tell()==0:
                        writer.writeheader()
                    writer.writerow(contact_add)
                    print()
                    print("Contact Saved Successfully...")
                    print()
            except Exception as e:
                print("Something Went Wrong ...")

        elif user == 2:
            print("-"*20,"ContactMaster","-"*20)
            del_contact = input('Enter Name To Delete : ')
            print()
            try:
                with open('contact.csv',newline='') as file:
                    reader = csv.DictReader(file)
                    fieldname = reader.fieldnames
                    rows = [i for i in reader if i['Name']!= del_contact ]
                with open('contact.csv','w',newline='') as file2:
                    writer = csv.DictWriter(file2,fieldnames=fieldname)
                    writer.writeheader()
                    writer.writerows(rows)
                print('Contact Deleted Successfully...')
            except Exception :
                print("Name Doesn't Exist")
        elif user == 3:
            try:
                user = input("Enter Name To Search : ")
                with open('contact.csv') as r:
                    reader = csv.DictReader(r)
                    res = [(i['Name'],i['Phone']) for i in reader if user in i['Name']]
                    if res == []:
                        print("Name Doesn't Matched Enter A Valid Name ")
                    print(res)
            except Exception as e :
                print("Something Went Wrong.. Please Try Again ...")
        elif user == 4:
            try:
                with open('contact.csv') as fp:
                    reader = csv.DictReader(fp)
                    res = [i for i in reader]
                    print([(i['Name'],i['Phone']) for i in res])
            except Exception:
                print("File Doesn't Exist")
        elif user == 5:
            print()
            print("Thanks For Using ContactMaster....")
            print()
            exit()
        else:
            print('You have chosen a wrong option, Please try again')
    except Exception as e :
        print("Wrong Entry ... Please Try Again")

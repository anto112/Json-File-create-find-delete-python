
# to acces the json module 
import json

# global variable
Student_ID = {}
print ("<<<This system Is list Student ID, so lets do it >>> \n========================================================")
# call by reference
with open('data.json', 'r') as f:
          Student_ID = json.loads(f.read())
          # print (Student_ID)

# local vaariable
def add_entry(): 
    name = input('Who do you want to add to the Student ID Dictionnary?\n').title()
    date = input('Student ID {} ?\n'.format(name))
    Student_ID[name] = date
    with open('data.json', 'w') as f:
        json.dump(Student_ID, f)
    print('student ID {} was added to data list\n'.format(name))

def find_data():
    # call by value
    name = input("who's Student ID do you want to know?\n").title()
    try :
        if Student_ID[name]:
            print('{} Student ID is {}\n'.format(name, Student_ID[name]))
    except KeyError:
        print('{} is not in the list\n'.format(name))

def list_entries():
    x = (len(Student_ID))
    print('The current entries in data list are {} people:\n============================================'.format(x))
    # for student in (sorted(student_Dict.values(), key=operator.attrgetter('age'))):
    # print(student.name)
    for key in (sorted(Student_ID)):
        print(key.ljust(20), ':', Student_ID[key])

    print()

def askUser():
    username = input("username: ")
    password = input("password: ")
    checkPass(username, password)
def checkPass(use, pwd):
    if use == "user" and pwd == "user123":
        print ("Welcome " + use)
        print ("You have successfully logged in !")
        login(use)
    else:
        print ("Your username and/or password was incorrect")
        askUser()
def logout_account():
    next_again = input ('do you want login again :Yes, No\n').capitalize()
    if next_again =='Yes':
        askUser()
    elif next_again == 'No':
        print("Good Bye, Thanks for coming !!!\n")
        raise SystemExit(0)
def delete_list():
    name = input ('who you want to delete from list \n').title()
    try :
        if Student_ID [name]:
            Student_ID.pop(name)
            with open('data.json', 'w') as f:
                json.dump(Student_ID, f)
        print("%s was delete from list\n" % name)
    except KeyError:
        print("%s is not in the list" % name)

# while user =checkPass(use,pwd):
# control flow (looping)
def login(use):
    what_next = input('What do you want? you can: Add, Delete, Find, List, Logout\n').capitalize()
    if what_next == 'Logout':
        logout_account()
    elif what_next == 'Add':
        add_entry()
    elif what_next == 'Find':
        find_data()
    elif what_next == 'List':
        list_entries()
    elif what_next == 'Delete':
        delete_list()
    login(use)
askUser()

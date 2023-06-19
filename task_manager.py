#L1T24 CT1&2 Capstone porject 3

# Import modules always on top, followed by defined functions
from datetime import datetime


def reg_user(filename) :
    with open("user.txt","a+") as filename: # OI error fixed, check task 27
                filename.writelines("\n")
                filename.writelines(new_username)
                filename.writelines(", ")
                filename.writelines(new_password_verify) 

def add_task_read(filename) :
    with open("tasks.txt","r+") as filename: 
            for lines in filename : 
             temp = lines.strip()
             temp = temp.split(", ")

def add_task_write(filename) :
    with open("tasks.txt","a+") as filename:
    # .write (to write a string) curely brackets many variables .writelines one argument
        filename.write(f"\n{user_name_task}, {task_title}, {task_description}, {task_due_date}, {current_date}, {task_complete}, {task_number}")
        
def view_all(filename) :
     with open("tasks.txt","r+") as filename: 
        for lines in filename : 
            temp = lines.strip()
            temp = temp.split(",")
            print("_________________________________________________________\n")  
            print(f"Tasks:\t\t\t{temp[1]}")   
            print(f"Assigned to:\t\t{temp[0]}")   
            print(f"Date assigned:\t\t{temp[4]}")  # date assigned/ current date
            print(f"Due date:\t\t{temp[3]}")
            print(f"Task Complete:\t\t{temp[5]}")
            print(f"Task Description:\t{temp[2]}")
            print(f"Task number:\t\t{temp[6]}")
            print("_________________________________________________________\n")

# def view_mine(filename) :
#     pass     

def check_overdue(due_date):
    due_date = due_date.strip() # strips spaces & \n
    current_date = datetime.today().strftime("%d %b %Y")
    current_date = datetime.today().strptime(current_date, "%d %b %Y")
    date_due_gr = datetime.strptime(due_date, '%d %b %Y')
    if current_date > date_due_gr  :
        return True
    return False
#vm functions
#test et function works!!
def et():
    idx = int(task_user_number) - 1                          
    with open('tasks.txt', 'r') as f:
        file = f.readlines()
        edit_task_U = input("Edit ,'user_name_task',:\n")
        line = file[idx].split(',')
        line[0] = edit_task_U 
        file[idx] = ','.join(line)

    with open('tasks.txt', 'w') as f:
        for line in file:
            f.write(line)
             
# Create user login by validating user.txt, pass as login
usernames = []
passwords = []
# with open no need to close the file
with open("user.txt","r") as file: 
    for lines in file : 
        temp = lines.strip()
        temp = temp.split(", ")
        # print(temp) # check
        # print(temp[1])
        # print(temp[0])
        usernames.append(temp[0])
        passwords.append(temp[1])
        
print("Please login in using your username and password.")
# print(usernames) # check
# print(passwords) # check

while True:     
    user_name = input("Please enter your username:\n")
    pass_word = input("Please enter your password:\n") 

    if user_name in usernames :
        username_pass_index = usernames.index(user_name)
        # print(username_pass_index) # check
        if pass_word == passwords[username_pass_index]:
            print("You have logged in, Correct username and password entered")
            break
        print("Password incorrect")
    else:   
        print("Login unsuccesfull, Please retry!")
           
while True:
# presenting the menu to the user and 
# making sure that the user input is coneverted to lower case.
# Menu for admin user
    if user_name == 'admin':
        menu = input('''Please select one of the following options below:
r - Registering a user.
a - Adding a task.
va - View all tasks.
vm - View my task.
gr - Generate reports.
ds - Display Statistics.
e - Exit.
 ''').lower() # create menu gr and dependent on list ds, ds nor break if gr not printed. 
# Menu for non Admin user
    else:
        menu = input('''Please select one of the following options:
a - Add task.
va - View all tasks.
vm - View my task.
e - Exit.
 ''').lower().strip() 
    if menu == 'r' and user_name == 'admin': # Only admin can register a user
        
        print("Register as new user")
        new_username = (input("Please enter a new username:\n"))
        # validation username, store if list and check if in list
        new_password = (input("Please enter a new password:\n"))
        new_password_verify = (input("Please confirm your password:\n"))
        # call function
        if new_password == new_password_verify : 
                print("Password verified")  

                while True: 
                    if new_username not in usernames and new_password_verify not in passwords:
                       
                            reg_user('user.txt,')
                            print("You have entered the correct password & username and registered a new user")    
                            break
                    else: 
                        print("Password or username already exists, please retry.")
                        break
                
    
    elif menu == 'a':
        # pass, does nothing if code is written
        add_task_read("tasks.txt,")
            
        user_name_task = input("Please enter your username:\n")
        if user_name_task in usernames:
                task_title = input("Please enter your task title:\n")
                task_description = input("Please enter your task description:\n")
                task_due_date = input("Please enter the due date of task, format as current short:\n") 
                current_date = datetime.today().strftime("%d %b %Y") # string current date
                task_complete = "No"
                task_number = int(input("Please input a number for your task\n"))
                add_task_write("tasks.txt,")
                print("You have created a new task")
        else:
            print("Username doen not exist, cannot add a task")

    elif menu == 'va':
        view_all("tasks.txt,")
                        
    elif menu == 'vm': 
        
        vm_lists = []
        has_tasks = False # boolean
        with open("tasks.txt","r+") as file: 
            for lines in file : 
                temp = lines.strip()
                temp = temp.split(",")
                vm_lists.append(temp)   
                # print(user_name)
                # print(temp[0])
                if user_name == temp[0]: # check if username saved in input.txt in list
                    has_tasks = True    
                    print("_________________________________________________________\n")  
                    print(f"Tasks:\t\t\t{temp[1]}")   
                    print(f"Assigned to:\t\t{temp[0]}")   
                    print(f"Date assigned:\t\t{temp[4]}")  # current date
                    print(f"Due date:\t\t{temp[3]}")
                    print(f"Task Complete:\t\t{temp[5]}")
                    print(f"Task Description:\t{temp[2]}")
                    print(f"Task number:\t\t{temp[6]}")
                    print("_________________________________________________________\n")
            if not has_tasks: #statement must be under for lines in file with open
                    print("You did not have a task") 
                    break       
            task_user_number = (input("Please enter the  task number you would like to edit or -1 to return to menu\n")) 
             
            for lines in vm_lists:       
                if task_user_number == "-1" :
                    break
                elif lines[6].strip() == task_user_number  and lines[5].strip() == "No":  
                    print("Mark task as complete or edit task, Username or due date")

                            
                            
                    menu_VM = input('''Please select one of the following options:
mt - Mark Task
et - Edit task user
ed - Edit due date
ex - Exit.
''').lower().strip()                             
                    if menu_VM == "mt": #def as function
                        
                        idx = int(task_user_number) - 1                          
                        # idx = 1 #automate linked to task number to get list number
                        with open('tasks.txt', 'r') as f:
                                file = f.readlines()
                                task_completed = input('Please enter, Yes, if task completed\n')
                                line = file[idx].split(',')
                                line[5] = task_completed #index no in list in known
                                file[idx] = ','.join(line)

                        with open('tasks.txt', 'w') as f:
                                for line in file:
                                    f.write(line)      
                                                                    
                    elif menu_VM == "et": 
                        et() # works 
                        

                    elif menu_VM == "ed":
                                            
                        idx = int(task_user_number) - 1                          
                        with open('tasks.txt', 'r') as f:
                            file = f.readlines()
                            edit_due_date = input("Edit, task_due_date, d,m,short, year':\n")
                            line = file[idx].split(',')
                            line[4] = edit_due_date
                            file[idx] = ','.join(line)

                        with open('tasks.txt', 'w') as f:
                            for line in file:
                                f.write(line)

                    elif menu_VM == "ex":
                        print("Goodbye!")
                        exit()
                                            
    elif menu == 'gr': 
# tasks       
        with open("tasks.txt", "r+") as f:
            task_list = f.readlines()
            total_tasks = len(task_list)
            completed_tasks = 0
            uncompleted_tasks = 0
            overdue = 0
            per_incomplete = 0
            per_overdue = 0
            for lines in task_list : 
                temp = lines.strip()
                temp = temp.split(",")
                if temp[5].strip().lower() == 'yes':
                    completed_tasks += 1
                else: 
                    uncompleted_tasks += 1  
                if check_overdue(temp[4]) :
                    overdue += 1
            per_incomplete = uncompleted_tasks / total_tasks 
            per_overdue = overdue / total_tasks 
            # print(total_tasks) print any variable to test 
  
# write tasks stats to file                  
        with open('task_overview.txt', 'w+') as f: # write all at once
            f.writelines(f"Total tasks:\t\t{total_tasks}\n")
            f.writelines(f"Completed_tasks:\t{completed_tasks}\n")                       
            f.writelines(f"Uncompleted tasks:\t{uncompleted_tasks}\n")
            f.writelines(f"Overdue tasks:\t\t{overdue}\n")
            f.writelines(f"% incomplete tasks:\t{per_incomplete}%\n")
            f.writelines(f"% overdue tasks:\t{per_overdue}%\n")
# users
        with open("tasks.txt", "r+") as f:
            with open("user.txt", "r+") as g:
                task_list = f.readlines()
                total_tasks1 = len(task_list)
                user_list = g.readlines()
                total_user1 = len(user_list)
                total_task_per_user = 0
                names = []
                for lines in task_list :
                    temp = lines.split(",")
                    names.append(temp[0])


                for index, line in enumerate(user_list):
                    temp = line.split(",")
                    # if total_task_per_user >= 1 :
                    total_task_per_user = (f"{temp[0]}, {names.count(temp[0])}")
                    print(total_task_per_user)
                        # print(f"{temp[0]}")
                        # print(f"{names.count(temp[0])}")

# write users stats to file

        with open('user_overview.txt', 'w+') as f: # write all at once
            f.writelines(f"Total users:\t\t{total_tasks1}\n")
            f.writelines(f"Total tasks:\t\t{total_user1}\n")
            f.writelines(f"Total tasks per user:\t\t{total_task_per_user}\n") # prints last line, fix


#Finish Gr then read from Gr txt and alter menu and call funtion if gr not generated yet               
    elif  menu == 'ds' : 
        
        filename1 = "user.txt"
        with open(filename1,"r+") as file:
            num_users = len(file.readlines())     
        
        filename2 = "tasks.txt"
        with open(filename2,"r") as file:
            num_tasks = len(file.readlines())        

        print(f"Total Users:\t{num_users}")
        print(f"Total Tasks:\t{num_tasks}")

        
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
#######################--------------------#######################
# Program description:
# Task manager program - Allows you to Login as Admin or user, if registered
# Choose from variety of option of menu to edit and show stats of Tasks.

#######################--------------------#######################
# imports
from datetime import datetime as dt
import datetime
#######################--------------------#######################
# create .py file, and our .txt file, user.txt, task_overview.txt, tasks.txt, user_overview.txt
#Run program
#Steps:  Run terminal, steps, login, as admin or user and select option from menu's
#######################--------------------#######################

def register_user():
     
    print("Register as new user")
    new_username = (input("Please enter a new username:\n"))
    new_password = (input("Please enter a new password:\n"))
    new_password_verify = (input("Please confirm your password:\n"))
    if new_password == new_password_verify : 
            print("Password verified")  
            while True: 
                if new_username not in usernames and new_password_verify not in passwords:
                    
                        with open("user.txt","a+") as filename: 
                            filename.writelines("\n")
                            filename.writelines(new_username)
                            filename.writelines(", ")
                            filename.writelines(new_password_verify) 
                        print("You have entered the correct password & username and registered a new user")    
                        break
                else: 
                    print("Password or username already exists, please retry.")
                    break

def add_task():
     
     with open("tasks.txt","r+") as filename: 
        for lines in filename : 
            temp = lines.strip()
            temp = temp.split(", ")
            
        user_name_task = input("Please enter your username:\n")
        if user_name_task in usernames:
            task_title = input("Please enter your task title:\n")
            task_description = input("Please enter your task description:\n")
            task_due_date = input("Please enter the due date of task, format exact ie 23 Mar 2023:\n") 
            current_date = dt.today().strftime("%d %b %Y") # string current date
            task_complete = "No"
            task_number = int(input("Please input a number for your task\n"))
            with open("tasks.txt","a+") as filename:
                filename.write(f"\n{user_name_task}, {task_title}, {task_description}, {task_due_date}, {current_date}, {task_complete}, {task_number}")
                print("You have created a new task")
        else:
                print("Username does not exist, cannot add a task")


def view_all():
     
     with open("tasks.txt","r+") as filename: 
        for lines in filename : 
            temp = lines.strip()
            temp = temp.split(",")
            print("_________________________________________________________\n")  
            print(f"Tasks:\t\t\t{temp[1]}")   
            print(f"Assigned to:{temp[0]}")   
            print(f"Date assigned:\t\t{temp[4]}")  
            print(f"Due date:\t\t{temp[3]}")
            print(f"Task Complete:\t\t\t{temp[5]}")
            print(f"Task Description:\t{temp[2]}")
            print(f"Task number:\t\t{temp[6]}")
            print("_________________________________________________________\n")

def view_mine():

    vm_lists = []
    has_tasks = False # boolean
    with open("tasks.txt","r+") as file: 
        for lines in file : 
            temp = lines.strip()
            temp = temp.split(",")
            vm_lists.append(temp)   
       
            if user_name == temp[0]: 
                has_tasks = True    
                print("_________________________________________________________\n")  
                print(f"Tasks:\t\t\t{temp[1]}")   
                print(f"Assigned to:\t\t{temp[0]}")   
                print(f"Date assigned:\t\t{temp[4]}")  
                print(f"Due date:\t\t{temp[3]}")
                print(f"Task Complete:\t\t{temp[5]}")
                print(f"Task Description:\t{temp[2]}")
                print(f"Task number:\t\t{temp[6]}")
                print("_________________________________________________________\n")
        if not has_tasks: 
                print("You did not have a task") 
                return    
        task_user_number = (input("Please enter the  task number you would like to edit or -1 to return to menu\n")) 
            
        for lines in vm_lists:       
            if task_user_number == "-1" :
                break
            elif lines[6].strip() == task_user_number  and lines[5].strip() == "No":  
                print("Mark task as complete or edit task, Username or due date")
    

def mark_task():
        
        task_user_number = (input("Enter task number to edit\n"))
        idx = int(task_user_number) - 1                          
        
        with open('tasks.txt', 'r') as f:
                file = f.readlines()
                task_completed = input('Please enter, Yes, if task completed\n')
                line = file[idx].split(',')
                line[5] = task_completed 
                file[idx] = ','.join(line)

        with open('tasks.txt', 'w') as f:
                for line in file:
                    f.write(line)
                    print("Task marked completed successfully")


def edit_task():

    task_user_number = (input("Enter task number to edit\n"))
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
            print("Task username edited successfully")

def edit_due_date():
        
        task_user_number = (input("Enter task number to edit\n"))
        idx = int(task_user_number) - 1                          
        with open('tasks.txt', 'r') as f:
            file = f.readlines()
            edit_due_date = input("Edit, task_due_date, ie exact 28 Dec 2023,':\n")
            line = file[idx].split(',')
            line[4] = edit_due_date
            file[idx] = ','.join(line)

        with open('tasks.txt', 'w') as f:
            for line in file:
                f.write(line) 
                print("Task due date edited successfully")   

def generate_reports():
    try:
        with open("tasks.txt", "r") as f:
            task_list = f.readlines()
            total_tasks = len(task_list)
            completed_tasks = 0
            uncompleted_tasks = 0
            overdue = 0
            per_incomplete = 0
            per_overdue = 0
            for line in task_list:
                temp = line.strip().split(",")
                if temp[5].strip().lower() == 'yes':
                    completed_tasks += 1
                else:
                    uncompleted_tasks += 1
                if check_overdue(temp[4]):
                    overdue += 1
            per_incomplete = round((uncompleted_tasks / total_tasks * 100), 2)
            per_overdue = round((overdue / total_tasks * 100), 2)

        with open('task_overview.txt', 'w') as f:
            f.write(f"Total tasks:\t\t{total_tasks}\n")
            f.write(f"Completed tasks:\t{completed_tasks}\n")
            f.write(f"Uncompleted tasks:\t{uncompleted_tasks}\n")
            f.write(f"Overdue tasks:\t\t{overdue}\n")
            f.write(f"% Incomplete tasks:\t{per_incomplete}%\n")
            f.write(f"% Overdue tasks:\t{per_overdue}%\n")

    except FileNotFoundError:
        print("The file you are trying to read does not exist.")

    try:

        # with open("user.txt", "r+") as f:
        #     users = f.readlines()
        #     total_tasks_for_users = []
        #     per_total_task_user1 = 0
        #     per_total_task_user1_completed = 0
        #     per_total_task_user1_not_completed = 0
        #     per_total_task_user1_not_completed_and_overdue = 0
            
        #     for user in users:
        #         username = user.strip().split(",")[0]
        #         user_tasks = [task for task in task_list if task.startswith(username)]
        #         total_tasks_for_users.append(f"{username}: {len(user_tasks)} tasks")
                
        #         if username == "user1":
        #             user1_completed_tasks = [task for task in user_tasks if task.strip().split(", ")[5] == "Yes"]
        #             user1_not_completed_tasks = [task for task in user_tasks if task.strip().split(", ")[5] == "No"]
        #             user1_not_completed_and_overdue_tasks = [task for task in user1_not_completed_tasks if check_overdue(task.strip().split(", ")[4])]
                    
        #             per_total_task_user1 = round(len(user_tasks) / total_tasks * 100, 2)
        #             per_total_task_user1_completed = round(len(user1_completed_tasks) / total_tasks * 100, 2)
        #             per_total_task_user1_not_completed = round(len(user1_not_completed_tasks) / total_tasks * 100, 2)
        #             per_total_task_user1_not_completed_and_overdue = round(len(user1_not_completed_and_overdue_tasks) / total_tasks * 100, 2)

        with open("user.txt", "r") as f:
            user_list = f.readlines()
            total_users = len(user_list)
            total_tasks_per_user = []
            for line in user_list:
                user = line.strip().split(", ")
                username = user[0]
                count = 0
                for task in task_list:
                    temp = task.strip().split(",")
                    if temp[0] == username:
                        count += 1
                total_tasks_per_user.append((username, count))

        # with open('user_overview.txt', 'w+') as f:
        #     f.writelines(f"Total users:\t\t{total_users}\n")
        #     f.writelines(f"Total tasks:\t\t{total_tasks}\n")
        #     for user, count in total_tasks_per_user:
        #         f.writelines("\n".join(total_tasks_for_users) + "\n")
        #         f.writelines(f"% of total task for user:\t\t{per_total_task_user1}%\n")
        #         f.writelines(f"% of total task for user completed:\t\t{per_total_task_user1_completed}%\n")
        #         f.writelines(f"% of total task for user not completed:\t\t{per_total_task_user1_not_completed}%\n")
        #         f.writelines(f"% of total task for user not completed & overdue:\t\t{per_total_task_user1_not_completed_and_overdue}%\n")


        with open("user.txt", "r") as f:
            user_list = f.readlines()
            total_users = len(user_list)
            total_tasks_per_user = []
            for line in user_list:
                user = line.strip().split(", ")
                username = user[0]
                count = 0
                for task in task_list:
                    temp = task.strip().split(",")
                    if temp[0] == username:
                        count += 1
                total_tasks_per_user.append((username, count))
        
        with open('user_overview.txt', 'w') as f:
            f.write(f"Total users:\t\t{total_users}\n")
            f.write(f"Total tasks:\t\t{total_tasks}\n")
            for user, count in total_tasks_per_user:
                f.write(f"Total tasks for {user}:\t{count}\n")
                f.write(f"% of total tasks for {user}:\t{round((count / total_tasks * 100), 2)}%\n")

    except FileNotFoundError:
        print("The file you are trying to read does not exist.")

def display_stats():  
    
    try:
        print("-------------------------")
        print("task overview stats")
        with open("task_overview.txt","r") as file:
            for lines in file:
                temp = lines.strip()
                temp = temp.split(",")
                print(lines)
        print("-------------------------")
    except FileNotFoundError:
            print("The File you are trying to read does not exist, report will be generated automatically.")
            generate_reports()

    try:  
        print("-------------------------")
        print("user overview stats")  
        with open("user_overview.txt","r") as file:
            for lines in file:
                temp = lines.strip()
                temp = temp.split(",")
                print(lines)
        print("-------------------------")
    except FileNotFoundError:
            print("The File you are trying to read does not exist, report will be generated automatically.")
            generate_reports()

            
def check_overdue(due_date):

    due_date = due_date.strip() 
    current_date = dt.today().strftime("%d %b %Y")
    current_date = dt.today().strptime(current_date, "%d %b %Y")
    date_due_gr = dt.strptime(due_date, '%d %b %Y')
    if current_date > date_due_gr  :
        return True
    return False



#######################--------------------#######################
# login
usernames = []
passwords = []
# with open no need to close the file
with open("user.txt","r") as file: 
    for lines in file : 
        temp = lines.strip()
        temp = temp.split(", ")
        usernames.append(temp[0])
        passwords.append(temp[1])
        
print("Please login in using your username and password.")


while True:     
    user_name = input("Please enter your username:\n")
    pass_word = input("Please enter your password:\n") 

    if user_name in usernames :
        username_pass_index = usernames.index(user_name)
        if pass_word == passwords[username_pass_index]:
            print("You have logged in, Correct username and password entered")
            break
        print("Password incorrect")
    else:   
        print("Login unsuccessful, Please retry!")
  
#######################--------------------#######################
# Admin Menu
while True:

    if user_name == 'admin':
        menu = input('''Please select one of the following options below:
r - Registering a user.
a - Adding a task.
va - View all tasks.
vm - View my task.
gr - Generate reports.
ds - Display Statistics. 
e - Exit.
 ''').lower() #ds must not break if gr not generated, create

#######################--------------------#######################
# User Menu
    else:
        menu = input('''Please select one of the following options:
a - Add task.
va - View all tasks.
vm - View my task.
e - Exit.
 ''').lower().strip() 
    if menu == 'r' and user_name == 'admin': 
        register_user()
    
    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()   

    elif menu == 'vm': 
        view_mine()
#######################--------------------#######################
# View Mine Menu

        menu_VM = input('''Please select one of the following options:
mt - Mark Task
et - Edit task user
ed - Edit due date
ex - Exit.
''').lower().strip()                             
    
        if menu_VM == "mt":  
            mark_task()

        elif menu_VM == "et": 
            edit_task() 

        elif menu_VM == "ed":
            edit_due_date()

        elif menu_VM == "ex":
            print("Goodbye! Rerun program.")
            exit() 


    elif menu == 'gr':  
        generate_reports()

    elif  menu == 'ds' : 
        display_stats()
 
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")   
        

            

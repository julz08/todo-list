from tinydb import TinyDB, Query
db = TinyDB('./db.json')

todos = Query()

while True:
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    
    userinput = input("Enter your command: ")
    if userinput.lower() == 'create' or userinput == "1":
        task = input("What task would you like to add? ")
        importance = input("Of what importance is this? (High, Medium, Low) ")
        due = input("When is this due? ")
        create = db.insert({'task': task, 'importance': importance, "dueDate" : due})
    elif userinput.lower() == 'read' or userinput == "2":
        asklevel = input("Would you like to read all or one? (Enter all or one) ")
        if asklevel.lower() == 'all':
            allData = db.all()
            for data in allData:
                print(f'To-do {data.doc_id}: Task: {data["task"]}, Importance: {data["importance"]}, Due Date: {data["dueDate"]}')
        elif asklevel.lower() == 'one':
            itemlist = input("Which task are you looking for? (Enter the name of the task) ")
            read = db.search(todos.task == itemlist)
            if read:
                print(f'Task found: {read}')
            else:
                print("Task not found.")
        else:
            print("You didn't enter 'all' or 'one'")
    elif userinput.lower() == 'update' or userinput == "3":
        task = input("Which task do you want to update? ")
        nameTask = input("What name do you want to change it to? ")
        update = db.update({'task': nameTask}, todos.task == task)
    elif userinput.lower() == 'delete' or userinput == "4":
        taskDelete = input("What task do you want to delete? ")
        delete = db.remove(todos.task == taskDelete)
    else:
        print("You did not enter the command name or the command number.")
    
    
    


# create = db.insert
# read = db.all()
# update = db.update({'changed data'}, where you want to update)
# delete = db.remove